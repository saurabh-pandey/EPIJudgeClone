from typing import Optional

from tests.test_base import TestBase
from tests.utils import binary_tree as bt

from binary_tree_node import BinaryTreeNode as N
from binary_tree_with_parent_prototype import BinaryTreeNode as NodeWithParent


class TestBinaryTreeUtils(TestBase):
    def _check_tree(self, tree: Optional[N], max_key: Optional[int]):
        lo_serial_tree = bt.LevelOrder.serialize(tree)
        lo_deserial_tree = bt.LevelOrder.deserialize(lo_serial_tree)
        lo_reserial_tree = bt.LevelOrder.serialize(lo_deserial_tree)
        assert lo_reserial_tree == lo_serial_tree
        po_serial_tree = bt.PreOrder.serialize(tree)
        po_deserial_tree = bt.PreOrder.deserialize(po_serial_tree)
        po_reserial_tree = bt.PreOrder.serialize(po_deserial_tree)
        assert po_reserial_tree == po_serial_tree
        if max_key is not None:
            assert bt.find_node(tree, 0) == None
            for i in range(1, max_key + 1):
                assert bt.find_node(tree, i).data == i
            for i in range(max_key + 1, max_key + 20):
                assert bt.find_node(tree, i) == None
        else:
            for i in range(0, 20):
                assert bt.find_node(tree, i) == None
    
    def _check_tree_with_parent(self, tree: Optional[N],
                                max_key: Optional[int]):
        lo_serial_tree = bt.LevelOrder.serialize(tree)
        lo_deserial_tree = bt.LevelOrder.deserialize(lo_serial_tree,
                                                     NodeWithParent)
        if lo_deserial_tree is not None and lo_deserial_tree.left is not None:
            assert lo_deserial_tree.left.parent is lo_deserial_tree
        if lo_deserial_tree is not None and lo_deserial_tree.right is not None:
            assert lo_deserial_tree.right.parent is lo_deserial_tree
        lo_reserial_tree = bt.LevelOrder.serialize(lo_deserial_tree)
        assert lo_reserial_tree == lo_serial_tree
        po_serial_tree = bt.PreOrder.serialize(tree)
        po_deserial_tree = bt.PreOrder.deserialize(po_serial_tree, 
                                                   NodeWithParent)
        po_reserial_tree = bt.PreOrder.serialize(po_deserial_tree)
        assert po_reserial_tree == po_serial_tree
        if max_key is not None:
            assert bt.find_node(tree, 0) == None
            for i in range(1, max_key + 1):
                assert bt.find_node(tree, i).data == i
            for i in range(max_key + 1, max_key + 20):
                assert bt.find_node(tree, i) == None
        else:
            for i in range(0, 20):
                assert bt.find_node(tree, i) == None
    
    def test_tree1(self):
        tree = bt.BinaryTreeFactory.tree1()
        self._check_tree(tree, 12)
        self._check_tree_with_parent(tree, 12)
    
    def test_tree2(self):
        tree = bt.BinaryTreeFactory.tree2()
        self._check_tree(tree, 10)
        self._check_tree_with_parent(tree, 10)
    
    def test_single(self):
        tree = bt.BinaryTreeFactory.single_node()
        self._check_tree(tree, 1)
        self._check_tree_with_parent(tree, 1)
    
    def test_tree3(self):
        tree = bt.BinaryTreeFactory.tree3()
        self._check_tree(tree, 5)
        self._check_tree_with_parent(tree, 5)
    
    def test_empty(self):
        tree = None
        self._check_tree(tree, None)
        self._check_tree_with_parent(tree, None)
