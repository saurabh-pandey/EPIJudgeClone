from tests.test_base import TestBase

import math

class TestPowerXY(TestBase):
    def test_example1(self):
        for x in range(1, 6):
            for y in range(1, 11):
                assert self.solve(x, y) == pow(x, y)
    
    def test_example2(self):
        start = 1.2
        for i in range(1, 6):
            for y in range(1, 11):
                x = start + i
                # print(f"{x}^{y} = {self.solve(x, y)}, {x ** y}, {math.isclose(self.solve(x, y), (x ** y))}")
                assert math.isclose(self.solve(x, y), (x ** y))
    
    def test_example3(self):
        start = 1.2
        for i in range(1, 6):
            for y in range(1, 11):
                x = -(start + i)
                # print(f"{x}^{y} = {self.solve(x, y)}, {x ** y}, {math.isclose(self.solve(x, y), (x ** y))}")
                assert math.isclose(self.solve(x, y), (x ** y))
    
    def test_example4(self):
        start = 1.2
        for i in range(1, 6):
            for y in range(-1, -11, -1):
                x = start + i
                # print(f"{x}^{y} = {self.solve(x, y)}, {x ** y}, {math.isclose(self.solve(x, y), (x ** y))}")
                assert math.isclose(self.solve(x, y), (x ** y))

