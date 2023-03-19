import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from tests.test_even_odd_array import TestEvenOddArray


def even_odd_v1(A: List[int]) -> None:
    '''
    My O(n) time and O(1) space implementation
    '''
    even_index = 0
    i = 0
    sz = len(A)
    while i < sz:
        if A[i] % 2 == 1:
            break
        i += 1
    even_index = i
    while i < sz:
        if A[i] % 2 == 0:
            temp = A[even_index]
            A[even_index] = A[i]
            A[i] = temp
            even_index += 1
        i += 1


def even_odd(A: List[int]) -> None:
    even_odd_v1(A)
    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    TestEvenOddArray(even_odd_v1).run_tests()
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
