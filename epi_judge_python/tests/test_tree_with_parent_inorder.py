from tests.test_base import TestBase

from tests.utils import binary_tree as bt


class TestTreeWithParentInorder(TestBase):
    def test_tree1(self):
        tree = bt.Factory.tree1(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_tree2(self):
        tree = bt.Factory.tree2(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_tree3(self):
        tree = bt.Factory.tree3(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_single_node(self):
        tree = bt.Factory.single_node(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_left_only(self):
        tree = bt.Factory.left_only(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
    
    def test_right_only(self):
        tree = bt.Factory.right_only(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
