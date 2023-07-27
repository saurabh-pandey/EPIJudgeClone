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
    Another Book's version
    '''
    def next_permutation() -> List[int]:
        '''
        Idea is to see A and find the smallest bigger number that can be formed
        by just rearranging. If A is already in descending order then we have to
        return empty list. This will mark the end of search.
        General idea to find the next bigger permutation is to find the 
        furthest point where a subsequent bigger number can be used. Once that
        bigger number is placed in that place everything later is to be in
        ascending order.
        An algorithm that might do the trick is as follows:
        1. Find the furthest number whose next number is bigger. Call it pivot.
        2. Next replace this pivot with the next bigger subsequent number.
        3. Now everything next to pivot should be arranged in ascending order.
        4. Above sorting can be simplified as the smallest number is the pivot.
        5. Everything else after pivot has to be in descending order to begin 
        with otherwise the choice of pivot is wrong.
        6. Thus ascending order is pivot followed by last number and then 
        progressing in reverse until reaching next to the pivot point.

        If all the numbers are in descending order then we won't be able to 
        find the pivot element. This means we fail at step 1 of the above algo. 
        In such a situation we return empty list.
        '''
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
        A[pivot_index + 1:] = sorted(A[pivot_index + 1:])
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
    return permutations_v3(A)

if __name__ == '__main__':
    TestPermutations(permutations_v1).run_tests()
    TestPermutations(permutations_v2).run_tests()
    TestPermutations(permutations_v3).run_tests()
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
