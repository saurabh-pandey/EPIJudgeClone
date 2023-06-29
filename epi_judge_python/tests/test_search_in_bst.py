from typing import Optional

from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils.bst import Factory

class TestSearchInBst(TestBase):
    def test_example1(self):
        tree: BstNode = Factory.three_layered(BstNode)
        for i in range(1, 8):
            node: Optional[BstNode] = self.solve(tree, i)
            assert node is not None, f"Expected not None node"
            assert node.data == i, f"Expected {i} != {node.data} result"
        for i in (0, 8, 9):
            node: Optional[BstNode] = self.solve(tree, i)
            assert node is None, f"Expected node to be None"
