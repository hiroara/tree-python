from .structs import Tree, LeafTree, LeafNode


def build_tree(data):
    return Tree(None, __build_children(data))


def __build_children(data):
    assert type(data) is dict
    return [__build_child(key, val) for (key, val) in data.items()]


def __build_child(value, data):
    if type(data) is dict:
        return Tree(value, __build_children(data))
    else:
        return LeafTree(value, LeafNode(data))
