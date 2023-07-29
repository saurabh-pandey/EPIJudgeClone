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


def permutations_v2(A: List[int]) -> List[List[int]]:
    '''
    Book's version
    '''
    def permutations_recursive(i: int) -> None:
        if i == len(A) - 1:
            permutations.append(A[:])
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            permutations_recursive(i + 1)
            A[i], A[j] = A[j], A[i]
    permutations = []
    permutations_recursive(0)
    return permutations


def permutations_v3(A: List[int]) -> List[List[int]]:
    '''
    Another Book's version with my version of next permutation
    '''
    def next_permutation() -> List[int]:
        pivot_index = -1
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                pivot_index = i
        if pivot_index == -1:
            return []
        next_bigger_index = len(A) - 1
        for i in range(len(A) - 1, pivot_index, -1):
            if A[i] > A[pivot_index]:
                next_bigger_index = i
                break
        A[pivot_index], A[next_bigger_index] = A[next_bigger_index], A[pivot_index]
        # The array beyond pivot is sorted in descending so just swap to sort in
        # ascending
        i = pivot_index + 1
        j = len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
    permutations = []
    while True:
        permutations.append(A[:])
        A = next_permutation()
        if not A:
            break
    return permutations


def permutations_v4(A: List[int]) -> List[List[int]]:
    '''
    Complete Book's version
    '''
    def next_permutation() -> List[int]:
        inversion_point = len(A) - 2
        while (inversion_point >= 0
               and A[inversion_point] >= A[inversion_point + 1]):
            inversion_point -= 1
        if inversion_point == -1:
            return []
        for i in reversed(range(inversion_point + 1, len(A))):
            if A[i] > A[inversion_point]:
                A[inversion_point], A[i] = A[i], A[inversion_point]
                break
        A[inversion_point + 1:] = reversed(A[inversion_point + 1:])
        return A

    permutations = []
    while True:
        permutations.append(A[:])
        A = next_permutation()
        if not A:
            break
    return permutations


def permutations(A: List[int]) -> List[List[int]]:
    # return permutations_v1(A)
    # return permutations_v2(A)
    # return permutations_v3(A)
    return permutations_v4(A)

if __name__ == '__main__':
    TestPermutations(permutations_v1).run_tests()
    TestPermutations(permutations_v2).run_tests()
    TestPermutations(permutations_v3).run_tests()
    TestPermutations(permutations_v4).run_tests()
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
