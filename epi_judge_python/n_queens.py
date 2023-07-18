from typing import List

from test_framework import generic_test

from tests.test_n_queens import TestNQueens


def n_queens_v1(n: int) -> List[List[int]]:
    '''
    My version
    '''
    return []


def n_queens(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    return []


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    TestNQueens(n_queens_v1).run_tests()
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
