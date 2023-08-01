import copy

from enum import Enum
from random import sample
from typing import List

from tests.test_base import TestBase


class Level(Enum):
    EASY = (100 // 3)
    MEDIUM = (200 // 3)
    HARD = (300 // 4)


class TestSudokuSolve(TestBase):
    base: int = 3
    side: int = base * base

    
    def test_example1(self):
        solved_sudoku = self.generate_solved_sudoku()
        self.generate_sudoku_puzzle(solved_sudoku)
        self.generate_sudoku_puzzle(solved_sudoku, Level.MEDIUM)
        self.generate_sudoku_puzzle(solved_sudoku, Level.HARD)

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
            sudoku_puzzle[i][j] = 0

        numSize = len(str(TestSudokuSolve.side))
        for line in sudoku_puzzle:
            print(*(f"{n or '.':{numSize}} " for n in line))

    def is_solved(self,
                  puzzle: List[List[int]],
                  solution: List[List[int]]) -> bool:
        pass
