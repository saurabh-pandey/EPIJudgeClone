from typing import List

from test_framework import generic_test

from tests.test_search_first_key import TestSearchFirstKey


def search_first_of_k_v1(A: List[int], k: int) -> int:
    '''
    My version of O(log(n)) time and O(1) space complexity
    '''
    begin, end = 0, len(A) - 1
    result = len(A)
    while begin <= end:
        mid = begin + (end - begin)//2
        if k < A[mid]:
            end = mid - 1
        elif k == A[mid]:
            result = mid if mid < result else result
            end = mid - 1
        else:
            begin = mid + 1
    return result if result < len(A) else -1


def search_first_of_k_v2(A: List[int], k:int) -> int:
    '''
    Book inspired version with same runtime and space complexity
    '''
    begin, end = 0, len(A) - 1
    result = -1
    while begin <= end:
        mid = begin + (end - begin)//2
        if k < A[mid]:
            end = mid - 1
        elif k == A[mid]:
            result = mid
            end = mid - 1
        else:
            begin = mid + 1
    return result


def search_first_of_k(A: List[int], k: int) -> int:
    # return search_first_of_k_v1(A, k)
    return search_first_of_k_v2(A, k)


if __name__ == '__main__':
    TestSearchFirstKey(search_first_of_k_v1).run_tests()
    TestSearchFirstKey(search_first_of_k_v2).run_tests()
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
