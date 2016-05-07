import pytest

from tree import Forest, Tree


class TestTree:
    @pytest.fixture
    def data1(self):
        return {
            'a': {
                'b': {
                    'c': 1
                },
                'd': 2
            }
        }

    @pytest.fixture
    def tree1(self, data1):
        return Tree(data1)

    def test_init(self, data1, tree1):
        assert type(tree1) is Tree
        assert tree1.data == data1

    def test_to_forest(self, tree1):
        forest = tree1.to_forest()
        assert type(forest) is Forest
        assert forest.trees == [tree1]
