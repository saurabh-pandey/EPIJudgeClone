from tests.test_base import TestBase

class TestPrimitiveMultiply(TestBase):
    def test_example1(self):
        for x in range(25):
            for y in range(25):
                # print(f"### {x} * {y} = {self.solve(x, y)}")
                assert self.solve(x, y) == x * y, f"Failed for {x} * {y}"
