from tree import Tree, LeafNode


class Walker:
    def __init__(self, tree):
        self.root = tree
        self.current = tree
        self.route = []

    def _walk_to(self, node):
        self.route.append(self.current)
        self.current = node

    def _back(self):
        self.current = self.route[-1]
        del self.route[-1]

    def _next_sibling_index(self):
        parent = self.route[-1]
        index = parent.children.index(self.current)
        if len(parent.children) > index + 1:
            return index + 1


class PreorderWalker(Walker):
    def __next__(self):
        result = self.current
        if result is None:
            raise StopIteration()
        if isinstance(self.current, Tree):
            self._walk_to(self.current.children[0])
        elif isinstance(self.current, LeafNode):
            next_node = self.__rise()
            if next_node is None:
                self.current = None
            else:
                self._walk_to(next_node)
        return result

    def __rise(self):
        next_sibling_index = None
        while next_sibling_index is None:
            if not self.route:
                return None
            next_sibling_index = self._next_sibling_index()
            self._back()
        return self.current.children[next_sibling_index]


class PostorderWalker(Walker):
    def __init__(self, tree):
        super().__init__(tree)
        self.__fall()

    def __next__(self):
        result = self.current
        if result is None:
            raise StopIteration()
        if not self.route:
            self.current = None
            return result
        next_sibling_index = self._next_sibling_index()
        self._back()
        if next_sibling_index is not None:
            self._walk_to(self.current.children[next_sibling_index])
            self.__fall()
        return result

    def __fall(self):
        while isinstance(self.current, Tree):
            self._walk_to(self.current.children[0])
