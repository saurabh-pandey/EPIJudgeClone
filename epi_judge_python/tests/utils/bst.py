from typing import Type, Union

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
