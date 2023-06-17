import bisect

from typing import List

from test_framework import generic_test

from tests.test_intersect_sorted_arrays import TestIntersectSortedArrays


def intersect_two_sorted_arrays_v1(A: List[int], B: List[int]) -> List[int]:
    '''
    My version with O(nlog(m)) runtime where n is size of smaller array and m is
    size of bigger array
    '''
    smaller, bigger = A, B
    if len(smaller) > len(bigger):
        smaller, bigger = bigger, smaller
    result = []
    unique = set()
    for s in smaller:
        if s in unique or s < bigger[0] or s > bigger[-1]:
            continue
        else:
            index = bisect.bisect_left(bigger, s)
            if bigger[index] == s:
                result.append(s)
                unique.add(s)
    return result


def intersect_two_sorted_arrays_v2(A: List[int], B: List[int]) -> List[int]:
    '''
    Better version with O(m + n) runtime
    '''
    intersection = []
    i = 0
    j = 0
    k = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            if k == 0 or intersection[k - 1] != A[i]:
                intersection.append(A[i])
                k += 1
            i += 1
            j += 1
        else:
            j += 1
    return intersection


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # return intersect_two_sorted_arrays_v1(A, B)
    return intersect_two_sorted_arrays_v2(A, B)


if __name__ == '__main__':
    TestIntersectSortedArrays(intersect_two_sorted_arrays_v1).run_tests()
    TestIntersectSortedArrays(intersect_two_sorted_arrays_v2).run_tests()
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
