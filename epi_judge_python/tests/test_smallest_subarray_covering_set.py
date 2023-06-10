from tests.test_base import TestBase


class TestSmallestSubarrayCoveringSet(TestBase):
    def test_example1(self):
        paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
        keywords = {"b", "c"}
        result = self.solve(paragraph, keywords)
        expected = (8, 10)
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
    