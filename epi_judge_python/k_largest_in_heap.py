import heapq

from typing import List

from test_framework import generic_test, test_utils

from tests.test_k_largest_in_heap import TestKLargestInHeap


def k_largest_in_binary_heap_v1(A: List[int], k: int) -> List[int]:
    '''
    My version
    '''
    def get_children(n: int, size: int) -> List[int]:
        children = []
        if 2 * n + 1 < size:
            children.append(2 * n + 1)
        if 2 * n + 2 < size:
            children.append(2 * n + 2)
        return children
    
    min_heap = []
    index_queue = [0]
    while index_queue:
        curr_index_queue = index_queue[:]
        index_queue = []
        for index in curr_index_queue:
            if len(min_heap) < k:
                heapq.heappush(min_heap, A[index])
                index_queue.extend(get_children(index, len(A)))
            elif len(min_heap) == k and A[index] > min_heap[0]:
                heapq.heapreplace(min_heap, A[index])
                index_queue.extend(get_children(index, len(A)))
    return min_heap


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    return k_largest_in_binary_heap_v1(A, k)


if __name__ == '__main__':
    TestKLargestInHeap(k_largest_in_binary_heap_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
