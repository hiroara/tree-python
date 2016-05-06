class Forest:
    def __init__(self, trees):
        self.trees = trees


class Tree:
    def __init__(self, data):
        assert type(data) is dict
        self.data = data

    def to_forest(self):
        return Forest([self])
