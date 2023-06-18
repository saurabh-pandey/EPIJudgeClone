from typing import List

from test_framework import generic_test

from tests.test_two_sorted_arrays_merge import TestTwoSortedArraysMerge


def merge_two_sorted_arrays_v1(A: List[int],
                               m: int,
                               B: List[int],
                               n: int) -> None:
    '''
    My version with O(m + n) time and O(1) space
    '''
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0 and k >= 0:
        if A[i] >= B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while i >= 0 and k >= 0:
        A[k] = A[i]
        i -= 1
        k -= 1
    while j >= 0 and k >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    merge_two_sorted_arrays_v1(A, m, B, n)


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    TestTwoSortedArraysMerge(merge_two_sorted_arrays_v1).run_tests()
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
