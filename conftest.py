import pytest

from tree import build_tree


@pytest.fixture
def data1():
    return {
        'a': {
            'b': {
                'c': 1
            },
            'd': 2
        },
        'e': 4
    }


@pytest.fixture
def tree1(data1):
    return build_tree(data1)
