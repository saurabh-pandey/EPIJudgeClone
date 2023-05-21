import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_search_entry_equal_to_index import TestSearchEntryEqualToIndex


def search_entry_equal_to_its_index_v1(A: List[int]) -> int:
    '''
    My O(log(n)) version
    '''
    begin, end = 0, len(A) - 1
    while begin <= end:
        mid = begin + (end - begin)//2
        if mid < A[mid]:
            end = mid - 1
        elif mid == A[mid]:
            return mid
        else:
            begin = mid + 1
    return -1

def search_entry_equal_to_its_index(A: List[int]) -> int:
    return search_entry_equal_to_its_index_v1(A)


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    TestSearchEntryEqualToIndex(search_entry_equal_to_its_index_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
