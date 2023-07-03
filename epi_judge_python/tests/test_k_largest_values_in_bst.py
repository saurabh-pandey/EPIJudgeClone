from tests.test_base import TestBase

from tests.utils import bst

from bst_node import BstNode

class TestKLargestInBst(TestBase):
    def test_example1(self):
        tree = bst.Factory.simple_even(BstNode)
        result = self.solve(tree, 1)
        expected = [6]
        assert result == expected, f"Expected {expected} != {result} result"
        result = self.solve(tree, 2)
        expected = [6, 4]
        assert result == expected, f"Expected {expected} != {result} result"
        result = self.solve(tree, 3)
        expected = [6, 4, 2]
        assert result == expected, f"Expected {expected} != {result} result"
        result = self.solve(tree, 4)
        expected = [6, 4, 2]
        assert result == expected, f"Expected {expected} != {result} result"
