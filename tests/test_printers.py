from tree import pretty_text


def test_pretty_text(tree1):
    lines = pretty_text(tree1).split('\n')
    assert lines[0] == '+ {}'.format(str(tree1))
    assert lines[1] == '   + {}'.format(str(tree1.get('a')))
    assert lines[2] == '   |  + {}'.format(str(tree1.get('a/b')))
    assert lines[3] == '   |  |  + {}'.format(str(tree1.get('a/b/c')))
    assert lines[4] == '   |  |     + {}'.format(str(tree1.get('a/b/c').leaf))
