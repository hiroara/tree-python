import sys

from .structs import Node, Tree, LeafTree, LeafNode, NoneNode
from .builder import build_tree
from .parser import parse_json
from .printers import pretty_print, pretty_text
from .walker import preorder, postorder


def json2tree():
    pretty_print(parse_json(sys.stdin.read()))
