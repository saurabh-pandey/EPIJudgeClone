from tests.test_base import TestBase

class TestIsStringPalindromic(TestBase):
    def test_example1(self):
        s = "abccba"
        assert self.solve(s) == True
    
    def test_example2(self):
        s = "abcabc"
        assert self.solve(s) == False
    
    def test_example3(self):
        s = "a"
        assert self.solve(s) == True
