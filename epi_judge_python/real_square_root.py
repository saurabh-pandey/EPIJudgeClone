import math

from test_framework import generic_test

from tests.test_real_square_root import TestRealSquareRoot


def square_root_v1(x: float) -> float:
    '''
    My version
    '''
    if x == 0:
        return 0
    elif x < 1.0:
        sq_rt = square_root_v1(1 / x)
        return 1/sq_rt
    begin, end = 0.0, x
    mid = (begin + end) / 2
    sq = mid * mid
    while not math.isclose(sq, x):
        if sq > x:
            end = mid
        else:
            begin = mid
        mid = (begin + end) / 2
        sq = mid * mid
    return mid


def square_root(x: float) -> float:
    return square_root_v1(x)


if __name__ == '__main__':
    TestRealSquareRoot(square_root_v1).run_tests()
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
