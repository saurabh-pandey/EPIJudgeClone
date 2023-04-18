from tests.test_base import TestBase

import pdb

class TestEvaluateRPN(TestBase):
    def test_example1(self):
        rpn = "3,4,+,2,*,1,+"
        assert self.solve(rpn) == 15
    
    def test_example2(self):
        rpn = "1,2,+"
        assert self.solve(rpn) == 3
    
    def test_example3(self):
        rpn = "5"
        # pdb.set_trace()
        assert self.solve(rpn) == 5
    
    def test_example4(self):
        rpn = "-6"
        # pdb.set_trace()
        assert self.solve(rpn) == -6
    
    def test_example5(self):
        rpn = "-6,-4,+"
        assert self.solve(rpn) == -10
    
    def test_example6(self):
        rpn = "-6,-4,+,2,*,1,-,7,/,2,/"
        # pdb.set_trace()
        res = self.solve(rpn)
        # print(f"Res = {res}")
        expected = -2
        assert res == expected, f"expected = {expected}, actual = {res}"
    
    def test_attempt1(self):
        rpn = "11,8,10,*,+,7,12,*,+,12,7,*,+,9,14,*,+,17,+"
        res = self.solve(rpn)
        expected = 402
        assert res == expected, f"expected = {expected}, actual = {res}"
