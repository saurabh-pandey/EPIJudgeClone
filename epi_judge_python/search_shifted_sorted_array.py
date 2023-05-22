from typing import List

from test_framework import generic_test

from tests.test_search_shifted_sorted_array import TestSearchShiftedSortedArray


def search_smallest_v1(A: List[int]) -> int:
    '''
    My version with O(log(n)) runtime
    '''
    begin, end = 0, len(A) - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if A[mid] < A[end]:
            end = mid
        elif A[mid] >= A[begin]:
            begin = mid + 1
    return begin


def search_smallest_v2(A: List[int]) -> int:
    '''
    Book's version
    '''
    begin, end = 0, len(A) - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if A[mid] > A[end]:
            begin = mid + 1
        else:
            end = mid
    return begin


def search_smallest(A: List[int]) -> int:
    # return search_smallest_v1(A)
    return search_smallest_v2(A)


if __name__ == '__main__':
    TestSearchShiftedSortedArray(search_smallest_v1).run_tests()
    TestSearchShiftedSortedArray(search_smallest_v2).run_tests()
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
