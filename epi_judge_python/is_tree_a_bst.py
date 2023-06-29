from typing import Optional

from binary_tree_node import BinaryTreeNode

from test_framework import generic_test
from tests.test_is_tree_a_bst import TestIsTreeBst


def is_binary_tree_bst_v1(tree: BinaryTreeNode) -> bool:
    '''
    My version with O(n) time and O(h) space complexity
    '''
    def check_bst_property(node: Optional[BinaryTreeNode],
                           parent: Optional[BinaryTreeNode]) -> bool:
        if not node:
            return True
        if node.left and node.data < node.left.data:
            return False
        if node.right and node.data > node.right.data:
            return False
        if parent:
            if parent.left is node:
                if node.right and parent.data < node.right.data:
                    return False
            else:
                if node.left and parent.data > node.left.data:
                    return False
        return (check_bst_property(node.left, node)
            and check_bst_property(node.right, node))
    return check_bst_property(tree, None)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_binary_tree_bst_v1(tree)


if __name__ == '__main__':
    TestIsTreeBst(is_binary_tree_bst_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
