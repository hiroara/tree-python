from functools import reduce

from tree import Tree


class Forest:
    def __init__(self, trees=[]):
        self.trees = trees

    @property
    def head(self):
        return self.trees[-1] if self.trees else None

    @property
    def head_forest(self):
        if isinstance(self.head, Tree):
            return Forest(self.head.children)
        else:
            return Forest()

    @property
    def tail_forest(self):
        return Forest(self.trees[:-1]) if len(self.trees) > 1 else Forest()

    @property
    def except_head_forest(self):
        if isinstance(self.head, Tree):
            return Forest(self.trees[:-1] + self.head.children)
        else:
            return Forest(self.trees[:-1])

    @property
    def head_value(self):
        return self.head.value if self.head else None

    def __eq__(self, other):
        return isinstance(other, Forest) and self.trees == other.trees

    def __hash__(self):
        return 17 + sum(hash(tree) for tree in self.trees)


def distance(tree1, tree2):
    return Distance(tree1, tree2).calculate()


class Distance:
    def __init__(self, ltree, rtree):
        self.tree = DistanceTree(Forest([ltree]), Forest([rtree]), None)

    def calculate(self):
        for node in self.tree:
            node.calculate()
        return self.tree.value


class CalculationNode:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def __iter__(self):
        return Visitor(self)


class CalculationTree(CalculationNode):
    def calculate(self):
        pass

    @property
    def children(self):
        return []


class Visitor:
    def __init__(self, node):
        self.root = node
        self.current = node
        self.__fall()

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        result = self.current
        if self.current.parent is None:
            self.current = None
        else:
            self.__walk()
        return result

    def __fall(self):
        while self.current.children:
            self.current = self.current.children[0]

    def __next_sibling(self):
        siblings = self.current.parent.children
        current_index = siblings.index(self.current)
        return siblings[current_index + 1] if len(siblings) > current_index + 1 else None

    def __walk(self):
        sibling = self.__next_sibling()
        if sibling is not None:
            self.current = sibling
            self.__fall()
        else:
            self.current = self.current.parent


class DistanceTree(CalculationTree):
    def __init__(self, lforest, rforest, parent):
        if lforest == rforest:
            super().__init__(0, parent)
        elif not lforest.trees or not rforest.trees:
            distance = reduce(lambda total, tree: total + len(tree), lforest.trees + rforest.trees, 0)
            super().__init__(distance, parent)
        else:
            super().__init__(None, parent)
            self.head = HeadDistanceTree(lforest, rforest, self)
            self.left = LeftDistanceTree(lforest, rforest, self)
            self.right = RightDistanceTree(lforest, rforest, self)

    @property
    def children(self):
        return [self.head, self.left, self.right] if self.value is None else []

    def calculate(self):
        if self.value is None:
            self.value = min(child.value for child in self.children)


class CostSummingTree(CalculationTree):
    def calculate(self):
        if self.value is None:
            self.value = self.cost + sum(child.value for child in self.children)

    def _cost(self, lforest, rforest):
        return 0 if lforest.head_value == rforest.head_value else 1


class HeadDistanceTree(CostSummingTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(None, parent)
        self.cost = self._cost(lforest, rforest)
        self.head = DistanceTree(lforest.head_forest, rforest.head_forest, self)
        self.tail = DistanceTree(lforest.tail_forest, rforest.tail_forest, self)

    @property
    def children(self):
        return [self.head, self.tail] if self.value is None else []


class LeftDistanceTree(CostSummingTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(None, parent)
        self.cost = self._cost(lforest, Forest())
        self.tail = DistanceTree(lforest.except_head_forest, rforest, self)

    @property
    def children(self):
        return [self.tail] if self.value is None else []


class RightDistanceTree(LeftDistanceTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(rforest, lforest, parent)  # reverse
