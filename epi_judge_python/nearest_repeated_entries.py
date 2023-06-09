import collections
import sys

from typing import DefaultDict, Dict, List

from test_framework import generic_test

from tests.test_nearest_repeated_entries import TestNearestRepeatedEntries


def find_nearest_repetition_v1(paragraph: List[str]) -> int:
    '''
    My version O(n) space and O(n) time where n is number of words in para
    '''
    word_indices: DefaultDict[str, List[int]] = collections.defaultdict(list)
    for i, w in enumerate(paragraph):
        word_indices[w].append(i)
    min_dist = sys.maxsize
    for indices in word_indices.values():
        for i in range(1, len(indices)):
            dist = indices[i] - indices[i - 1]
            min_dist = min(min_dist, dist)
    return min_dist if min_dist < sys.maxsize else -1

def find_nearest_repetition_v2(paragraph: List[str]) -> int:
    '''
    Books version O(k) space and O(n) time where n is number of words in para 
    and k is number of unique words
    '''
    min_dist: int = sys.maxsize
    word_last_seen_index: Dict[str, int] = {}
    for i, w in enumerate(paragraph):
        if w in word_last_seen_index:
            dist = i - word_last_seen_index[w]
            min_dist = min(min_dist, dist)
        word_last_seen_index[w] = i
    return min_dist if min_dist < sys.maxsize else -1


def find_nearest_repetition(paragraph: List[str]) -> int:
    # return find_nearest_repetition_v1(paragraph)
    return find_nearest_repetition_v2(paragraph)


if __name__ == '__main__':
    TestNearestRepeatedEntries(find_nearest_repetition_v1).run_tests()
    TestNearestRepeatedEntries(find_nearest_repetition_v2).run_tests()
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
