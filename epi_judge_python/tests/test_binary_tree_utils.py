from tests.test_base import TestBase
from tests.utils import binary_tree

from binary_tree_node import BinaryTreeNode as N


class TestBinaryTreeUtils(TestBase):
    def test_tree1(self):
        tree = N(1,
                 N(2,
                   N(4),
                   N(5,
                     N(8),
                     None
                    )
                 ),
                 N(3,
                   N(6,
                     None,
                     N(9)
                    ),
                   N(7,
                     None,
                     N(10,
                       N(11),
                       N(12)
                      )
                    )
                 )
                )
        lo_serial_tree = binary_tree.LevelOrder.serialize(tree)
        lo_deserial_tree = binary_tree.LevelOrder.deserialize(lo_serial_tree)
        lo_reserial_tree = binary_tree.LevelOrder.serialize(lo_deserial_tree)
        assert lo_reserial_tree == lo_serial_tree
        po_serial_tree = binary_tree.PreOrder.serialize(tree)
        po_deserial_tree = binary_tree.PreOrder.deserialize(po_serial_tree)
        po_reserial_tree = binary_tree.PreOrder.serialize(po_deserial_tree)
        assert po_reserial_tree == po_serial_tree
        assert binary_tree.find_node(tree, 0) == None
        for i in range(1, 13):
            assert binary_tree.find_node(tree, i).data == i
        for i in range(13, 21):
            assert binary_tree.find_node(tree, i) == None
    
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
