import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_dutch_national_flag import TestDutchNationalFlag


RED, WHITE, BLUE = range(3)

def dutch_flag_partition_v1(pivot_index: int, A: List[int]) -> None:
    '''
    My O(n) time and O(1) space version
    '''
    sz = len(A)
    pivot = A[pivot_index]
    next_less = 0
    for i in range(sz):
        if A[i] < pivot:
            A[next_less], A[i] = A[i], A[next_less]
            next_less += 1
    next_greater = sz - 1
    for i in reversed(range(sz)):
        if A[i] > pivot:
            A[next_greater], A[i] = A[i], A[next_greater]
            next_greater -= 1

def dutch_flag_partition_v2(pivot_index: int, A: List[int]) -> None:
    '''
    Book's single pass O(n) time and O(1) space version
    '''
    sz = len(A)
    pivot = A[pivot_index]
    next_less = 0
    next_greater = sz - 1
    i = 0
    while i <= next_greater:
        if A[i] < pivot:
            A[next_less], A[i] = A[i], A[next_less]
            next_less += 1
            i += 1
        elif A[i] == pivot:
            i += 1
        else:
            A[next_greater], A[i] = A[i], A[next_greater]
            next_greater -= 1


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # dutch_flag_partition_v1(pivot_index, A)
    dutch_flag_partition_v2(pivot_index, A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    TestDutchNationalFlag(dutch_flag_partition_v1).run_tests()
    TestDutchNationalFlag(dutch_flag_partition_v2).run_tests()
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
