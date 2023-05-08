from tests.test_base import TestBase

from tests.utils import binary_tree as bt

class TestTreeFromPreorderInorder(TestBase):
    def test_example1(self):
        tree = bt.Factory.tree1()
        inorder = bt.generate_inorder(tree)
        preorder = bt.generate_preorder(tree)
        result = self.solve(preorder, inorder)
        assert bt.are_equal(tree, tree), "Incorrect construction"
