from tests.test_base import TestBase

from tests.utils import bst

from bst_node import BstNode


class TestSearchFirstGreaterInBst(TestBase):
    def test_example1(self):
        tree: BstNode = bst.Factory.simple_even(BstNode)
        result: BstNode = self.solve(tree, 1)
        expected = 2
        assert result.data == expected, f"Expected {expected} != {result.data}"
        result: BstNode = self.solve(tree, 2)
        expected = 4
        assert result.data == expected, f"Expected {expected} != {result.data}"
        result: BstNode = self.solve(tree, 3)
        expected = 4
        assert result.data == expected, f"Expected {expected} != {result.data}"
        result: BstNode = self.solve(tree, 4)
        expected = 6
        assert result.data == expected, f"Expected {expected} != {result.data}"
        result: BstNode = self.solve(tree, 5)
        expected = 6
        assert result.data == expected, f"Expected {expected} != {result.data}"
        result: BstNode = self.solve(tree, 6)
        assert result == None, f"None != {result.data}"
        result: BstNode = self.solve(tree, 7)
        assert result == None, f"None != {result.data}"
