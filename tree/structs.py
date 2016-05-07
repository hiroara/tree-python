from functools import reduce


class Node:
    def __init__(self, value):
        self.value = value

    def get_child(self, key):
        return NoneNode()

    def __str__(self):
        return "<{}>".format(self.value)


class Tree(Node):
    def __init__(self, value, children):
        super().__init__(value)
        self.children = children

    def get(self, path):
        return reduce(lambda node, key: node.get_child(key), path.split('/'), self)

    def get_child(self, key):
        return next((node for node in self.children if node.value == key), NoneNode())

    def __str__(self):
        return '<T: {} (with {} nodes)>'.format(self.value, len(self.children))


class LeafTree(Tree):
    def __init__(self, value, leaf):
        super().__init__(value, [leaf])
        self.leaf = leaf


class LeafNode(Node):
    def __str__(self):
        return '<L: {}>'.format(self.value)


class NoneNode(Node):
    def __init__(self):
        super().__init__(None)
