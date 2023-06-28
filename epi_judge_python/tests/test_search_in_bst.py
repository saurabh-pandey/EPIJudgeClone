from typing import Optional

from bst_node import BstNode

from tests.test_base import TestBase
from tests.utils.bst import Factory

class TestSearchInBst(TestBase):
    def test_example1(self):
        tree: BstNode = Factory.three_layered()
        print(tree)
        # value = 4
        # node: Optional[BstNode] = self.solve(tree, value)
        # assert node is not None, f"Expected not None node"
        # assert node.data == value, f"Expected {value} != {node.data} result"
