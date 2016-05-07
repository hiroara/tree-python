import json
from tree import build_tree


def parse(json_str):
    return build_tree(json.loads(json_str))
