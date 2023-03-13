from test_framework import generic_test
from tests.test_primitive_divide import TestPrimitiveDivide

import pdb

def divide_v1(x: int, y: int) -> int:
    '''
    O(2^n) brute-force division
    '''
    assert y != 0
    running_diff = x
    quotient = 0
    while running_diff >= y:
        running_diff -= y
        quotient += 1
    return quotient

def divide_v2(x: int, y: int) -> int:
    '''
    O(n^2) version by jumping more per iteration
    '''
    assert y != 0
    quotient = 0
    while x >= y:
        power = 0
        diff = x
        while diff >= 0:
            power += 1
            diff = x - (y << power)
        quotient += 1 << (power - 1)
        x -= (y << (power - 1))
    return quotient

def divide(x: int, y: int) -> int:
    return divide_v2(x, y)


if __name__ == '__main__':
    TestPrimitiveDivide(divide_v1).run_tests()
    TestPrimitiveDivide(divide_v2).run_tests()
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
