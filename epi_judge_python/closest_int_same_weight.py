from test_framework import generic_test
from tests.test_closest_int_same_weight import TestClosestBitSameWeight

from count_bits import count_bits

def closest_int_same_bit_count_v1(x: int) -> int:
    '''
    Brute-force version seems O(2^n)
    '''
    diff = 1
    wt = count_bits(x)
    while True:
        if x > diff:
            x_l = x - diff
            if wt == count_bits(x_l):
                return x_l
        x_h = x + diff
        if wt == count_bits(x_h):
            return x_h
        diff += 1


def closest_int_same_bit_count_v2(x: int) -> int:
    '''
    Book O(n) solution
    '''
    i = 0
    prev_bit = x & 1
    n = x
    while n:
        i += 1
        n >>= 1
        curr_bit = n & 1
        if prev_bit ^ curr_bit:
            break
        else:
            prev_bit = curr_bit
    if i > 0:
        x ^= (1 << i)
        x ^= (1 << (i - 1))
    return x



def closest_int_same_bit_count(x: int) -> int:
    return closest_int_same_bit_count_v2(x)


if __name__ == '__main__':
    TestClosestBitSameWeight(closest_int_same_bit_count_v1).run_tests()
    TestClosestBitSameWeight(closest_int_same_bit_count_v2).run_tests()
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
