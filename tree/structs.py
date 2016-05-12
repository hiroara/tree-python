from functools import reduce


class Node:
    def __init__(self, value):
        self.value = value

    def get_child(self, key):
        return NoneNode()

    def keys(self):
        return []

    def __str__(self):
        return "<{}>".format(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and other.value == self.value

    def __len__(self):
        return 1

    def __hash__(self):
        return 19 + hash(self.value)

    def __getitem__(self, key):
        return self.get_child(key)


class Tree(Node):
    def __init__(self, value, children):
        super().__init__(value)
        self.children = children
        self.__children_length = sum(len(child) for child in children)
        self.__children_hash = sum(hash(child) for child in children)

    def get(self, path):
        return reduce(lambda node, key: node.get_child(key), path.split('/'), self)

    def get_child(self, key):
        return next((node for node in self.children if node.value == key), NoneNode())

    def keys(self):
        return [child.value for child in self.children]

    def __str__(self):
        return '<T: {} (with {} nodes)>'.format(self.value, len(self.children))

    def __eq__(self, other):
        return isinstance(other, Tree) and super().__eq__(other) and other.children == self.children

    def __len__(self):
        return super().__len__() + self.__children_length

    def __hash__(self):
        return 13 + super().__hash__() + self.__children_hash


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
