from test_framework import generic_test
from tests.test_closest_int_same_weight import TestClosestBitSameWeight

from count_bits import count_bits

def closest_int_same_bit_count_v1(x: int) -> int:
    '''
    Brute-force version
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


def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestClosestBitSameWeight(closest_int_same_bit_count_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('closest_int_same_weight.py',
    #                                    'closest_int_same_weight.tsv',
    #                                    closest_int_same_bit_count))
