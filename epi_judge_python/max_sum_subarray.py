import sys

from typing import List

from test_framework import generic_test

from tests.test_max_sum_subarray import TestMaxSumSubarray


def find_maximum_subarray_v1(A: List[int]) -> int:
    '''
    Brute-force version
    '''
    max_sum = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray_sum = sum(A[i:j + 1])
            if subarray_sum > max_sum:
                max_sum = subarray_sum
    return max_sum


def find_maximum_subarray(A: List[int]) -> int:
    return find_maximum_subarray_v1(A)


if __name__ == '__main__':
    TestMaxSumSubarray(find_maximum_subarray_v1).run_tests()
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
