import operator
import random

from typing import Callable, List

from test_framework import generic_test

from tests.test_kth_largest_in_array import TestKthLargestInArray


def find_kth_largest_v1(k: int, A: List[int]) -> int:
    '''
    My version with O(n) time and O(log(n)) space complexity
    '''
    def find_kth(A: List[int], begin: int, end: int, k: int) -> int:
        i, j = begin, end
        pivot = random.randint(begin, end)
        A[begin], A[pivot] = A[pivot], A[begin]
        while i < j:
            if A[i + 1] > A[i]:
                A[i], A[i + 1] = A[i + 1], A[i]
                i += 1
            else:
                A[i + 1], A[j] = A[j], A[i + 1]
                j -= 1
        if k == i + 1:
            return A[i]
        elif k < i + 1:
            return find_kth(A, begin, i - 1, k)
        else:
            return find_kth(A, i + 1, end, k)
    return find_kth(A, 0, len(A) - 1, k)


def find_kth_largest_v2(k: int, A: List[int]) -> int:
    '''
    Book's version with O(n) time and O(1) space complexity
    '''
    def find_kth(comparator: Callable[[int, int], bool]) -> int:
        def partition_around_pivot(A: List[int],
                                   begin: int,
                                   end: int,
                                   pivot_index: int) -> int:
            pivot_value = A[pivot_index]
            new_pivot_index = begin
            A[pivot_index], A[end] = A[end], A[pivot_index]
            for i in range(begin, end):
                if comparator(A[i], pivot_value):
                    A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
                    new_pivot_index += 1
            A[new_pivot_index], A[end] = A[end], A[new_pivot_index]
            return new_pivot_index
        begin, end = 0, len(A) - 1
        while begin <= end:
            pivot = random.randint(begin, end)
            new_pivot_index = partition_around_pivot(A, begin, end, pivot)
            if new_pivot_index == k - 1:
                return A[new_pivot_index]
            elif new_pivot_index > k - 1:
                end = new_pivot_index - 1
            else:
                begin = new_pivot_index + 1
    return find_kth(operator.gt)


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # return find_kth_largest_v1(k, A)
    return find_kth_largest_v2(k, A)


if __name__ == '__main__':
    TestKthLargestInArray(find_kth_largest_v1).run_tests()
    TestKthLargestInArray(find_kth_largest_v2).run_tests()
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
