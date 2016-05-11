import pytest

from tree import preorder


class TestNodeIndexer:
    @pytest.fixture
    def preorder_indexer1(self, tree1):
        return preorder(tree1).indexer()

    def test_index(self, tree1, preorder_indexer1):
        for (index, node) in enumerate(preorder(tree1)):
            assert preorder_indexer1.index(node) is index

    def test_index_does_not_contain(self, tree2, preorder_indexer1):
        with pytest.raises(ValueError):
            preorder_indexer1.index(tree2) is 0

    def test_getitem(self, tree1, preorder_indexer1):
        for (index, node) in enumerate(preorder(tree1)):
            assert preorder_indexer1[index] is node

    def test_getitem_out_of_range(self, tree1, preorder_indexer1):
        with pytest.raises(IndexError):
            preorder_indexer1[len(tree1)]
