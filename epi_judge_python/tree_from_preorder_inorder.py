from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from tests.test_tree_from_preorder_inorder import TestTreeFromPreorderInorder

def binary_tree_from_preorder_inorder_v1(
        preorder: List[int],
        inorder: List[int]
        ) -> Optional[BinaryTreeNode]:
    '''
    My O(n^2) version
    '''
    if not preorder:
        return None
    # This one takes O(n) time
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


def binary_tree_from_preorder_inorder_v2(
        preorder: List[int],
        inorder: List[int]
        ) -> Optional[BinaryTreeNode]:
    '''
    Book's O(n) version
    '''
    node_to_index = {data: i for i, data in enumerate(inorder)}
    def construct_tree(preorder_start: int,
                       preorder_end: int,
                       inorder_start: int,
                       inorder_end: int) -> Optional[BinaryTreeNode]:
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        root = BinaryTreeNode(preorder[preorder_start])
        partition_index = node_to_index[preorder[preorder_start]]
        left_subtree_sz = partition_index - inorder_start
        root.left = construct_tree(preorder_start + 1,
                                   preorder_start + left_subtree_sz + 1,
                                   inorder_start,
                                   partition_index)
        root.right = construct_tree(preorder_start + left_subtree_sz + 1,
                                    preorder_end,
                                    partition_index + 1,
                                    inorder_end)
        return root
    return construct_tree(0, len(preorder), 0, len(inorder))


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # return binary_tree_from_preorder_inorder_v1(preorder, inorder)
    return binary_tree_from_preorder_inorder_v2(preorder, inorder)


if __name__ == '__main__':
    TestTreeFromPreorderInorder(
        binary_tree_from_preorder_inorder_v1).run_tests()
    TestTreeFromPreorderInorder(
        binary_tree_from_preorder_inorder_v2).run_tests()
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
