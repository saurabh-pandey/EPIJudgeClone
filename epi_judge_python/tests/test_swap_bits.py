from tests.test_base import TestBase

class TestSwapBits(TestBase):
    def test_example1(self) -> None:
        x = 2
        i = 0
        j = 1
        expected = 1
        assert self.solve(x, i, j) == expected

    def test_example2(self) -> None:
        x = 1
        i = 0
        j = 1
        expected = 2
        assert self.solve(x, i, j) == expected
    
    def test_example3(self) -> None:
        x = 3
        i = 0
        j = 1
        expected = 3
        assert self.solve(x, i, j) == expected
    
    def test_example4(self) -> None:
        x = 4
        i = 0
        j = 2
        expected = 1
        assert self.solve(x, i, j) == expected
    
    def test_example5(self) -> None:
        x = 5
        i = 0
        j = 2
        expected = 5
        assert self.solve(x, i, j) == expected
    
    def test_example6(self) -> None:
        x = 0
        i = 0
        j = 2
        expected = 0
        assert self.solve(x, i, j) == expected
