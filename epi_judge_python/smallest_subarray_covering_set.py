import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_smallest_subarray_covering_set import (
    TestSmallestSubarrayCoveringSet)

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set_v1(paragraph: List[str],
                                           keywords: Set[str]) -> Subarray:
    '''
    Book inspired version O(n) version
    '''
    start, end = -1, len(paragraph)
    left = 0
    right = 0
    keywords_counter = collections.Counter(keywords)
    num_keywords_left = len(keywords_counter)
    while right < len(paragraph):
        if num_keywords_left > 0:
            if paragraph[right] in keywords_counter:
                keywords_counter[paragraph[right]] -= 1
                if keywords_counter[paragraph[right]] >= 0:
                    num_keywords_left -= 1
        elif num_keywords_left == 0:
            if right - left < end - start:
                start, end = left, right
            if paragraph[left] in keywords_counter:
                keywords_counter[paragraph[left]] += 1
                if keywords_counter[paragraph[left]] > 0:
                    num_keywords_left += 1
            left += 1
        if num_keywords_left > 0:
            right += 1
    if end == len(paragraph):
        return (-1, -1)
    return (start, end)


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    return find_smallest_subarray_covering_set_v1(paragraph, keywords)


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


if __name__ == '__main__':
    TestSmallestSubarrayCoveringSet(
        find_smallest_subarray_covering_set_v1).run_tests()
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
