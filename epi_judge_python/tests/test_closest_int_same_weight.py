from tests.test_base import TestBase

class TestClosestBitSameWeight(TestBase):
    def test_example1(self):
        test_data = {
            1: 2,
            2: 1,
            3: 5,
            4: 2,
            5: 6,
            7: 11,
            8: 4,
            9: 10,
            10: 9,
            11: 13,
            12: 10,
            13: 14,
            14: 13,
            15: 23,
            16: 8
        }
        for x, expected in test_data.items():
            assert self.solve(x) == expected, f"Failed for {x}"
