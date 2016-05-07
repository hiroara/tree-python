from .structs import Tree, LeafTree, LeafNode


def build_tree(data, root_value=None):
    return Tree(root_value, __build_children(data))


def __build_children(data):
    if __is_as_dict(data):
        return [__build_child(key, val) for (key, val) in sorted(data.items(), key=lambda item: item[0])]
    elif __is_as_list(data):
        return [__build_child(idx, val) for (idx, val) in enumerate(data)]
    raise Exception('Unsupported data type: {}'.format(data))


def __build_child(value, data):
    if __is_as_tree_data(data):
        return Tree(value, __build_children(data))
    else:
        return LeafTree(value, LeafNode(data))


def __is_as_dict(data):
    try:
        return callable(getattr(data, 'items'))
    except AttributeError:
        return False


def __is_as_list(data):
    try:
        return callable(getattr(data, '__iter__'))
    except AttributeError:
        return False


def __is_as_tree_data(data):
    return __is_as_dict(data) or __is_as_list(data)
