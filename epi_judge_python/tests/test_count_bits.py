from tests.test_base import TestBase

class TestCountBits(TestBase):
    def test_example1(self):
        test_data = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 1,
            9: 2,
            10: 2,
            11: 3,
            12: 2,
            13: 3,
            14: 3,
            15: 4
        }
        for x, expected in test_data.items():
            assert self.solve(x) == expected, f"Failed for {x}"
