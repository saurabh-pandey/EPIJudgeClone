from tests.test_base import TestBase

import pdb

class TestBuySellStockOnce(TestBase):
    def test_example1(self):
        prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        expected = 30
        # pdb.set_trace()
        assert self.solve(prices) == expected
    
    def test_monotonically_increasing(self):
        prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 9
        assert self.solve(prices) == expected
    
    def test_monotonically_decreasing(self):
        prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = 0
        assert self.solve(prices) == expected
    
    def test_constant(self):
        prices = [2, 2, 2, 2, 2, 2]
        expected = 0
        assert self.solve(prices) == expected
    
    def test_last_day_jackpot(self):
        prices = [2, 2, 2, 2, 2, 2, 1, 10]
        expected = 9
        assert self.solve(prices) == expected
    