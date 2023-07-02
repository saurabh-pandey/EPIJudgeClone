from binary_tree_node import BinaryTreeNode

from tests.test_base import TestBase

from tests.utils import binary_tree as btree
from tests.utils import bst

import pdb

class TestIsTreeBst(TestBase):
    def test_example1(self):
        tree = bst.Factory.three_layered(BinaryTreeNode)
        # pdb.set_trace()
        result = self.solve(tree)
        expected = True
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        tree = btree.Factory.tree1()
        result = self.solve(tree)
        expected = False
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example3(self):
        tree = btree.Factory.left_only()
        result = self.solve(tree)
        expected = False
        assert result == expected, f"Expected {expected} != {result} result"