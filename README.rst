Library for tree data structure
===============================

::

  from tree import build_tree

  # Build tree data
  tree1 = build_tree({ 'a': { 'b': 1 }, 'c': 4})

  # Get value with path
  tree1.get('a/b').leaf.value # => 1

  # Pretty print
  from tree import pretty_print
  pretty_print(tree1)
  ## Output
  #
  # + <T: None (with 2 nodes)>
  #    + <T: a (with 1 nodes)>
  #    |  + <T: b (with 1 nodes)>
  #    |     + <L: 1>
  #    + <T: c (with 1 nodes)>
  #       + <L: 4>
  #
  ## Also you can get same output with `json2tree` command.

  # Tree Edit Distance
  from tree.distance import tree_edit_distance
  tree2 = build_tree({ 'e': 3, 'c': { 'a': 2 }, 'd': 4})
  tree_edit_distance(tree1, tree2) # => 6
