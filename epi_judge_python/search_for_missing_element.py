import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

from tests.test_search_for_missing_element import TestSearchMissingElement


DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing_v1(A: List[int]) -> DuplicateAndMissing:
    '''
    My brute-force version with O(n) time and space
    '''
    counter = [0] * len(A)
    for a in A:
        counter[a] += 1
    duplicate = None
    missing = None
    for i, c in enumerate(counter):
        if c == 2:
            duplicate = i
        if c == 0:
            missing = i
    return DuplicateAndMissing(duplicate, missing)


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    return find_duplicate_missing_v1(A)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    TestSearchMissingElement(find_duplicate_missing_v1).run_tests()
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
