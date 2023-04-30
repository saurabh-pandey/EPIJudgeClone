from typing import List, Optional

from binary_tree_node import BinaryTreeNode

def deserialize_level_order(
        nodes: List[Optional[int]]) -> Optional[BinaryTreeNode]:
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
                parent_node.left = BinaryTreeNode(left_child_key)
                nodes_queue.append(parent_node.left)
            if right_child_key:
                parent_node.right = BinaryTreeNode(right_child_key)
                nodes_queue.append(parent_node.right)
    return root

def serialize_level_order(
        tree: Optional[BinaryTreeNode]) -> List[Optional[int]]:
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
