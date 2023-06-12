import collections
import functools
import sys

from typing import Any, Iterator, List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_smallest_subarray_covering_set import (
    TestSmallestSubarrayCoveringSet)

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set_streaming_v1(
        paragraph: Iterator[str],
        keywords: Set[str]) -> Subarray:
    '''
    My version with O(nk) where n is paragraph size and k is size of keywords
    time and O(k) space
    '''
    start, end = -1, -1
    keyword_index = {k : [] for k in keywords}
    for idx, word in enumerate(paragraph):
        if word in keyword_index:
            if keyword_index[word]:
                keyword_index[word][0] = idx
            else:
                keyword_index[word].append(idx)
            all_found = True
            min_idx = sys.maxsize
            max_idx = -1
            for idx_list in keyword_index.values():
                if not idx_list:
                    all_found = False
                    break
                else:
                    min_idx = min(min_idx, idx_list[0])
                    max_idx = max(max_idx, idx_list[0])
            if all_found:
                if (start, end) == (-1, -1):
                    start, end = min_idx, max_idx
                elif max_idx - min_idx < end - start:
                    start, end = min_idx, max_idx
    return start, end


def find_smallest_subarray_covering_set_streaming_v2(
        paragraph: Iterator[str],
        keywords: Set[str]) -> Subarray:
    '''
    Book's version with O(n) time where n is paragraph size and k is size of keywords and O(k) space
    '''
    class Node:
        def __init__(self, data: Any) -> None:
            self.data: Any = data
            self.next: 'Node' = None
            self.prev: 'Node' = None
    
    class DoublyLinkedList:
        def __init__(self) -> None:
            self.head: Node = None
            self.tail: Node = None
            self._size: int = 0
        
        def __len__(self) -> int:
            return self._size
        
        def insert_at_tail(self, value: int) -> None:
            node = Node(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1
        
        def remove(self, node: Node) -> None:
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = None
            node.prev = None
            self._size -= 1
    
    start, end = -1, -1
    keyword_node_map = {k: None for k in keywords}
    index_list = DoublyLinkedList()
    for idx, word in enumerate(paragraph):
        if word in keyword_node_map:
            node = keyword_node_map[word]
            if node:
                index_list.remove(node)
            index_list.insert_at_tail(idx)
            keyword_node_map[word] = index_list.tail
        if len(index_list) == len(keywords):
            if (start, end) == (-1, -1):
                start, end = index_list.head.data, idx
            elif idx - index_list.head.data < end - start:
                start, end = index_list.head.data, idx
    return start, end


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    # return find_smallest_subarray_covering_set_streaming_v1(
    #     iter(paragraph), keywords)
    return find_smallest_subarray_covering_set_streaming_v2(
        iter(paragraph), keywords)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


def find_smallest_subarray_covering_set_streaming_wrapper_v1(
        paragraph: List[str],
        keywords: Set[str]) -> Subarray:
    return find_smallest_subarray_covering_set_streaming_v1(
        iter(paragraph), keywords)


def find_smallest_subarray_covering_set_streaming_wrapper_v2(
        paragraph: List[str],
        keywords: Set[str]) -> Subarray:
    return find_smallest_subarray_covering_set_streaming_v2(
        iter(paragraph), keywords)


if __name__ == '__main__':
    TestSmallestSubarrayCoveringSet(
        find_smallest_subarray_covering_set_streaming_wrapper_v1).run_tests()
    TestSmallestSubarrayCoveringSet(
        find_smallest_subarray_covering_set_streaming_wrapper_v2).run_tests()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
