import itertools

from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from tests.test_absent_value_array import TestAbsentValue


def find_missing_element_v1(stream: Iterator[int]) -> int:
    '''
    Book's first solution O(n) time and O(1) space complexity
    '''
    missing_ip = 0
    streams = itertools.tee(stream, 32)
    for bit in range(32):
        bit_count = [0, 0]
        max_ip_count = 1 << (31 - bit)
        for ip in streams[bit]:
            bit_count[ip >> (31 - bit) & 1] += 1
        if bit_count[1] < max_ip_count:
            # max_ip_count also acts as on bit
            missing_ip |= max_ip_count
    return missing_ip


def find_missing_element(stream: Iterator[int]) -> int:
    return find_missing_element_v1(stream)


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    TestAbsentValue(find_missing_element_v1).run_tests()
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
