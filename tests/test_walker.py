import pytest

from tree import pretty_print
from tree.walker import PreorderWalker


class TestPreorderWalker:
    @pytest.fixture
    def walker3(self, tree1):
        return PreorderWalker(tree1)

    def test_next(self, tree1, walker3):
        pretty_print(tree1)
        assert next(walker3) is tree1
        assert next(walker3) is tree1.get('a')
        assert next(walker3) is tree1.get('a/b')
        assert next(walker3) is tree1.get('a/b/c')
        assert next(walker3) is tree1.get('a/b/c').leaf
        assert next(walker3) is tree1.get('a/d')
        assert next(walker3) is tree1.get('a/d').leaf
        assert next(walker3) is tree1.get('e')
        assert next(walker3) is tree1.get('e').leaf
        with pytest.raises(StopIteration):
            next(walker3)
