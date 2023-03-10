from test_framework import generic_test
from tests.test_primitive_multiply import TestPrimitiveMultiply

def multiply_v1(x: int, y: int) -> int:
    '''
    O(n^2) version
    '''
    additives = []
    while x:
        if x & 1:
            additives.append(y)
        y <<= 1
        x >>= 1
    return sum(additives)

def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestPrimitiveMultiply(multiply_v1).run_tests()
    # exit(
    #     generic_test.generic_test_main('primitive_multiply.py',
    #                                    'primitive_multiply.tsv', multiply))
