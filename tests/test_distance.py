import pytest

from tree import build_tree
from tree.distance import tree_edit_distance


@pytest.fixture
def tree1():
    return build_tree({
        'a': {
            'b': 1
        }
    })


def test_tree_edit_distance_from_head(tree1, tree2):
    distance = tree_edit_distance(tree1, tree2)
    assert distance == 1


def test_tree_edit_distance_from_right_forest(tree1, tree3):
    distance = tree_edit_distance(tree1, tree3)
    assert distance == 1


def test_tree_edit_distance_from_left_forest(tree1, tree4):
    distance = tree_edit_distance(tree1, tree4)
    assert distance == 2


def test_tree_edit_distance_identity(tree1):
    distance = tree_edit_distance(tree1, tree1)
    assert distance == 0


def test_tree_edit_distance_symmetry(tree2, tree4):
    distance = tree_edit_distance(tree2, tree4)
    reverse_distance = tree_edit_distance(tree4, tree2)
    expected = 2
    assert distance == expected
    assert reverse_distance == expected


def test_tree_edit_distance_subadditivity(tree1, tree2, tree4):
    d1 = tree_edit_distance(tree1, tree2)
    d2 = tree_edit_distance(tree1, tree4)
    d3 = tree_edit_distance(tree2, tree4)
    assert d1 + d2 > d3
    assert d1 + d3 > d2
    assert d2 + d3 > d1
