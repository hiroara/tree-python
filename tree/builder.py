from .structs import Tree, LeafTree, LeafNode


def build_tree(data, root_value=None):
    return Tree(root_value, __build_children(data))


def __build_children(data):
    assert type(data) is dict
    return [__build_child(key, val) for (key, val) in sorted(data.items(), key=lambda item: item[0])]


def __build_child(value, data):
    if type(data) is dict:
        return Tree(value, __build_children(data))
    else:
        return LeafTree(value, LeafNode(data))
