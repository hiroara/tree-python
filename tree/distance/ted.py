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


def distance(tree1, tree2):
    return __distance(Forest([tree1]), Forest([tree2]))


def __distance(forest1, forest2):
    if forest1 == forest2:
        return 0
    if not forest1.trees or not forest2.trees:
        return reduce(lambda total, tree: total + len(tree), forest1.trees + forest2.trees, 0)
    return min(
        __distance_from_head(forest1, forest2),
        __distance_from_right_forest(forest1, forest2),
        __distance_from_right_forest(forest2, forest1)
    )


def __distance_from_head(forest1, forest2):
    d_head = __distance_between_head_values(forest1, forest2)
    d_head_forest = __distance(forest1.head_forest, forest2.head_forest)
    d_tail_forest = __distance(forest1.tail_forest, forest2.tail_forest)
    return d_head + d_head_forest + d_tail_forest


def __distance_from_right_forest(forest1, forest2):
    d_head = __distance_between_head_values(forest1, Forest())
    d_head_forest = __distance(forest1.except_head_forest, forest2)
    return d_head + d_head_forest


def __distance_between_head_values(forest1, forest2):
    return 0 if forest1.head_value == forest2.head_value else 1
