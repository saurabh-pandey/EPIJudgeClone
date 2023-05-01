from tests.test_base import TestBase
from tests.utils import binary_tree

import pdb

class TestBinaryTreeUtils(TestBase):
    def test_level_order(self):
        nodes = [1, 2, 3, 4, 5, None, 6, None, 7, 8, 9, None, None, None, None, None, None, 10]
        # pdb.set_trace()
        print(f"Original nodes = {nodes}")
        tree = binary_tree.LevelOrder.deserialize(nodes)
        # pdb.set_trace()
        new_nodes = binary_tree.LevelOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
        # node0 = binary_tree.find_node(tree, 7)
        # node1 = binary_tree.find_node(tree, 5)
        # expected = binary_tree.find_node(tree, 2)
        # result = self.solve(tree, node0, node1)
        # assert result is expected, (
        #     f"expected = {expected.data}, result = {result.data}")
        nodes = [1, 2, 3]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.LevelOrder.deserialize(nodes)
        new_nodes = binary_tree.LevelOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
    
    def test_pre_order(self):
        nodes = [1, 2, None, 4, None, None, 3]
        # pdb.set_trace()
        print(f"Original nodes = {nodes}")
        tree = binary_tree.PreOrder.deserialize(nodes)
        # pdb.set_trace()
        new_nodes = binary_tree.PreOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
        # node0 = binary_tree.find_node(tree, 7)
        # node1 = binary_tree.find_node(tree, 5)
        # expected = binary_tree.find_node(tree, 2)
        # result = self.solve(tree, node0, node1)
        # assert result is expected, (
        #     f"expected = {expected.data}, result = {result.data}")
        nodes = [1, 2, 3]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.PreOrder.deserialize(nodes)
        new_nodes = binary_tree.PreOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
