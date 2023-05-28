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


def find_missing_element_v2(stream: Iterator[int]) -> int:
    '''
    Book's better solution O(n) time and O(1) space complexity
    '''
    num_buckets = 1 << 16
    counter = [0] * num_buckets
    stream1, stream2 = itertools.tee(stream)
    for ip in stream1:
        upper_part_ip = ip >> 16
        counter[upper_part_ip] += 1
    bucket_capacity = 1 << 16
    missing_ip_upper_part = next(i for i, c in enumerate(counter)
                                 if c < bucket_capacity)
    candidates = [0] * bucket_capacity
    for ip in stream2:
        upper_part_ip = ip >> 16
        if upper_part_ip == missing_ip_upper_part:
            lower_part_ip = ((1 << 16) - 1) & ip
            candidates[lower_part_ip] = 1
    for i, c in enumerate(candidates):
        if c == 0:
            return (missing_ip_upper_part << 16) | i


def find_missing_element(stream: Iterator[int]) -> int:
    # return find_missing_element_v1(stream)
    return find_missing_element_v2(stream)


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    TestAbsentValue(find_missing_element_v1).run_tests()
    TestAbsentValue(find_missing_element_v2).run_tests()
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
