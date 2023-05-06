from abc import ABC, abstractmethod
from typing import List, Optional, Type, Union

from binary_tree_node import BinaryTreeNode as SimpleNode
from binary_tree_with_parent_prototype import BinaryTreeNode as NodeWithParent

BinTreeNode = Union[SimpleNode, NodeWithParent]


class Factory:
    '''
    Factory for some standard binary trees used in tests
    '''
    @staticmethod
    def single_node(with_parent: bool = False) -> SimpleNode:
        tree = SimpleNode(1)
        return Factory._fetch_tree(tree, with_parent)
    
    @staticmethod
    def tree1(with_parent: bool = False) -> SimpleNode:
        tree = SimpleNode(1,
            SimpleNode(2,
                SimpleNode(4),
                SimpleNode(5,
                    SimpleNode(8),
                    None)
                ),
            SimpleNode(3,
                SimpleNode(6,
                    None,
                    SimpleNode(9)
                ),
                SimpleNode(7,
                    None,
                    SimpleNode(10,
                        SimpleNode(11),
                        SimpleNode(12)
                    )
                )
            )
        )
        return Factory._fetch_tree(tree, with_parent)
    
    @staticmethod
    def tree2(with_parent: bool = False) -> SimpleNode:
        tree = SimpleNode(1,
            SimpleNode(2,
                SimpleNode(4,
                    None,
                    SimpleNode(7)
                ),
                SimpleNode(5,
                    SimpleNode(8),
                    SimpleNode(9,
                        SimpleNode(10)
                    )
                )
            ),
            SimpleNode(3,
                None,
                SimpleNode(6)
            )
        )
        return Factory._fetch_tree(tree, with_parent)
    
    @staticmethod
    def tree3(with_parent: bool = False) -> SimpleNode:
        tree = SimpleNode(1,
            SimpleNode(2,
                None,
                SimpleNode(4)
            ),
            SimpleNode(3,
                SimpleNode(5)
            )
        )
        return Factory._fetch_tree(tree, with_parent)
    
    @staticmethod
    def _fetch_tree(tree: SimpleNode, with_parent: bool = False) -> BinTreeNode:
        if with_parent:
            return LevelOrder.deserialize(
                LevelOrder.serialize(tree), NodeWithParent)
        else:
            return tree



class SerializeDeserialize(ABC):
    '''
    Binary tree serializers and deserializers
    '''
    @abstractmethod
    def serialize(tree: Optional[BinTreeNode]) -> List[Optional[int]]:
        pass

    @abstractmethod
    def deserialize(nodes: List[Optional[int]]) -> Optional[BinTreeNode]:
        pass


class LevelOrder(SerializeDeserialize):
    def serialize(tree: Optional[BinTreeNode]) -> List[Optional[int]]:
        if tree is None:
            return []
        nodes_queue = [tree]
        serialized_tree = [tree.data]
        while nodes_queue:
            node = nodes_queue.pop(0)
            if node:
                serialized_tree.append(node.left.data if node.left else None)
                serialized_tree.append(node.right.data if node.right else None)
                nodes_queue.append(node.left)
                nodes_queue.append(node.right)
        while serialized_tree[-1] is None:
            serialized_tree.pop()
        return serialized_tree
    
    def deserialize(nodes: List[Optional[int]],
                    NodeCls: Type[BinTreeNode] = SimpleNode
                    ) -> Optional[BinTreeNode]:
        if not nodes:
            return None
        cloned_nodes = nodes[:]
        root_key = None
        while root_key is None:
            root_key = cloned_nodes.pop(0)
        root = NodeCls(root_key)
        nodes_queue = [root]
        while cloned_nodes:
            parent_node = nodes_queue.pop(0)
            if parent_node:
                left_child_key = cloned_nodes.pop(0)
                right_child_key = cloned_nodes.pop(0) if cloned_nodes else None
                if left_child_key:
                    left_child_node = NodeCls(left_child_key)
                    parent_node.left = left_child_node
                    if hasattr(left_child_node, "parent"):
                        left_child_node.parent = parent_node
                    nodes_queue.append(parent_node.left)
                if right_child_key:
                    right_child_node = NodeCls(right_child_key)
                    parent_node.right = right_child_node
                    if hasattr(right_child_node, "parent"):
                        right_child_node.parent = parent_node
                    nodes_queue.append(parent_node.right)
        return root


class PreOrder(SerializeDeserialize):
    def serialize(tree: Optional[BinTreeNode]) -> List[Optional[int]]:
        def serialize_helper(
                node: Optional[BinTreeNode]) -> List[Optional[int]]:
            serialized_tree = []
            if not node:
                serialized_tree.append(None)
            else:
                serialized_tree.append(node.data)
                serialized_tree.extend(
                    serialize_helper(node.left))
                serialized_tree.extend(
                    serialize_helper(node.right))
            return serialized_tree
        if not tree:
            return []
        serialized_tree = serialize_helper(tree)
        while serialized_tree[-1] is None:
            serialized_tree.pop()
        return serialized_tree

    def deserialize(nodes: List[Optional[int]],
                    NodeCls: Type[BinTreeNode] = SimpleNode
                    ) -> Optional[BinTreeNode]:
        def deserialize_helper(
                nodes: List[Optional[int]],
                NodeCls: Type[BinTreeNode] = SimpleNode
                ) -> Optional[BinTreeNode]:
            if not nodes:
                return None
            node = None
            key = nodes.pop(0)
            if key:
                node = NodeCls(key)
                node.left = deserialize_helper(nodes)
                if hasattr(node.left, "parent"):
                    node.left.parent = node
                node.right = deserialize_helper(nodes)
                if hasattr(node.right, "parent"):
                    node.right.parent = node
            return node
        cloned_nodes = nodes[:]
        return deserialize_helper(cloned_nodes, NodeCls)


def find_node(node: Optional[BinTreeNode], key: int) -> Optional[BinTreeNode]:
    '''
    Find node with key in a binary tree
    '''
    if node is None:
        return None
    if node.data == key:
        return node
    found_node = find_node(node.left, key)
    if found_node:
        return found_node
    found_node = find_node(node.right, key)
    if found_node:
        return found_node
    return None


def generate_inorder(tree: BinTreeNode) -> List[int]:
    if tree is None:
        return []
    inorder = []
    inorder.extend(generate_inorder(tree.left))
    inorder.append(tree.data)
    inorder.extend(generate_inorder(tree.right))
    return inorder
