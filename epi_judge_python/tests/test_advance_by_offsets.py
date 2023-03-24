from tests.test_base import TestBase


class TestAdvanceByOffset(TestBase):
    def test_example1(self):
        A = [3, 3, 1, 0, 2, 0, 1]
        assert self.solve(A) == True
    
    def test_example2(self):
        A = [3, 2, 0, 0, 2, 0, 1]
        assert self.solve(A) == False
    
    def test_example3(self):
        A = [2, 4, 1, 1, 0, 2, 3]
        assert self.solve(A) == True
    
    def test_halt_first(self):
        A = [0, 1, 2, 2]
        assert self.solve(A) == False
    
    def test_big_leap(self):
        A = [5, 0, 0, 0]
        assert self.solve(A) == True
    