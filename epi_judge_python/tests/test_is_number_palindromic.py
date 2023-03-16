from tests.test_base import TestBase

class TestIsNumberPalindromic(TestBase):
    def test_single_digits(self):
        for x in range(10):
            assert self.solve(x) == True
    
    def test_positive_example1(self):
        test_data = [11, 22, 33, 121, 222, 989, 1001, 5555, 10101, 543212345]
        for d in test_data:
            assert self.solve(d) == True
    
    def test_negative_example1(self):
        test_data = [10, 12, 34, 1110, 1222, 9089, 11001, 123456, 43212345]
        for d in test_data:
            assert self.solve(d) == False
    
    def test_negative(self):
        for x in range(-1, -1000, -1):
            assert self.solve(x) == False
