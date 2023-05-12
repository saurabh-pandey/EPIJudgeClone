from typing import List

from test_framework import generic_test
from tests.test_sort_increasing_decreasing_array import (
    TestSortIncreasingDecreasingArray)


def sort_k_increasing_decreasing_array_v1(A: List[int]) -> List[int]:
    '''
    My version
    '''
    return []

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestSortIncreasingDecreasingArray(
        sort_k_increasing_decreasing_array_v1).run_tests()
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
