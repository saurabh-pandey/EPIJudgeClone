import sys
import heapq

from typing import List

from test_framework import generic_test
from tests.test_sorted_arrays_merge import TestSortedArraysMerge


def merge_sorted_arrays_v1(sorted_arrays: List[List[int]]) -> List[int]:
    '''
    Simple O(nk) version
    '''
    total_len = sum([len(arr) for arr in sorted_arrays])
    result = [0 for _ in range(total_len)]
    running_arr_indices = [0 for _ in sorted_arrays]
    index = 0
    while index < total_len:
        min_val = sys.maxsize
        arr_index = 0
        for i, arr in enumerate(sorted_arrays):
            curr_arr_index = running_arr_indices[i]
            if curr_arr_index < len(arr):
                curr_value = arr[curr_arr_index]
                if curr_value < min_val:
                    min_val = curr_value
                    arr_index = i
        result[index] = min_val
        index += 1
        running_arr_indices[arr_index] += 1
    return result


def merge_sorted_arrays_v2(sorted_arrays: List[List[int]]) -> List[int]:
    '''
    Version using min heaps with runtime of O(nlog(k)) where k is number of 
    sorted arrays
    '''
    total_len = sum([len(arr) for arr in sorted_arrays])
    result = [0] * total_len
    index = 0
    h = [(arr[0], 0, i) for i, arr in enumerate(sorted_arrays)]
    heapq.heapify(h)
    while index < total_len:
        min_val, i, arr_i = heapq.heappop(h)
        result[index] = min_val
        index += 1
        sorted_arr = sorted_arrays[arr_i]
        if i + 1 < len(sorted_arr):
            heapq.heappush(h, (sorted_arr[i + 1], i + 1, arr_i))
    return result


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # return merge_sorted_arrays_v1(sorted_arrays)
    return merge_sorted_arrays_v2(sorted_arrays)


if __name__ == '__main__':
    TestSortedArraysMerge(merge_sorted_arrays_v1).run_tests()
    TestSortedArraysMerge(merge_sorted_arrays_v2).run_tests()
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
