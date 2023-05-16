from tests.test_base import TestBase

import pdb

class TestOnlineMedian(TestBase):
    def test_example1(self):
        data = [1, 0, 3, 5, 2, 0, 1]
        expected = [1, 0.5, 1, 2, 2, 1.5, 1]
        # pdb.set_trace()
        result = self.solve(iter(data))
        assert result == expected, f"Expected = {expected}, result = {result}"
