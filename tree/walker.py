from tree import Tree, LeafNode


class PreorderWalker:
    def __init__(self, tree):
        self.tree = tree
        self.current = tree
        self.route = []

    def __next__(self):
        result = self.current
        if result is None:
            raise StopIteration()
        if isinstance(self.current, Tree):
            self.__walk_to(self.current.children[0])
        elif isinstance(self.current, LeafNode):
            next_node = self.__rise()
            if next_node is None:
                self.current = None
            else:
                self.__walk_to(next_node)
        return result

    def __walk_to(self, node):
        self.route.append(self.current)
        self.current = node

    def __back(self):
        self.current = self.route[-1]
        del self.route[-1]

    def __next_sibling_index(self):
        parent = self.route[-1]
        index = parent.children.index(self.current)
        if len(parent.children) > index + 1:
            return index + 1

    def __rise(self):
        next_sibling_index = None
        while next_sibling_index is None:
            if not self.route:
                return None
            next_sibling_index = self.__next_sibling_index()
            self.__back()
        return self.current.children[next_sibling_index]
