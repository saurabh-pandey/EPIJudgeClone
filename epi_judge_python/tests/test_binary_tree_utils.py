from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_node import BinaryTreeNode as N


class TestBinaryTreeUtils(TestBase):
    def test_tree1(self):
        tree = N(1, N(2, N(4), N(5, N(8), None)),
             N(3, N(6, None, N(9)), N(7, None, N(10, N(11), N(12)))))
        # Test all functionalities on this tree
    
    def test_level_order(self):
        nodes = [1, 2, 3, 4, 5, None, 6, None, 7, 8, 9, None, None, None, None, None, None, 10]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.LevelOrder.deserialize(nodes)
        new_nodes = binary_tree.LevelOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
        nodes = [1, 2, 3]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.LevelOrder.deserialize(nodes)
        new_nodes = binary_tree.LevelOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
    
    def test_pre_order(self):
        nodes = [1, 2, None, 4, None, None, 3]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.PreOrder.deserialize(nodes)
        new_nodes = binary_tree.PreOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
        nodes = [1, 2, 3]
        print(f"Original nodes = {nodes}")
        tree = binary_tree.PreOrder.deserialize(nodes)
        new_nodes = binary_tree.PreOrder.serialize(tree)
        print(f"Computed nodes = {new_nodes}")
