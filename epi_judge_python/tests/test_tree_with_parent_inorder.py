from tests.test_base import TestBase

from tests.utils import binary_tree as bt


class TestTreeWithParentInorder(TestBase):
    def test_example1(self):
        tree = bt.Factory.tree1(True)
        result = self.solve(tree)
        expected = bt.generate_inorder(tree)
        assert result == expected, f"Expected = {expected}, result = {result}"
