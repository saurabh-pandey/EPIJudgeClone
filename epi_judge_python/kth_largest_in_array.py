from typing import List

from test_framework import generic_test

from tests.test_kth_largest_in_array import TestKthLargestInArray


def find_kth_largest_v1(k: int, A: List[int]) -> int:
    return 0


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestKthLargestInArray(find_kth_largest_v1).run_tests()
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
