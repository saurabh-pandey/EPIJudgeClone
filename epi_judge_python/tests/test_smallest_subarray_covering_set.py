from tests.test_base import TestBase


class TestSmallestSubarrayCoveringSet(TestBase):
    def test_example1(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"b", "c"}
        result = self.solve(paragraph, keywords)
        expected = (8, 10)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        paragraph = ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", 
                     "b", "e"]
        keywords = {"b", "c", "e"}
        result = self.solve(paragraph, keywords)
        expected = (3, 8)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example3(self):
        paragraph = ["a", "b"]
        keywords = {"a", "b"}
        result = self.solve(paragraph, keywords)
        expected = (0, 1)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_one_not_present(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"b", "e"}
        result = self.solve(paragraph, keywords)
        expected = (-1, -1)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_other_not_present(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"e", "c"}
        result = self.solve(paragraph, keywords)
        expected = (-1, -1)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_both_not_present(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"e", "f"}
        result = self.solve(paragraph, keywords)
        expected = (-1, -1)
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_both_not_present(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"e", "f"}
        result = self.solve(paragraph, keywords)
        expected = (-1, -1)
        assert result == expected, f"Expected {expected} != {result} result"
    