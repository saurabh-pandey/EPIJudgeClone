from typing import Optional

from binary_tree_node import BinaryTreeNode


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
