from typing import Optional, Tuple

from binary_tree_node import BinaryTreeNode

from test_framework import generic_test
from tests.test_is_tree_a_bst import TestIsTreeBst


def is_binary_tree_bst_v1(tree: BinaryTreeNode) -> bool:
    '''
    My version with O(n) time and O(h) space complexity
    '''
    def check_bst_property(
                node: Optional[BinaryTreeNode]
            ) -> Tuple[bool, Optional[int], Optional[int]]:
        if node is None:
            return (True, None, None)
        is_left_tree_bst, min_left, max_left = check_bst_property(node.left)
        if not is_left_tree_bst:
            return (False, None, None)
        is_right_tree_bst, min_right, max_right = check_bst_property(node.right)
        if not is_right_tree_bst:
            return (False, None, None)
        if max_left is not None and node.data < max_left:
            return (False, None, None)
        if min_right is not None and node.data > min_right:
            return (False, None, None)
        min_val = min_left if min_left is not None else node.data
        max_val = max_right if max_right is not None else node.data
        return (True, min_val, max_val)
    return check_bst_property(tree)[0]


def is_binary_tree_bst_v2(tree: BinaryTreeNode) -> bool:
    '''
    Using the fact that inorder traversal of a BST is always a sorted array.
    '''
    def inorder_traversal(
                node: Optional[BinaryTreeNode],
                prev: Optional[BinaryTreeNode]
            ) -> Tuple[bool, Optional[BinaryTreeNode]] :
        if node:
            is_left_tree_bst, last_left_node = inorder_traversal(node.left, 
                                                                 prev)
            if not is_left_tree_bst:
                return (False, None)
            if last_left_node and last_left_node.data > node.data:
                return (False, None)
            is_right_tree_bst, last_right_node = inorder_traversal(node.right,
                                                                   node)
            if not is_right_tree_bst:
                return (False, None)
            return (True, last_right_node or node)
        return (True, prev)
    return inorder_traversal(tree, None)[0]


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # return is_binary_tree_bst_v1(tree)
    return is_binary_tree_bst_v2(tree)


if __name__ == '__main__':
    TestIsTreeBst(is_binary_tree_bst_v1).run_tests()
    TestIsTreeBst(is_binary_tree_bst_v2).run_tests()
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py',
                                       'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
