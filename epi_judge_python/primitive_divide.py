from test_framework import generic_test
from tests.test_primitive_divide import TestPrimitiveDivide

import pdb

def divide_v1(x: int, y: int) -> int:
    # pdb.set_trace()
    assert y != 0
    running_diff = x
    quotient = 0
    while running_diff >= y:
        running_diff -= y
        quotient += 1
    return quotient

def divide(x: int, y: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestPrimitiveDivide(divide_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('primitive_divide.py',
    #                                    'primitive_divide.tsv', divide))
