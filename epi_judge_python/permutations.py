from typing import List

from test_framework import generic_test, test_utils

from tests.test_permutations import TestPermutations


def permutations_v1(A: List[int]) -> List[List[int]]:
    '''
    My version
    '''
    return []


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    TestPermutations(permutations_v1).run_tests()
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
