from tests.test_base import TestBase

import pdb

class TestSpiralOrdering(TestBase):
    def test_three(self):
        A = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert self.solve(A) == expected
    
    def test_two(self):
        A = [[1, 2],
             [3, 4]]
        expected = [1, 2, 4, 3]
        assert self.solve(A) == expected
    
    def test_one(self):
        A = [[1]]
        expected = [1]
        assert self.solve(A) == expected
    
    def test_four(self):
        A = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        assert self.solve(A) == expected
