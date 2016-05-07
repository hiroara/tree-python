from functools import reduce


class Node:
    def __init__(self, value):
        self.value = value

    def get_child(self, key):
        return NoneNode()


class Tree(Node):
    def __init__(self, value, data):
        super().__init__(value)
        if type(data) is dict:
            self.children = [Tree(key, value) for (key, value) in data.items()]
        else:
            self.children = [LeafNode(data)]

    def get(self, path):
        return reduce(lambda node, key: node.get_child(key), path.split('/'), self)

    def get_child(self, key):
        return next((node for node in self.children if node.value == key), NoneNode())


class LeafNode(Node):
    pass


class NoneNode(Node):
    def __init__(self):
        super().__init__(None)
