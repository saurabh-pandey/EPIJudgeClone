import sys

from typing import List

from test_framework import generic_test

from tests.test_max_sum_subarray import TestMaxSumSubarray


def find_maximum_subarray_v1(A: List[int]) -> int:
    '''
    Brute-force version with O(n^3) time
    '''
    max_sum = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray_sum = sum(A[i:j + 1])
            if subarray_sum > max_sum:
                max_sum = subarray_sum
    return max_sum


def find_maximum_subarray_v2(A: List[int]) -> int:
    '''
    O(n^2) version with O(n) space
    '''
    max_sum = 0
    sum_array = [0 for _ in range(len(A) + 1)]
    for i, a in enumerate(A):
        sum_array[i + 1] = sum_array[i] + a
    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray_sum = sum_array[j + 1] - sum_array[i]
            if subarray_sum > max_sum:
                max_sum = subarray_sum
    return max_sum


def find_maximum_subarray_v3(A: List[int]) -> int:
    '''
    O(n*log(n)) version using divide and conquer
    '''
    def maximum_subarray_recursive(subarray: List[int]) -> int:
        if len(subarray) == 0:
            return 0
        elif len(subarray) == 1:
            if subarray[0] < 1:
                return 0
        max_left = maximum_subarray_recursive(subarray[: len(subarray) // 2])
        max_right = maximum_subarray_recursive(subarray[len(subarray) // 2 :])
        # TODO: Merge here
        max_merge = 0
        return max(max_left, max_right, max_merge)
    return maximum_subarray_recursive(A)



def find_maximum_subarray(A: List[int]) -> int:
    # return find_maximum_subarray_v1(A)
    return find_maximum_subarray_v2(A)


if __name__ == '__main__':
    TestMaxSumSubarray(find_maximum_subarray_v1).run_tests()
    TestMaxSumSubarray(find_maximum_subarray_v2).run_tests()
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
