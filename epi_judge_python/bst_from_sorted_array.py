import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_bst_from_sorted_array import TestBstFromSortedArray


def build_min_height_bst_from_sorted_array_v1(
        A: List[int]) -> Optional[BstNode]:
    '''
    My version with O(n) time and O(log(n)) space complexity
    '''
    if not A:
        return None
    else:
        mid = len(A) // 2
        return BstNode(A[mid],
                       build_min_height_bst_from_sorted_array_v1(A[:mid]),
                       build_min_height_bst_from_sorted_array_v1(A[mid + 1:]))


def build_min_height_bst_from_sorted_array_v2(
        A: List[int]) -> Optional[BstNode]:
    '''
    Book's version with same complexity
    '''
    def build_min_height_bst_rec(start: int, finish: int) -> Optional[BstNode]:
        if start == finish:
            return None
        else:
            mid = (start + finish) // 2
            return BstNode(A[mid],
                           build_min_height_bst_rec(start, mid),
                           build_min_height_bst_rec(mid + 1, finish))
    return build_min_height_bst_rec(0, len(A))

def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    # return build_min_height_bst_from_sorted_array_v1(A)
    return build_min_height_bst_from_sorted_array_v2(A)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    TestBstFromSortedArray(
        build_min_height_bst_from_sorted_array_v1).run_tests()
    TestBstFromSortedArray(
        build_min_height_bst_from_sorted_array_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
