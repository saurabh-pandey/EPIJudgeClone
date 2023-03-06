from test_framework import generic_test
from tests.test_reverse_bits import TestReverseBits

from swap_bits import swap_bits

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

def reverse_bits_v2(x: int, num_bits: int = None) -> int:
    '''
    '''
    pass

def reverse_bits(x: int) -> int:
    return reverse_bits_v1(x, 63)


if __name__ == '__main__':
    TestReverseBits(reverse_bits_v1, "My reverse bits").run_tests()
    TestReverseBits(reverse_bits_v2, "Book reverse bits").run_tests()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
