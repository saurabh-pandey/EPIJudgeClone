from tests.test_base import TestBase


class TestFibonacci(TestBase):
    def test_all(self):
        fibonacci_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for n, val in enumerate(fibonacci_series):
            result = self.solve(n)
            assert result == val, f"Expected {val} != {result}"
