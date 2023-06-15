import bisect
import collections
import functools
import sys

from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_smallest_subarray_covering_all_values import (
    TestSmallestSubarrayCoveringAllValues)

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset_v1(paragraph: List[str],
                                                  keywords: List[str]
                                                  ) -> Subarray:
    '''
    My version with O(n) space and O(n*log(n/k)) where k is keyword size
    '''
    def find_min_index(kw_indices, kw, index, value):
        indices = kw_indices[kw[index]]
        next_index = bisect.bisect_left(indices, value) - 1
        if next_index < 0:
            return -1
        new_value = indices[next_index]
        if index == 0:
            return new_value
        return find_min_index(kw_indices, kw, index - 1, new_value)
    kw_indices = {k : [] for k in keywords}
    start, end = -1, -1
    for i, word in enumerate(paragraph):
        if word in kw_indices:
            kw_indices[word].append(i)
    for index in reversed(kw_indices[keywords[len(keywords) - 1]]):
        min_index = find_min_index(kw_indices,
                                   keywords,
                                   len(keywords) - 2,
                                   index)
        if min_index >= 0:
            if (start, end) == (-1, -1):
              start, end = min_index, index
            elif index - min_index < end - start:
                start, end = min_index, index
    return start, end


def find_smallest_sequentially_covering_subset_v2(paragraph: List[str],
                                                  keywords: List[str]
                                                  ) -> Subarray:
    '''
    A brute-force O(n^2) version with O(1) space
    '''
    start, end = -1, -1
    for left, word in enumerate(paragraph):
        if word == keywords[0]:
            # Since first keyword is found, now find the subset anchored at this
            # starting point
            right = left + 1
            kw_found = 1
            while kw_found < len(keywords) and right < len(paragraph):
                if keywords[kw_found] == paragraph[right]:
                    kw_found += 1
                right += 1
            if kw_found == len(keywords):
                if (start, end) == (-1, -1):
                    start, end = left, right - 1
                elif right - left -1 < end - start:
                    start, end = left, right - 1
    return start, end


def find_smallest_sequentially_covering_subset_v3(paragraph: List[str],
                                                  keywords: List[str]
                                                  ) -> Subarray:
    '''
    Books O(n) version with O(k) space where k is size of keywords
    '''
    start, end = -1, -1
    keyword_to_index = {k : i for i, k in enumerate(keywords)}
    latest_index = [-1] * len(keywords)
    shortest_subarray_length = [sys.maxsize] * len(keywords)
    shortest_distance = sys.maxsize
    for i, word in enumerate(paragraph):
        if word in keyword_to_index:
            kw_index = keyword_to_index[word]
            if kw_index == 0:
                shortest_subarray_length[0] = 1
            elif shortest_subarray_length[kw_index - 1] != sys.maxsize:
                shortest_subarray_length[kw_index] = shortest_subarray_length[kw_index - 1]  + i - latest_index[kw_index - 1]
            latest_index[kw_index] = i
            if (kw_index == len(keywords) - 1
                    and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                start, end = i - shortest_distance + 1, i
    return start, end


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    # start, end = find_smallest_sequentially_covering_subset_v1(paragraph, 
    #                                                            keywords)
    # start, end = find_smallest_sequentially_covering_subset_v2(paragraph, 
    #                                                            keywords)
    start, end = find_smallest_sequentially_covering_subset_v3(paragraph, 
                                                               keywords)
    return Subarray(start, end)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    TestSmallestSubarrayCoveringAllValues(
        find_smallest_sequentially_covering_subset_v1).run_tests()
    TestSmallestSubarrayCoveringAllValues(
        find_smallest_sequentially_covering_subset_v2).run_tests()
    TestSmallestSubarrayCoveringAllValues(
        find_smallest_sequentially_covering_subset_v3).run_tests()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
