from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from tests.test_tree_from_preorder_inorder import TestTreeFromPreorderInorder

def binary_tree_from_preorder_inorder_v1(
        preorder: List[int],
        inorder: List[int]
        ) -> Optional[BinaryTreeNode]:
    '''
    My O(n) version
    '''
    if not preorder:
        return None
    partition_index = inorder.index(preorder[0])
    root = BinaryTreeNode(preorder[0])
    root.left = binary_tree_from_preorder_inorder_v1(
        preorder[1: partition_index + 1],
        inorder[:partition_index]
    )
    root.right = binary_tree_from_preorder_inorder_v1(
        preorder[partition_index + 1:],
        inorder[partition_index + 1:]
    )
    return root


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    return binary_tree_from_preorder_inorder_v1(preorder, inorder)


if __name__ == '__main__':
    TestTreeFromPreorderInorder(
        binary_tree_from_preorder_inorder_v1).run_tests()
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
