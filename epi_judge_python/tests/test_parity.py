from tests.test_base import TestBase

class TestParity(TestBase):
    def test_example1(self):
        test_data = {
            0: 0,
            1: 1,
            2: 1,
            3: 0,
            4: 1,
            5: 0,
            6: 0,
            7: 1,
            8: 1,
            9: 0,
            10: 0,
            11: 1,
            12: 0,
            13: 1,
            14: 1,
            15: 0
        }
        for x, expected in test_data.items():
            assert self.solve(x) == expected, f"Failed for {x}"
