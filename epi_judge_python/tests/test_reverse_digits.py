from tests.test_base import TestBase

class TestReverseDigits(TestBase):
    def test_example1(self):
        x = 24
        expected = 42
        assert self.solve(x) == expected
    
    def test_example2(self):
        x = -24
        expected = -42
        assert self.solve(x) == expected
    
    def test_example3(self):
        x = 0
        expected = 0
        assert self.solve(x) == expected
    
    def test_example4(self):
        x = 1
        expected = 1
        assert self.solve(x) == expected
    
    def test_example5(self):
        x = 11
        expected = 11
        assert self.solve(x) == expected
    
    def test_example6(self):
        x = -22
        expected = -22
        assert self.solve(x) == expected
    
    def test_example7(self):
        x = 333
        expected = 333
        assert self.solve(x) == expected
    
    def test_example7(self):
        x = -444
        expected = -444
        assert self.solve(x) == expected
    
    def test_example8(self):
        x = 10
        expected = 1
        assert self.solve(x) == expected
    
    def test_example9(self):
        x = 100
        expected = 1
        assert self.solve(x) == expected
    
    def test_example10(self):
        x = 1010
        expected = 101
        assert self.solve(x) == expected
