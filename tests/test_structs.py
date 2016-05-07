import copy

from tree import build_tree, Tree, LeafTree, LeafNode, NoneNode


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

    def test_eq(self, data1, tree1):
        data1['extra'] = 10
        tree2 = build_tree(data1)
        copy_tree = copy.deepcopy(tree1)
        assert copy_tree is not tree1
        assert copy_tree == tree1
        assert tree2 != tree1
