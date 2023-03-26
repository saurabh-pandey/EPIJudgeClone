import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from tests.test_sorted_array_remove_dups import TestSortedArrayRemoveDups


def delete_duplicates_v1(A: List[int]) -> int:
    '''
    O(n) time and O(1) space
    '''
    sz = len(A)
    unique_index = 0
    for read_index in range(sz):
        if A[unique_index] != A[read_index]:
            unique_index += 1
            A[unique_index] = A[read_index]
        read_index += 1
    return unique_index + 1

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    return delete_duplicates_v1(A)


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    TestSortedArrayRemoveDups(delete_duplicates_v1).run_tests()
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
