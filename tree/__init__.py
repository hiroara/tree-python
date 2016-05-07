import sys

from .structs import Node, Tree, LeafTree, LeafNode, NoneNode
from .builder import build_tree
from .parser import parse_json
from .printers import pretty_text


def json2tree():
    print(pretty_text(parse_json(sys.stdin.read())))
