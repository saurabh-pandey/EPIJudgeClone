from typing import List

from test_framework import generic_test

from tests.test_search_first_key import TestSearchFirstKey


def search_first_of_k_v1(A: List[int], k: int) -> int:
    '''
    My version of O(log(n)) time and O(1) space complexity
    '''
    return 0


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestSearchFirstKey(search_first_of_k_v1).run_tests()
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
