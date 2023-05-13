import heapq

from typing import List

from test_framework import generic_test
from tests.test_sort_increasing_decreasing_array import (
    TestSortIncreasingDecreasingArray)


def sort_k_increasing_decreasing_array_v1(A: List[int]) -> List[int]:
    '''
    My version with O(nlog(k)) runtime
    '''
    if not A:
        return []
    if len(A) == 1:
        return A[:]
    array_bounds = {
        "inc": [],
        "dec": []
    }
    is_increasing = A[0] <= A[1]
    if is_increasing:
        array_bounds["inc"].append(0)
    else:
        array_bounds["dec"].append(0)
    for i in range(len(A) - 1):
        if is_increasing and A[i] > A[i + 1]:
            is_increasing = False
            array_bounds["inc"].append(i)
            array_bounds["dec"].append(i + 1)
        elif not is_increasing and A[i] <= A[i + 1]:
            is_increasing = True
            array_bounds["dec"].append(i)
            array_bounds["inc"].append(i + 1)
    if is_increasing:
        array_bounds["inc"].append(len(A) - 1)
    else:
        array_bounds["dec"].append(len(A) - 1)
    result = []
    min_heap = []
    for i in range(0, len(array_bounds["inc"]), 2):
        index = array_bounds["inc"][i]
        heapq.heappush(min_heap, (A[index], "inc", i, index))
    for i in range(1, len(array_bounds["dec"]), 2):
        index = array_bounds["dec"][i]
        heapq.heappush(min_heap,
                       (A[index], "dec", i, index))
    while min_heap:
        valve, arr_type, arr_index, index = heapq.heappop(min_heap)
        result.append(valve)
        if arr_type == "inc":
            bounds_arr = array_bounds["inc"]
            max_i = bounds_arr[arr_index + 1]
            if index + 1 <= max_i:
                heapq.heappush(min_heap,
                               (A[index + 1], "inc", arr_index, index + 1))
        elif arr_type == "dec":
            bounds_arr = array_bounds["dec"]
            min_i = bounds_arr[arr_index - 1]
            if index - 1 >= min_i:
                heapq.heappush(min_heap,
                               (A[index - 1], "dec", arr_index, index - 1))
        else:
            assert False, f"Unrecognised array type {arr_type}"
    return result


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    return sort_k_increasing_decreasing_array_v1(A)


if __name__ == '__main__':
    TestSortIncreasingDecreasingArray(
        sort_k_increasing_decreasing_array_v1).run_tests()
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
