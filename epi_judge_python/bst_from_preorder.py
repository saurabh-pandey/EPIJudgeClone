from typing import List, Optional

from bst_node import BstNode

from test_framework import generic_test

from tests.test_bst_from_preorder import TestBstFromPreorder


def rebuild_bst_from_preorder_v1(
        preorder_sequence: List[int]) -> Optional[BstNode]:
    '''
    My version with O(n) time and O(log(n)) space
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


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    return rebuild_bst_from_preorder_v1(preorder_sequence)


if __name__ == '__main__':
    TestBstFromPreorder(rebuild_bst_from_preorder_v1).run_tests()
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
