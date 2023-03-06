from tests.test_base import TestBase

class TestReverseBits(TestBase):
    def test_example1(self):
        x = 0b1011
        expected = 0b1101
        assert self.solve(x) == expected
    
    def test_example2(self):
        x = 0b11
        expected = 0b11
        assert self.solve(x) == expected
    
    def test_example3(self):
        x = 0b0
        expected = 0b0
        assert self.solve(x) == expected
    
    def test_example3(self):
        x = 0b1
        expected = 0b1
        assert self.solve(x) == expected
    
    def test_example4(self):
        x = 0b11110000
        expected = 0b00001111
        assert self.solve(x) == expected
    
    def test_run1(self):
        x = 1351510410656
        expected = 48392071865
        assert self.solve(x) == expected
    
    def test_run2(self):
        x = 1351510410656
        expected = 405942121183313920
        assert self.solve(x, 63) == expected

