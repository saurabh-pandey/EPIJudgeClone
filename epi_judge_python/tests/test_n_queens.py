import time

from typing import List

from tests.test_base import TestBase


class TestNQueens(TestBase):
    def test_example1(self):
        n = 4
        expected: List[List[int]] = [[1, 3, 0, 2], [2, 0, 3, 1]]
        result = self.solve(n)
        assert all(self.check_n_queens_solution(n, res) for res in result)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all(self):
        for n in range(0, 11):
            start = time.time()
            result = self.solve(n)
            print(f"N = {n}, num_solutions = {len(result)}, time = {time.time() - start}")
            assert all(self.check_n_queens_solution(n, res) for res in result)

    def check_n_queens_solution(self, n: int, solution: List[int]) -> bool:
        if len(solution) != n:
            # Not correct number of queens
            return False
        if len(solution) != len(set(solution)):
            # All rows should be unique
            return False
        for col, row in enumerate(solution):
            # Check if some queen is on a diagonal
            diag_row, diag_col = row - 1, col - 1
            while diag_row >= 0 and diag_col >= 0:
                if solution[diag_col] == diag_row:
                    return False
                diag_row -= 1
                diag_col -= 1
            diag_row, diag_col = row - 1, col + 1
            while diag_row >= 0 and diag_col < n:
                if solution[diag_col] == diag_row:
                    return False
                diag_row -= 1
                diag_col += 1
            diag_row, diag_col = row + 1, col - 1
            while diag_row < n and diag_col >= 0:
                if solution[diag_col] == diag_row:
                    return False
                diag_row += 1
                diag_col -= 1
            diag_row, diag_col = row + 1, col + 1
            while diag_row < n and diag_col < n:
                if solution[diag_col] == diag_row:
                    return False
                diag_row += 1
                diag_col += 1
        return True
