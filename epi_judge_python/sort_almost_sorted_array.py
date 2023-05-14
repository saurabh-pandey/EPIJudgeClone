import heapq

from typing import Iterator, List

from test_framework import generic_test
from tests.test_sort_almost_sorted_array import TestSortAlmostSortedArray


def sort_approximately_sorted_array_v1(sequence: Iterator[int],
                                       k: int) -> List[int]:
    '''
    My version with O(n) space and O(nlog(k)) runtime
    '''
    min_heap = []
    for _ in range(k + 1):
        value = next(sequence, None)
        if value is not None:
            heapq.heappush(min_heap, value)
        else:
            break
    result = []
    while min_heap:
        min_so_far = heapq.heappop(min_heap)
        result.append(min_so_far)
        value = next(sequence, None)
        if value is not None:
            heapq.heappush(min_heap, value)
    return result


def sort_approximately_sorted_array_v2(sequence: Iterator[int],
                                       k: int) -> List[int]:
    '''
    Program wise better version with similar runtime
    '''
    min_heap = []
    index = 0
    value = next(sequence, None)
    while value is not None and index < k:
        heapq.heappush(min_heap, value)
        value = next(sequence, None)
        index += 1
    result = []
    while value is not None:
        min_so_far = heapq.heappushpop(min_heap, value)
        result.append(min_so_far)
        value = next(sequence, None)
    while min_heap:
        min_so_far = heapq.heappop(min_heap)
        result.append(min_so_far)
    return result


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # return sort_approximately_sorted_array_v1(sequence, k)
    return sort_approximately_sorted_array_v2(sequence, k)


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    TestSortAlmostSortedArray(sort_approximately_sorted_array_v1).run_tests()
    TestSortAlmostSortedArray(sort_approximately_sorted_array_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
