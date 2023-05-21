from typing import List

from test_framework import generic_test

from tests.test_search_shifted_sorted_array import TestSearchShiftedSortedArray


def search_smallest_v1(A: List[int]) -> int:
    '''
    My version
    '''
    return 0


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestSearchShiftedSortedArray(search_smallest_v1).run_tests()
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
