import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from tests.test_sudoku_solve import TestSudokuSolve


def solve_sudoku_v1(partial_assignment: List[List[int]]) -> bool:
    '''
    My version
    '''
    def is_valid(row, col, num) -> bool:
        for i in range(9):
            row_val = partial_assignment[row][i]
            if row_val > 0 and row_val == num:
                return False
            col_val = partial_assignment[i][col]
            if col_val > 0 and col_val == num:
                return False
        subgrid_row = 3 * (row // 3)
        subgrid_col = 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                subgrid_val = partial_assignment[i][j]
                if subgrid_val > 0 and subgrid_val == num:
                    return False
        return True
    def solve_sudoku(cell: int) -> None:
        if cell == 81:
            return True
        i = cell // 9
        j = cell % 9
        if partial_assignment[i][j] > 0:
            return solve_sudoku(cell + 1)
        for num in range(1, 10):
            if is_valid(i, j, num):
                partial_assignment[i][j] = num
                if solve_sudoku(cell + 1):
                    return True
                else:
                    partial_assignment[i][j] = 0
        return False
    return solve_sudoku(0)


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    return solve_sudoku_v1(partial_assignment)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    TestSudokuSolve(solve_sudoku_v1).run_tests()
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
