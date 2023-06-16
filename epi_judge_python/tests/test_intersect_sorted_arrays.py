from tests.test_base import TestBase


class TestIntersectSortedArrays(TestBase):
    def test_example1(self):
        A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
        B = [5, 5, 6, 8, 8, 9, 10, 10]
        expected = [5, 6, 8]
        result = self.solve(A, B)
        assert expected == result, f"Expected {expected} != {result} result"
