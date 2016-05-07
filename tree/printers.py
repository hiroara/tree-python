from tree import Node, Tree


def pretty_print(node):
    print(pretty_text(node))


def pretty_text(node, prefix='+ ', children_prefix='   '):
    return _build_printer(node, prefix, children_prefix).pretty_text()


def _build_printer(node, prefix, children_prefix):
    if isinstance(node, Tree):
        return TreePrinter(node, prefix, children_prefix)
    elif isinstance(node, Node):
        return NodePrinter(node, prefix)
    raise Exception('Unsupported node type: {}'.format(node))


class NodePrinter:
    def __init__(self, node, prefix):
        assert isinstance(node, Node)
        self.node = node
        self.prefix = prefix

    def pretty_text(self):
        return self.prefix + str(self.node)


class TreePrinter(NodePrinter):
    def __init__(self, node, prefix, children_prefix):
        assert isinstance(node, Tree)
        super().__init__(node, prefix)
        self.children_prefix = children_prefix
        self.children = [self.__build_child(child, node) for child in self.node.children]

    def pretty_text(self):
        lines = [self.children_prefix + child.pretty_text() for child in self.children]
        lines.insert(0, super().pretty_text())
        return '\n'.join(lines)

    def __build_child(self, node, parent):
        if node is parent.children[-1]:
            children_prefix = self.children_prefix + '   '
        else:
            children_prefix = self.children_prefix + '|  '
        return _build_printer(node, '+ ', children_prefix)
