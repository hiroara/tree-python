class NodeIndexer:
    def __init__(self, walker):
        self.walker = walker
        self.__nodes = []

    def __walk(self):
        next_node = next(self.walker)
        self.__nodes.append(next_node)
        return next_node

    def index(self, node):
        result = self.__find_from_loaded(node)
        if result is None:
            result = self.__find_while_walking(node)
        if result is None:
            raise ValueError('{} is not in indexer'.format(node))
        else:
            return result

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        if index < 0:
            index = len(self) - index
        if len(self) <= index:
            raise IndexError('indexer index out of range')
        while len(self.__nodes) <= index:
            self.__walk()
        return self.__nodes[index]

    def __len__(self):
        return len(self.walker.root)

    def __find_from_loaded(self, node):
        for (idx, loaded) in enumerate(self.__nodes):
            if loaded is node:
                return idx

    def __find_while_walking(self, node):
        try:
            current = len(self.__nodes)
            while self.__walk() is not node:
                current += 1
            return current
        except StopIteration:
            return None
