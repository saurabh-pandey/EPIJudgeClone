from tests.test_base import TestBase

import pdb

class TestSmallestSubarrayCoveringAllValues(TestBase):
    def test_example1(self):
        paragraph = ["a", "b", "c", "a"]
        keywords = ["b", "a"]
        result = self.solve(paragraph, keywords)
        expected = (1, 3)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        paragraph = ["a", "c", "b", "a", "c", "a", "b"]
        keywords = ["a", "b"]
        # pdb.set_trace()
        result = self.solve(paragraph, keywords)
        expected = (5, 6)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example3(self):
        paragraph = ["a", "c", "b", "d", "e", "c", "a", "b", "d", "c"]
        keywords = ["a", "b", "c"]
        result = self.solve(paragraph, keywords)
        expected = (6, 9)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example4(self):
        paragraph = ["b", "c", "a", "b", "c", "c", "a", "b", "d", "c"]
        keywords = ["a", "b", "c"]
        result = self.solve(paragraph, keywords)
        expected = (2, 4)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example5(self):
        paragraph = ["b", "c", "a", "b", "d", "e", "f", "g", "h", "c"]
        keywords = ["a", "b", "c"]
        result = self.solve(paragraph, keywords)
        expected = (2, 9)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example6(self):
        paragraph = ["b", "c", "b", "d", "e", "f", "g", "h", "c", "a"]
        keywords = ["a", "b"]
        result = self.solve(paragraph, keywords)
        expected = (-1, -1)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_attempt1(self):
        paragraph =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '2',
                      '4', '6', '1', '0', '1', '0', '1', '0', '3', '2', '1',
                      '0']
        keywords = ['0', '2', '9', '4', '6']
        # pdb.set_trace()
        result = self.solve(paragraph, keywords)
        print("Res = ", result)
