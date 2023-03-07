from test_framework import generic_test
from tests.test_reverse_bits import TestReverseBits

from swap_bits import swap_bits

from typing import List

import math

def reverse_bits_v1(x: int, num_bits: int = None) -> int:
    '''
    O(n) solution
    '''
    if x == 0:
        return x
    if not num_bits:
        num_bits = math.floor(math.log2(x))
    i = 0
    j = num_bits
    while i < j:
        x = swap_bits(x, i, j)
        i += 1
        j -= 1
    return x


def fill_reverse_cache(cache_limit: int) -> List:
    max_val = 1 << cache_limit
    cache = [0 for _ in range(max_val)]
    for i, _ in enumerate(cache):
        cache[i] = reverse_bits_v1(i, (cache_limit - 1))
    return cache

REVERSE_CACHE = fill_reverse_cache(16)


def reverse_bits_v2(x: int, num_bits: int = None) -> int:
    '''
    O(n/16)
    '''
    mask_size = 16
    bit_mask = 0xFFFF
    r_0 = REVERSE_CACHE[x & bit_mask] << (3 * mask_size)
    r_1 = REVERSE_CACHE[(x >> mask_size) & bit_mask] << (2 * mask_size)
    r_2 = REVERSE_CACHE[(x >> (mask_size * 2)) & bit_mask] << mask_size
    r_3 = REVERSE_CACHE[(x >> (mask_size * 3)) & bit_mask]
    rev_x = r_0 | r_1 | r_2 | r_3
    return rev_x

def reverse_bits(x: int) -> int:
    # return reverse_bits_v1(x, 63)
    return reverse_bits_v2(x)


if __name__ == '__main__':
    TestReverseBits(reverse_bits_v1, "My reverse bits").run_tests()
    TestReverseBits(reverse_bits_v2, "Book reverse bits").run_tests("test_run2")
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
