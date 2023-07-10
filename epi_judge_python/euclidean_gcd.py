from test_framework import generic_test

from tests.test_euclidean_gcd import TestEuclideanGcd


def gcd_v1(x: int, y: int) -> int:
    '''
    My version with O(log(max(x, y))) time and space complexity
    '''
    bigger, smaller = x, y
    if bigger < smaller:
        bigger, smaller = smaller, bigger
    if smaller == 0:
        return bigger
    mod = bigger % smaller
    if mod == 0:
        return smaller
    return gcd(smaller, mod)


def gcd_v2(x: int, y: int) -> int:
    '''
    Book's version with same complexity
    '''
    return x if y == 0 else gcd_v2(y, x % y)


def gcd(x: int, y: int) -> int:
    # return gcd_v1(x, y)
    return gcd_v2(x, y)


if __name__ == '__main__':
    TestEuclideanGcd(gcd_v1).run_tests()
    TestEuclideanGcd(gcd_v2).run_tests()
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
