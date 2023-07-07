from typing import List, Optional, Type, Union

from binary_tree_node import BinaryTreeNode
from bst_node import BstNode

TreeNode = Union[BstNode, BinaryTreeNode]


class Factory:
    '''
    Factory for some standard Binary Search Trees used in tests
    '''
    @staticmethod
    def single_node(cls: Type[TreeNode]) -> TreeNode:
        tree = cls(1)
        return tree
    
    @staticmethod
    def simple_even(cls: Type[TreeNode]) -> TreeNode:
        tree = cls(4,
            cls(2),
            cls(6),
        )
        return tree

    @staticmethod
    def left_leaning(cls: Type[TreeNode]) -> TreeNode:
        tree = cls(2,
            cls(1)
        )
        return tree
    
    @staticmethod
    def right_leaning(cls: Type[TreeNode]) -> TreeNode:
        tree = cls(2,
            None,
            cls(3)
        )
        return tree

    @staticmethod
    def three_layered(cls: Type[TreeNode]) -> TreeNode:
        tree = cls(4,
            cls(2,
                cls(1),
                cls(3)
            ),
            cls(6,
                cls(5),
                cls(7)
            ),
        )
        return tree


def find_node(tree: Optional[BstNode], key: int) -> Optional[BstNode]:
    '''
    Find node with key in a binary search tree
    '''
    node = tree
    while node:
        if node.data == key:
            return node
        elif key < node.data:
            node = node.left
        else:
            node = node.right
    return None

def generate_preorder(tree: Optional[BstNode], key: int) -> List[int]:
    preorder_traversal = []
    if tree:
        preorder_traversal.extend(generate_preorder(tree.left))
        preorder_traversal.append(tree.data)
        preorder_traversal.extend(generate_preorder(tree.right))
    return preorder_traversal
