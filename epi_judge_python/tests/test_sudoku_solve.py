import copy

from enum import Enum
from random import sample
from typing import List, Tuple

from tests.test_base import TestBase


class Level(Enum):
    EASY = (100 // 3)
    MEDIUM = (200 // 3)
    HARD = (300 // 4)


class TestSudokuSolve(TestBase):
    base: int = 3
    side: int = base * base
    EMPTY: int = 0
    sub_grid: List[Tuple[int, int]] = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6),
    ]

    
    def test_sudoku(self):
        solved_sudoku = self.generate_solved_sudoku()
        puzzle = self.generate_sudoku_puzzle(solved_sudoku, Level.HARD)
        original_puzzle = copy.deepcopy(puzzle)
        result = self.solve(puzzle)
        print(f"Is solved = {result}")
        # print(f"Easy solution = {sudoku_puzzle_easy}")
        for line in puzzle: print(line)
        assert self.is_solved(original_puzzle, puzzle), (
            f"Puzzle {original_puzzle} not solved correctly")
        # print(f"Easy is solved = {self.is_solved(sudoku_puzzle_easy, solved_sudoku)}")
        # sudoku_puzzle_med = self.generate_sudoku_puzzle(solved_sudoku,
        #                                                 Level.MEDIUM)
        # print(f"Medium is solved = {self.is_solved(sudoku_puzzle_med, solved_sudoku)}")
        # sudoku_puzzle_hard = self.generate_sudoku_puzzle(solved_sudoku,
        #                                                  Level.HARD)
        # print(f"Hard is solved = {self.is_solved(sudoku_puzzle_hard, solved_sudoku)}")

        # sudoku_puzzle = self.generate_sudoku_puzzle()
        # result = self.solve(sudoku_puzzle)
        # assert self.is_solved(sudoku_puzzle, result), (
        #     f"Puzzle {sudoku_puzzle} not solved correctly")
    
    def generate_solved_sudoku(self) -> List[List[int]]:
        '''
        Got this code from stackoverflow link:
        https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
        '''
        # pattern for a baseline valid solution
        def pattern(r,c):
            return (TestSudokuSolve.base * (r % TestSudokuSolve.base)
                    + r // TestSudokuSolve.base + c) % TestSudokuSolve.side
        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(TestSudokuSolve.base) 
        rows  = [ g * TestSudokuSolve.base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g * TestSudokuSolve.base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1, TestSudokuSolve.side + 1))
        # produce board using randomized baseline pattern
        board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
        for line in board: print(line)
        return board
    
    def generate_sudoku_puzzle(self,
                               solved_sudoku: List[List[int]],
                               level: Level = Level.EASY
                               ) -> List[List[int]]:
        squares = TestSudokuSolve.side * TestSudokuSolve.side
        print(f"Level = {level}, value = {level.value}")
        empties = squares * level.value // 100
        sudoku_puzzle: List[List[int]] = copy.deepcopy(solved_sudoku)
        for p in sample(range(squares), empties):
            i = p // TestSudokuSolve.side
            j = p % TestSudokuSolve.side
            sudoku_puzzle[i][j] = TestSudokuSolve.EMPTY
        numSize = len(str(TestSudokuSolve.side))
        for line in sudoku_puzzle:
            print(*(f"{n or '.':{numSize}} " for n in line))
        return sudoku_puzzle

    def is_solved(self,
                  puzzle: List[List[int]],
                  solution: List[List[int]]) -> bool:
        def is_puzzle_solution() -> bool:
            for row in range(TestSudokuSolve.side):
                for col in range(TestSudokuSolve.side):
                    if puzzle[row][col] != TestSudokuSolve.EMPTY:
                        if puzzle[row][col] != solution[row][col]:
                            return False
            return True
        def is_row_correct(row) -> bool:
            return len(set(solution[row])) == TestSudokuSolve.side
        def is_col_correct(col) -> bool:
            unique = set()
            for i in range(TestSudokuSolve.side):
                unique.add(solution[i][col])
            return len(unique) == TestSudokuSolve.side
        def is_subgroup_correct(group) -> bool:
            unique = set()
            row_start, col_start = TestSudokuSolve.sub_grid[group]
            for row in range(row_start, row_start + TestSudokuSolve.base):
                for col in range(col_start, col_start + TestSudokuSolve.base):
                    unique.add(solution[row][col])
            return len(unique) == TestSudokuSolve.side
        if not is_puzzle_solution():
            return False
        for i in range(TestSudokuSolve.side):
            if not is_row_correct(i):
                return False
            if not is_col_correct(i):
                return False
            if not is_subgroup_correct(i):
                return False
        return True