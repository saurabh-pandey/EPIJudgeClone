from typing import List

from test_framework import generic_test

from tests.test_intersect_sorted_arrays import TestIntersectSortedArrays


def intersect_two_sorted_arrays_v1(A: List[int], B: List[int]) -> List[int]:
    '''
    My version
    '''
    return []

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestIntersectSortedArrays(intersect_two_sorted_arrays_v1).run_tests()
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
