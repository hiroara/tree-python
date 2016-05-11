from tree.distance import tree_edit_distance


def test_tree_edit_distance_from_head(tree5, tree2):
    distance = tree_edit_distance(tree5, tree2)
    assert distance == 1


def test_tree_edit_distance_from_right_forest(tree5, tree3):
    distance = tree_edit_distance(tree5, tree3)
    assert distance == 1


def test_tree_edit_distance_from_left_forest(tree5, tree4):
    distance = tree_edit_distance(tree5, tree4)
    assert distance == 2


def test_tree_edit_distance_identity(tree5):
    distance = tree_edit_distance(tree5, tree5)
    assert distance == 0


def test_tree_edit_distance_with_complex_trees(tree1, tree4):
    distance = tree_edit_distance(tree1, tree4)
    assert distance == 5


def test_tree_edit_distance_symmetry(tree2, tree4):
    distance = tree_edit_distance(tree2, tree4)
    reverse_distance = tree_edit_distance(tree4, tree2)
    expected = 2
    assert distance == expected
    assert reverse_distance == expected


def test_tree_edit_distance_subadditivity(tree5, tree2, tree4):
    d1 = tree_edit_distance(tree5, tree2)
    d2 = tree_edit_distance(tree5, tree4)
    d3 = tree_edit_distance(tree2, tree4)
    assert d1 + d2 > d3
    assert d1 + d3 > d2
    assert d2 + d3 > d1
