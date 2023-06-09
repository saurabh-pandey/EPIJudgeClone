from tests.test_base import TestBase


class TestNearestRepeatedEntries(TestBase):
    def test_example1(self):
        words = ["All", "work", "and", "no", "play", "makes", "for", "no", 
                 "work", "no", "fun", "and", "no", "result"]
        expected = 2
        result = self.solve(words)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_no_repeat(self):
        words = ["All", "work", "and", "no", "play", "makes", "for"]
        expected = -1
        result = self.solve(words)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_all_repeat(self):
        words = ["All", "all", "all", "all", "all", "all"]
        expected = 1
        result = self.solve(words)
        assert expected == result, f"Expected {expected} != {result} result"
    
    def test_end_repeat(self):
        words = ["All", "work", "and", "no", "play", "makes", "for", "All"]
        expected = 7
        result = self.solve(words)
        assert expected == result, f"Expected {expected} != {result} result"
