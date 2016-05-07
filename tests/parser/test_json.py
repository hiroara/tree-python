import pytest
from tree import parse_json, Tree


@pytest.fixture
def json_tree1():
    return parse_json('{"a":{"b":3},"c":{"d":{"e":5}}}')


def test_parse_json(json_tree1):
    assert type(json_tree1) is Tree
    assert json_tree1.get('c/d/e').leaf.value == 5
