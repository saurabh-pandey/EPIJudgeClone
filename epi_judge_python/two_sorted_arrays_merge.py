from typing import List

from test_framework import generic_test

from tests.test_two_sorted_arrays_merge import TestTwoSortedArraysMerge


def merge_two_sorted_arrays_v1(A: List[int],
                               m: int,
                               B: List[int],
                               n: int) -> None:
    '''
    My version
    '''
    return


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    TestTwoSortedArraysMerge(merge_two_sorted_arrays_v1).run_tests()
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
