from typing import List

from tests.test_base import TestBase


class TestSudokuSolve(TestBase):
    def test_example1(self):
        sudoku_puzzle = self.generate_sudoku_puzzle()
        result = self.solve(sudoku_puzzle)
        assert self.is_solved(sudoku_puzzle, result), (
            f"Puzzle {sudoku_puzzle} not solved correctly")
    
    def generate_sudoku_puzzle(self) -> List[List[int]]:
        pass

    def is_solved(self,
                  puzzle: List[List[int]],
                  solution: List[List[int]]) -> bool:
        pass
