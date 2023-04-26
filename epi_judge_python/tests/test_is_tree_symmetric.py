from tests.test_base import TestBase

from binary_tree_node import BinaryTreeNode as N


class TestIsTreeSymmetric(TestBase):
    def test_example1(self):
        tree = N(314,
                 N(6, None, N(2, None, N(3))),
                 N(6, N(2, N(3)))
                )
        expected = True
        result = self.solve(tree)
        assert expected == result, f"Expected = {expected}, actual = {result}"
    
    def test_example2(self):
        tree = N(314,
                 N(6, None, N(561, None, N(3))),
                 N(6, N(2, N(6)))
                )
        expected = False
        result = self.solve(tree)
        assert expected == result, f"Expected = {expected}, actual = {result}"
    
    def test_example3(self):
        tree = N(314,
                 N(6, None, N(561, None, N(3))),
                 N(6, N(2))
                )
        expected = False
        result = self.solve(tree)
        assert expected == result, f"Expected = {expected}, actual = {result}"
    
    def test_only_root(self):
        tree = N(42)
        expected = True
        result = self.solve(tree)
        assert expected == result, f"Expected = {expected}, actual = {result}"
