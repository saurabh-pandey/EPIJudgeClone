from tests.test_base import TestBase


class TestIntersectSortedArrays(TestBase):
    def test_example1(self):
        A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
        B = [5, 5, 6, 8, 8, 9, 10, 10]
        expected = [5, 6, 8]
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_no_intersection(self):
        A = [1, 2, 3, 3, 4, 4]
        B = [5, 5, 6, 8, 8, 9, 10, 10]
        expected = []
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_intersection(self):
        A = [1, 2, 3, 3, 4, 4]
        B = [1, 2, 3, 3, 4, 4]
        expected = [1, 2, 3, 4]
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_same(self):
        A = [1, 1, 1, 1, 1, 1]
        B = [1, 1, 1, 1, 1, 1]
        expected = [1]
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_diff(self):
        A = [1, 1, 1, 1, 1, 1]
        B = [2, 2, 2, 2, 2, 2]
        expected = []
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
    