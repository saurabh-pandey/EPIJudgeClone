import sys

from typing import List, Optional

from bst_node import BstNode

from test_framework import generic_test

from tests.test_bst_from_preorder import TestBstFromPreorder


def rebuild_bst_from_preorder_v1(
        preorder_sequence: List[int]) -> Optional[BstNode]:
    '''
    My version with O(n^2) time and O(log(n)) space
    '''
    if not preorder_sequence:
        return None
    node = BstNode(preorder_sequence[0])
    left_subarr_end = 1
    while (left_subarr_end < len(preorder_sequence)
           and preorder_sequence[left_subarr_end] < preorder_sequence[0]):
        left_subarr_end += 1
    node.left = rebuild_bst_from_preorder_v1(
                    preorder_sequence[1:left_subarr_end])
    node.right = rebuild_bst_from_preorder_v1(
                    preorder_sequence[left_subarr_end:])
    return node


def rebuild_bst_from_preorder_v2(
        preorder_sequence: List[int]) -> Optional[BstNode]:
    '''
    Book's recursive version with same constants
    '''
    if not preorder_sequence:
        return None
    left_subarr_end = 1
    while (left_subarr_end < len(preorder_sequence)
           and preorder_sequence[left_subarr_end] < preorder_sequence[0]):
        left_subarr_end += 1
    return BstNode(preorder_sequence[0],
                   rebuild_bst_from_preorder_v2(
                        preorder_sequence[1:left_subarr_end]),
                   rebuild_bst_from_preorder_v2(
                        preorder_sequence[left_subarr_end:]))


def rebuild_bst_from_preorder_v3(
        preorder_sequence: List[int]) -> Optional[BstNode]:
    '''
    Book's O(n) time version
    '''
    def rebuild_bst_from_preorder_with_bounds(
            lower_bound: int, upper_bound: int) -> Optional[BstNode]:
        if root_idx[0] >= len(preorder_sequence):
            return None
        root = preorder_sequence[root_idx[0]]
        if root < lower_bound or root > upper_bound:
            return None
        root_idx[0] += 1
        left_subtree = rebuild_bst_from_preorder_with_bounds(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_with_bounds(root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)    
    root_idx = [0]
    return rebuild_bst_from_preorder_with_bounds(-sys.maxsize, sys.maxsize)


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # return rebuild_bst_from_preorder_v1(preorder_sequence)
    # return rebuild_bst_from_preorder_v2(preorder_sequence)
    return rebuild_bst_from_preorder_v3(preorder_sequence)


if __name__ == '__main__':
    TestBstFromPreorder(rebuild_bst_from_preorder_v1).run_tests()
    TestBstFromPreorder(rebuild_bst_from_preorder_v2).run_tests()
    TestBstFromPreorder(rebuild_bst_from_preorder_v3).run_tests()
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
