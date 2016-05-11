class NodeIndexer:
    def __init__(self, walker):
        self.walker = walker
        self.__nodes = []

    def __walk(self):
        next_node = next(self.walker)
        self.__nodes.append(next_node)
        return next_node

    def index(self, node):
        try:
            while node not in self.__nodes:
                self.__walk()
        except StopIteration:
            pass
        return self.__nodes.index(node)

    def __getitem__(self, index):
        if len(self.walker.root) <= index:
            return self.__nodes[index]
        while len(self.__nodes) <= index:
            self.__walk()
        return self.__nodes[index]
