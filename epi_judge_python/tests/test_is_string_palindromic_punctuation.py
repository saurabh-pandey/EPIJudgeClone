from tests.test_base import TestBase

class TestIsStringPalindromicPunctuation(TestBase):
    def test_example1(self):
        s = "A man, a plan, a canal, Panama"
        assert self.solve(s) == True
    
    def test_example2(self):
        s = "Able was I, ere I saw Elba!"
        assert self.solve(s) == True
    
    def test_example3(self):
        s = "Ray a Ray"
        assert self.solve(s) == False
