from tree import postorder


class Forest:
    def __init__(self, tree, indexer, indices):
        assert indices[1] >= indices[0]
        self.tree = tree
        self.indexer = indexer
        self.indices = indices
        self.head = self.__find_head()
        self.__first_leaf_index = self.__find_first_leaf_index() if self.head is not None else None

    @property
    def head_forest(self):
        if self.__first_leaf_index is not None and self.__first_leaf_index < self.indices[1]:
            return self.child((self.__first_leaf_index, self.indices[1] - 1))
        else:
            return self.child()

    @property
    def tail_forest(self):
        if self.__first_leaf_index is not None:
            return self.child((self.indices[0], self.__first_leaf_index))
        else:
            return self.child()

    @property
    def except_head_forest(self):
        if len(self):
            return self.child((self.indices[0], self.indices[1] - 1))
        else:
            return self.child()

    def child(self, indices=(0, 0)):
        return Forest(self.tree, self.indexer, indices)

    @property
    def cache_key(self):
        return ':'.join([str(self.indices[0]), str(self.indices[1])])

    def all_nodes(self):
        return self.indexer[self.indices[0]:self.indices[1]]

    def __eq__(self, other):
        return isinstance(other, Forest) and len(self) == len(other) and self.all_nodes() == other.all_nodes()

    def __len__(self):
        return self.indices[1] - self.indices[0]

    def __find_head(self):
        return self.indexer[self.indices[1] - 1] if self.indices[1] > self.indices[0] else None

    def __find_first_leaf_index(self):
        return self.indexer.index(next(postorder(self.head)))


def distance(tree1, tree2):
    return Distance(tree1, tree2).calculate()


class Distance:
    def __init__(self, ltree, rtree):
        lforest = Forest(ltree, postorder(ltree).indexer(), (0, len(ltree)))
        rforest = Forest(rtree, postorder(rtree).indexer(), (0, len(rtree)))
        self.tree = DistanceTree(lforest, rforest, None)

    def calculate(self):
        for node in self.tree:
            node.calculate()
        return self.tree.value


class CalculationTree:
    def __init__(self, parent, cache_key):
        self.cache_key = '/'.join([type(self).__name__, cache_key])
        self.cache = parent.cache if parent else {}
        self.__value = self.cache[self.cache_key] if self.cache_key in self.cache else None
        self.parent = parent
        self.built = False
        self._children = []

    def build(self):
        if self.built:
            return
        self._build()
        self.built = True

    def calculate(self):
        pass

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
        self.cache[self.cache_key] = new_value

    @property
    def children(self):
        self.build()
        return self._children if self.value is None else []

    def __iter__(self):
        return Visitor(self)


class DistanceTree(CalculationTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(parent, '/'.join([lforest.cache_key, rforest.cache_key]))
        self.lforest = lforest
        self.rforest = rforest

    def _build(self):
        if self.lforest == self.rforest:
            self.value = 0
        elif not len(self.lforest) or not len(self.rforest):
            self.value = max(len(self.lforest), len(self.rforest))
        else:
            self._children = [
                HeadDistanceTree(self.lforest, self.rforest, self),
                LeftDistanceTree(self.lforest, self.rforest, self),
                RightDistanceTree(self.lforest, self.rforest, self),
            ]

    def calculate(self):
        if self.value is None:
            self.value = min(child.value for child in self.children)
            self._children = []


class CostSummingTree(CalculationTree):
    def calculate(self):
        if self.value is None:
            self.value = self.cost + sum(child.value for child in self.children)
            self._children = []

    def _cost(self, lforest, rforest):
        if lforest.head is None and rforest.head is None:
            return 0
        elif lforest.head is None or rforest.head is None:
            return 1
        else:
            return 0 if lforest.head.value == rforest.head.value else 1


class HeadDistanceTree(CostSummingTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(parent, '/'.join([lforest.cache_key, rforest.cache_key]))
        self.cost = self._cost(lforest, rforest)
        self.lforest = lforest
        self.rforest = rforest

    def _build(self):
        self._children = [
            DistanceTree(self.lforest.head_forest, self.rforest.head_forest, self),
            DistanceTree(self.lforest.tail_forest, self.rforest.tail_forest, self),
        ]


class LeftDistanceTree(CostSummingTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(parent, '/'.join([lforest.cache_key, rforest.cache_key]))
        self.cost = self._cost(lforest, rforest.child())
        self.lforest = lforest
        self.rforest = rforest

    def _build(self):
        self._children = [DistanceTree(self.lforest.except_head_forest, self.rforest, self)]


class RightDistanceTree(LeftDistanceTree):
    def __init__(self, lforest, rforest, parent):
        super().__init__(rforest, lforest, parent)  # reverse


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
