from typing import List

from test_framework import generic_test

from tests.test_n_queens import TestNQueens


def n_queens_v1(n: int) -> List[List[int]]:
    '''
    My version
    '''
    def is_valid_move(row: int, col: int) -> bool:
        # All rows must have unique value
        unique_rows = set(queens)
        if row in unique_rows:
            return False
        # Check if this is falling on a diagonal of a queen
        for i in range(col):
            diag_row, diag_col = queens[i] - 1, i - 1
            while diag_row >= 0 and diag_col >= 0:
                if row == diag_row and col == diag_col:
                    return False
                diag_row -= 1
                diag_col -= 1
            diag_row, diag_col = queens[i] - 1, i + 1
            while diag_row >= 0 and diag_col <= col:
                if row == diag_row and col == diag_col:
                    return False
                diag_row -= 1
                diag_col += 1
            diag_row, diag_col = queens[i] + 1, i - 1
            while diag_row < n and diag_col >= 0:
                if row == diag_row and col == diag_col:
                    return False
                diag_row += 1
                diag_col -= 1
            diag_row, diag_col = queens[i] + 1, i + 1
            while diag_row < n and diag_col <= col:
                if row == diag_row and col == diag_col:
                    return False
                diag_row += 1
                diag_col += 1
        return True
    def n_queens_recursive(col: int) -> None:
        if col == n:
            solutions.append(queens[:])
        else:
            for row in range(n):
                if is_valid_move(row, col):
                    queens[col] = row
                    n_queens_recursive(col + 1)
                    queens[col] = -1
    solutions = []
    queens = [-1] * n
    n_queens_recursive(0)
    return solutions


def n_queens_v2(n: int) -> List[List[int]]:
    '''
    My another version with simpler move validity check
    '''
    def is_valid_move(row: int, col: int) -> bool:
        # All rows must have unique value
        unique_rows = set(queens)
        if row in unique_rows:
            return False
        # Check if this is falling on a diagonal of a queen
        diag_row_positive, diag_row_negative = row + 1, row - 1
        col_index = col - 1
        while (col_index >= 0
               and diag_row_positive < n or diag_row_negative >= 0):
            if (queens[col_index] == diag_row_positive
                or queens[col_index] == diag_row_negative):
                return False
            col_index -= 1
            diag_row_positive += 1
            diag_row_negative -= 1
        return True
    def n_queens_recursive(col: int) -> None:
        if col == n:
            solutions.append(queens[:])
        else:
            for row in range(n):
                if is_valid_move(row, col):
                    queens[col] = row
                    n_queens_recursive(col + 1)
                    queens[col] = -1
    solutions = []
    queens = [-1] * n
    n_queens_recursive(0)
    return solutions


def n_queens(n: int) -> List[List[int]]:
    # return n_queens_v1(n)
    return n_queens_v2(n)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    TestNQueens(n_queens_v1).run_tests()
    TestNQueens(n_queens_v2).run_tests()
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
