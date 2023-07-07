from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils import bst


class TestBstFromPreorder(TestBase):
    def test_example1(self):
        tree: BstNode = bst.Factory.three_layered(BstNode)
        preorder_traversal = bst.generate_preorder(tree)
        result = self.solve(preorder_traversal)
        assert result == tree, f"Bst from preorder failed for {tree}"
    
    def test_single(self):
        tree: BstNode = bst.Factory.single_node(BstNode)
        preorder_traversal = bst.generate_preorder(tree)
        result = self.solve(preorder_traversal)
        assert result == tree, f"Bst from preorder failed for {tree}"
    
    def test_simple(self):
        tree: BstNode = bst.Factory.simple_even(BstNode)
        preorder_traversal = bst.generate_preorder(tree)
        result = self.solve(preorder_traversal)
        assert result == tree, f"Bst from preorder failed for {tree}"
    
    def test_left_leaning(self):
        tree: BstNode = bst.Factory.left_leaning(BstNode)
        preorder_traversal = bst.generate_preorder(tree)
        result = self.solve(preorder_traversal)
        assert result == tree, f"Bst from preorder failed for {tree}"
    
    def test_right_leaning(self):
        tree: BstNode = bst.Factory.right_leaning(BstNode)
        preorder_traversal = bst.generate_preorder(tree)
        result = self.solve(preorder_traversal)
        assert result == tree, f"Bst from preorder failed for {tree}"
