import pytest

from tree import build_tree, Tree, LeafTree, LeafNode, NoneNode


@pytest.fixture
def data1():
    return {
        'a': {
            'b': {
                'c': 1
            },
            'd': 2
        }
    }


@pytest.fixture
def tree1(data1):
    return build_tree(data1)


class TestForest:
    def test_init(self, tree1):
        assert type(tree1) is Tree
        assert tree1.value is None

    def test_get_child(self, tree1):
        subtree = tree1.get('a')
        assert type(subtree) is Tree
        assert subtree.value is 'a'

    def test_get_child_with_unknown_key(self, tree1):
        node = tree1.get('x')
        assert type(node) is NoneNode

    def test_get(self, tree1):
        subtree = tree1.get('a/b/c')
        assert type(subtree) is LeafTree
        assert subtree.value is 'c'
        leaf = subtree.children[0]
        assert type(leaf) is LeafNode
        assert leaf.value is 1

    def test_get_with_unknown_keys(self, tree1):
        node = tree1.get('a/b/c/d/e/f/g')
        assert type(node) is NoneNode
