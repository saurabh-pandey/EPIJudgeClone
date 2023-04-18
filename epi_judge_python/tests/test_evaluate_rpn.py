from tests.test_base import TestBase

class TestEvaluateRPN(TestBase):
    def test_example1(self):
        rpn = "3,4,+,2,*,1,+"
        assert self.solve(rpn) == 15
    
    def test_example2(self):
        rpn = "1,2,+"
        assert self.solve(rpn) == 3
    
    def test_example3(self):
        rpn = "5"
        assert self.solve(rpn) == 5
    
    def test_example4(self):
        rpn = "-6"
        assert self.solve(rpn) == -6
    
    def test_example5(self):
        rpn = "-6,-4,+"
        assert self.solve(rpn) == -10
    
    def test_example6(self):
        rpn = "-6,-4,+,2,*,1,-,7,/,2,/"
        assert self.solve(rpn) == -1