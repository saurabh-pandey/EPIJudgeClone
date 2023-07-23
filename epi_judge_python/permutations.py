from typing import List

from test_framework import generic_test, test_utils

from tests.test_permutations import TestPermutations


def permutations_v1(A: List[int]) -> List[List[int]]:
    '''
    My version
    '''
    def permutations_recursive(count: int) -> None:
        if count == len(A):
            permutations.append(permutation[:])
            return
        for i, a in enumerate(A):
            if i not in looked_indices:
                looked_indices.add(i)
                permutation[count] = a
                permutations_recursive(count + 1)
                looked_indices.remove(i)
                permutation[count] = 0
    permutations = []
    permutation = [0] * len(A)
    looked_indices = set()
    permutations_recursive(0)
    return permutations


def permutations(A: List[int]) -> List[List[int]]:
    return permutations_v1(A)


if __name__ == '__main__':
    TestPermutations(permutations_v1).run_tests()
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
