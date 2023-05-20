from tests.test_base import TestBase


class TestSearchFirstKey(TestBase):
    def test_example1(self):
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        value_expected = {108: 3, 285: 6, 110: -1, 410: -1, -20: -1, -10: 1, 
                          401: 9, -14: 0, 2: 2, 243: 5}
        for val, expected in value_expected.items():
            result = self.solve(A, val)
            assert expected == result, (
                f"expected = {expected}, result = {result}")
    
    def test_all_const(self):
        A = [2, 2, 2, 2, 2, 2]
        expected = 0
        result = self.solve(A, 2)
        assert expected == result, f"expected = {expected}, result = {result}"
        expected = -1
        result = self.solve(A, 1)
        assert expected == result, f"expected = {expected}, result = {result}"
    