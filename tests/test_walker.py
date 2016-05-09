import pytest

from tree import pretty_print
from tree.walker import PreorderWalker, PostorderWalker


class TestPreorderWalker:
    @pytest.fixture
    def walker1(self, tree1):
        return PreorderWalker(tree1)

    def test_next(self, tree1, walker1):
        pretty_print(tree1)
        assert next(walker1) is tree1
        assert next(walker1) is tree1.get('a')
        assert next(walker1) is tree1.get('a/b')
        assert next(walker1) is tree1.get('a/b/c')
        assert next(walker1) is tree1.get('a/b/c').leaf
        assert next(walker1) is tree1.get('a/d')
        assert next(walker1) is tree1.get('a/d').leaf
        assert next(walker1) is tree1.get('e')
        assert next(walker1) is tree1.get('e').leaf
        with pytest.raises(StopIteration):
            next(walker1)


class TestPostorderWalker:
    @pytest.fixture
    def walker1(self, tree1):
        return PostorderWalker(tree1)

    def test_next(self, tree1, walker1):
        pretty_print(tree1)
        assert next(walker1) is tree1.get('a/b/c').leaf
        assert next(walker1) is tree1.get('a/b/c')
        assert next(walker1) is tree1.get('a/b')
        assert next(walker1) is tree1.get('a/d').leaf
        assert next(walker1) is tree1.get('a/d')
        assert next(walker1) is tree1.get('a')
        assert next(walker1) is tree1.get('e').leaf
        assert next(walker1) is tree1.get('e')
        assert next(walker1) is tree1
        with pytest.raises(StopIteration):
            next(walker1)
