from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils import bst


class TestLowestCommonAncestorInBst(TestBase):
    def test_example1(self):
        tree: BstNode = bst.Factory.three_layered(BstNode)
        s: BstNode = bst.find_node(tree, 3)
        b: BstNode = bst.find_node(tree, 5)
        lca: BstNode = self.solve(tree, s, b)
        expected: BstNode = bst.find_node(tree, 4)
        assert lca is expected, f"Expected {expected.data} != {lca.data} lca"
        s: BstNode = bst.find_node(tree, 3)
        b: BstNode = bst.find_node(tree, 1)
        lca: BstNode = self.solve(tree, s, b)
        expected: BstNode = bst.find_node(tree, 2)
        assert lca is expected, f"Expected {expected.data} != {lca.data} lca"
        s: BstNode = bst.find_node(tree, 5)
        b: BstNode = bst.find_node(tree, 7)
        lca: BstNode = self.solve(tree, s, b)
        expected: BstNode = bst.find_node(tree, 6)
        assert lca is expected, f"Expected {expected.data} != {lca.data} lca"
        s: BstNode = bst.find_node(tree, 1)
        b: BstNode = bst.find_node(tree, 7)
        lca: BstNode = self.solve(tree, s, b)
        expected: BstNode = bst.find_node(tree, 4)
        assert lca is expected, f"Expected {expected.data} != {lca.data} lca"
        s: BstNode = bst.find_node(tree, 2)
        b: BstNode = bst.find_node(tree, 3)
        lca: BstNode = self.solve(tree, s, b)
        expected: BstNode = bst.find_node(tree, 2)
        assert lca is expected, f"Expected {expected.data} != {lca.data} lca"
