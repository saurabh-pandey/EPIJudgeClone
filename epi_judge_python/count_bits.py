from test_framework import generic_test
from tests.test_count_bits import TestCountBits

def count_bits_v1(x: int) -> int:
    '''
    Naive O(1) version
    '''
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

def count_bits_v2(x: int) -> int:
    '''
    O(k) where k is number of set bits
    '''
    count = 0
    while x:
        count += 1
        x &= (x - 1)
    return count


def count_bits(x: int) -> int:
    return count_bits_v2(x)


if __name__ == '__main__':
    TestCountBits(count_bits_v1).run_tests()
    TestCountBits(count_bits_v2).run_tests()
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
