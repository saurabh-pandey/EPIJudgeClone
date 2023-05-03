from abc import ABC, abstractmethod
from typing import List, Optional

from binary_tree_node import BinaryTreeNode


class SerializeDeserialize(ABC):
    @abstractmethod
    def serialize(tree: Optional[BinaryTreeNode]) -> List[Optional[int]]:
        pass

    @abstractmethod
    def deserialize(nodes: List[Optional[int]]) -> Optional[BinaryTreeNode]:
        pass


class LevelOrder(SerializeDeserialize):
    def serialize(tree: Optional[BinaryTreeNode]) -> List[Optional[int]]:
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
    
    def deserialize( nodes: List[Optional[int]]) -> Optional[BinaryTreeNode]:
        if not nodes:
            return None
        cloned_nodes = nodes[:]
        root_key = None
        while root_key is None:
            root_key = cloned_nodes.pop(0)
        root = BinaryTreeNode(root_key)
        nodes_queue = [root]
        while cloned_nodes:
            parent_node = nodes_queue.pop(0)
            if parent_node:
                left_child_key = cloned_nodes.pop(0)
                right_child_key = cloned_nodes.pop(0) if cloned_nodes else None
                if left_child_key:
                    left_child_node = BinaryTreeNode(left_child_key)
                    parent_node.left = left_child_node
                    if hasattr(left_child_node, "parent"):
                        left_child_node.parent = parent_node
                    nodes_queue.append(parent_node.left)
                if right_child_key:
                    right_child_node = BinaryTreeNode(right_child_key)
                    parent_node.right = right_child_node
                    if hasattr(right_child_node, "parent"):
                        right_child_node.parent = parent_node
                    nodes_queue.append(parent_node.right)
        return root


class PreOrder(SerializeDeserialize):
    def serialize(tree: Optional[BinaryTreeNode]) -> List[Optional[int]]:
        def serialize_helper(
                node: Optional[BinaryTreeNode]) -> List[Optional[int]]:
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

    def deserialize(nodes: List[Optional[int]]) -> Optional[BinaryTreeNode]:
        def deserialize_helper(
                nodes: List[Optional[int]]) -> Optional[BinaryTreeNode]:
            if not nodes:
                return None
            node = None
            key = nodes.pop(0)
            if key:
                node = BinaryTreeNode(key)
                node.left = deserialize_helper(nodes)
                if hasattr(node.left, "parent"):
                    node.left.parent = node
                node.right = deserialize_helper(nodes)
                if hasattr(node.right, "parent"):
                    node.right.parent = node
            return node
        cloned_nodes = nodes[:]
        return deserialize_helper(cloned_nodes)


def find_node(node: BinaryTreeNode, key: int) -> Optional[BinaryTreeNode]:
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
