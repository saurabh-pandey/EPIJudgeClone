from test_framework import generic_test

from tests.test_int_square_root import TestIntSquareRoot


def square_root_v1(k: int) -> int:
    '''
    My O(log(n)) version where n is the input number
    '''
    begin, end = 0, k
    while begin < end:
        mid = begin + (end - begin) // 2
        square = mid * mid
        if square == k:
            return mid
        elif square > k:
            end = mid - 1
        elif begin == mid:
            if end * end > k:
                return begin
            else:
                return end
        else:
            begin = mid
    return begin


def square_root_v2(k: int) -> int:
    '''
    Book's version with same runtime
    '''
    begin, end = 0, k
    while begin <= end:
        mid = begin + (end - begin) // 2
        square = mid * mid
        if square <= k:
            begin = mid + 1
        else:
            end = mid - 1
    return begin - 1


def square_root(k: int) -> int:
    # return square_root_v1(k)
    return square_root_v2(k)


if __name__ == '__main__':
    TestIntSquareRoot(square_root_v1).run_tests()
    TestIntSquareRoot(square_root_v2).run_tests()
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
