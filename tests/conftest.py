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


@pytest.fixture
def tree2():
    return build_tree({
        'a': {
            'c': 1
        }
    })


@pytest.fixture
def tree3():
    return build_tree({
        'b': 1
    })


@pytest.fixture
def tree4():
    return build_tree({
        'a': {
            'b': {
                'c': 3
            }
        }
    })
