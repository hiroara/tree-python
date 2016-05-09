import pytest

from tree import preorder


class TestNodeCollection:
    @pytest.fixture
    def preorder_collection1(self, tree1):
        return preorder(tree1).collection()

    def test_index(self, tree1, preorder_collection1):
        for (index, node) in enumerate(preorder(tree1)):
            assert preorder_collection1.index(node) is index

    def test_index_does_not_contain(self, tree2, preorder_collection1):
        with pytest.raises(ValueError):
            preorder_collection1.index(tree2) is 0

    def test_getitem(self, tree1, preorder_collection1):
        for (index, node) in enumerate(preorder(tree1)):
            assert preorder_collection1[index] is node

    def test_getitem_out_of_range(self, tree1, preorder_collection1):
        with pytest.raises(IndexError):
            preorder_collection1[len(tree1)]
