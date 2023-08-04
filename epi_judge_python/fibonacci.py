import functools

from test_framework import generic_test

from tests.test_fibonacci import TestFibonacci


def fibonacci_v1(n: int) -> int:
    '''
    Classic recursive version
    '''
    if n <= 1:
        return n
    return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)


@functools.lru_cache
def cached_fibonacci_v1(n: int) -> int:
    '''
    Cached version of the classic recursive version
    '''
    if n <= 1:
        return n
    return cached_fibonacci_v1(n - 1) + cached_fibonacci_v1(n - 2)


def fibonacci_v2(n: int) -> int:
    '''
    Iterative fibonacci
    '''
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci(n: int) -> int:
    # return fibonacci_v1(n)
    # return cached_fibonacci_v1(n)
    return fibonacci_v2(n)


if __name__ == '__main__':
    TestFibonacci(fibonacci_v1).run_tests()
    TestFibonacci(cached_fibonacci_v1).run_tests()
    TestFibonacci(fibonacci_v2).run_tests()
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
