from test_framework import generic_test

from tests.test_euclidean_gcd import TestEuclideanGcd


def gcd_v1(x: int, y: int) -> int:
    return 0


def gcd(x: int, y: int) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    TestEuclideanGcd(gcd_v1).run_tests()
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
