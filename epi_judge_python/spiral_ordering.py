from typing import List

from test_framework import generic_test
from tests.test_spiral_ordering import TestSpiralOrdering

def matrix_in_spiral_order_v1(square_matrix: List[List[int]]) -> List[int]:
    '''
    My O(n^2) version
    '''
    origin = 0
    n = len(square_matrix)
    spiral_ordering = []
    while origin <= (((n + 1) // 2) - 1):
        for index in range(origin, n - origin):
            spiral_ordering.append(square_matrix[origin][index])
        for index in range(origin + 1, n - origin):
            spiral_ordering.append(square_matrix[index][n - origin - 1])
        for index in range(n - origin - 2, origin - 1, -1):
            spiral_ordering.append(square_matrix[n - origin - 1][index])
        for index in range(n - origin - 2, origin, -1):
            spiral_ordering.append(square_matrix[index][origin])
        origin += 1
    return spiral_ordering


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    return matrix_in_spiral_order_v1(square_matrix)


if __name__ == '__main__':
    TestSpiralOrdering(matrix_in_spiral_order_v1).run_tests()
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
