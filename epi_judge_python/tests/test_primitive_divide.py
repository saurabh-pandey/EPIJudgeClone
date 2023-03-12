from tests.test_base import TestBase

class TestPrimitiveDivide(TestBase):
    def test_division(self):
        for x in range(1000):
            for y in range(1, 1001):
                # print(f"### {x}//{y} = {self.solve(x, y)}")
                assert self.solve(x, y) == (x // y)
