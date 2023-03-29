from tests.test_base import TestBase

class TestIsValidSudoku(TestBase):
    def test_example1(self):
        A = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [7, 0, 0, 5, 9, 8, 0, 2, 1],
             [0, 1, 0, 4, 0, 0, 9, 0, 3],
             [3, 0, 6, 7, 0, 0, 4, 0, 8],
             [8, 2, 0, 1, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 0, 0],
             [0, 8, 4, 3, 0, 7, 0, 5, 0],
             [6, 9, 0, 0, 0, 0, 2, 0, 0],
             [1, 3, 0, 0, 0, 2, 8, 0, 7]]
        assert self.solve(A)
