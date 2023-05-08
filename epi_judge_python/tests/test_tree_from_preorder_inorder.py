from tests.test_base import TestBase

from tests.utils import binary_tree as bt

class TestTreeFromPreorderInorder(TestBase):
    def test_tree1(self):
        tree = bt.Factory.tree1()
        inorder = bt.generate_inorder(tree)
        preorder = bt.generate_preorder(tree)
        result = self.solve(preorder, inorder)
        assert bt.are_equal(tree, tree), "Incorrect construction of tree 1"
    
    def test_tree2(self):
        tree = bt.Factory.tree2()
        inorder = bt.generate_inorder(tree)
        preorder = bt.generate_preorder(tree)
        result = self.solve(preorder, inorder)
        assert bt.are_equal(tree, tree), "Incorrect construction of tree 2"
    
    def test_tree3(self):
        tree = bt.Factory.tree3()
        inorder = bt.generate_inorder(tree)
        preorder = bt.generate_preorder(tree)
        result = self.solve(preorder, inorder)
        assert bt.are_equal(tree, tree), "Incorrect construction of tree 3"
