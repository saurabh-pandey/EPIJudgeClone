from typing import List

from test_framework import generic_test
from tests.test_is_valid_sudoku import TestIsValidSudoku


def is_valid_sudoku_v1(sudoku_puzzle: List[List[int]]) -> bool:
    def is_cell_valid(value: int, is_seen: List[int]) -> bool:
        if value > 0:
            index = value - 1
            if is_seen[index]:
                return False
            else:
                is_seen[index] = True
        return True

    for i in range(9):
        is_seen = [False] * 9
        for j in range(9):
            if not is_cell_valid(sudoku_puzzle[i][j], is_seen):
                return False
    for j in range(9):
        is_seen = [False] * 9
        for i in range(9):
            if not is_cell_valid(sudoku_puzzle[i][j], is_seen):
                return False
    for grid_i in range(0, 9, 3):
        for grid_j in range(0, 9, 3):
            is_seen = [False] * 9
            for i in range(grid_i, grid_i + 3):
                for j in range(grid_j, grid_j + 3):
                    if not is_cell_valid(sudoku_puzzle[i][j], is_seen):
                        return False
    return True

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    return is_valid_sudoku_v1(partial_assignment)


if __name__ == '__main__':
    TestIsValidSudoku(is_valid_sudoku_v1).run_tests()
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
