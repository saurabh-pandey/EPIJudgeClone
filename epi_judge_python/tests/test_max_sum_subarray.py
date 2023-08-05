from tests.test_base import TestBase

class TestMaxSumSubarray(TestBase):
    def test_example1(self):
        A = [904, 40, 523, 12, -335, -385, -124, 481, -31]
        result = self.solve(A)
        expected = 1479
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = self.solve(A)
        expected = 6
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_positive(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        result = self.solve(A)
        expected = 36
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_negative(self):
        A = [-1, -2, -3, -4, -5, -6, -7, -8]
        result = self.solve(A)
        expected = 0
        assert expected == result, f"Expected {expected} != {result} result"
