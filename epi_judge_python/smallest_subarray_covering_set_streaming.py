import collections
import functools
import sys

from typing import Iterator, List, Set

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
    My version
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


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    return find_smallest_subarray_covering_set_streaming_v1(
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


if __name__ == '__main__':
    TestSmallestSubarrayCoveringSet(
        find_smallest_subarray_covering_set_streaming_wrapper_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
