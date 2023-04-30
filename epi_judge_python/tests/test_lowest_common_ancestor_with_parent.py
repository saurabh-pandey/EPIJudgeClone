from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_with_parent_prototype import BinaryTreeNode as N

import pdb

class TestLowestCommonAncestorWithParent(TestBase):
    def test_example1(self):
        nodes = [1, 2, 3, 4, 5, None, 6, None, 7, 8, 9, None, None, None, None, None, None, 10]
        # pdb.set_trace()
        print(f"Original nodes = {nodes}")
        tree = binary_tree.deserialize_level_order(nodes)
        # pdb.set_trace()
        new_nodes = binary_tree.serialize_level_order(tree)
        print(f"Computed nodes = {new_nodes}")
        # node0 = binary_tree.find_node(tree, 7)
        # node1 = binary_tree.find_node(tree, 5)
        # expected = binary_tree.find_node(tree, 2)
        # result = self.solve(tree, node0, node1)
        # assert result is expected, (
        #     f"expected = {expected.data}, result = {result.data}")
