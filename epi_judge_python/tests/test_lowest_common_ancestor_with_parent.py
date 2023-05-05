from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_with_parent_prototype import BinaryTreeNode as N

import pdb

class TestLowestCommonAncestorWithParent(TestBase):
    def test_example1(self):
        nodes = [1, 2, 3, 4, 5, None, 6, None, 7, 8, 9, None, None, None, None, None, None, 10]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.LevelOrder.deserialize(nodes)

