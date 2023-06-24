from tests.test_base import TestBase

import pdb

class TestIntervalUnion(TestBase):
    # Intervals are passed as mathematical intervals where () means open and
    # [] means closed
    def test_example1(self):
        intervals = ["(0, 3)", "[1, 1]", "[2, 4]", "[3, 4)", "[5, 7)",
                     "[7, 8)", "[8, 11)", "(9, 11]", "[12, 14]", "(12, 16]",
                     "(13, 15)", "(16, 17)"]
        result = self.solve(intervals)
        expected = ["(0, 4]", "[5, 11]", "[12, 17)"]
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        intervals = ["(0, 3)", "(3, 5)", "[3, 6]"]
        result = self.solve(intervals)
        expected = ["(0, 6]"]
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example3(self):
        intervals = ["(0, 1)", "[1, 5)", "(5, 7)", "[5, 8]"]
        result = self.solve(intervals)
        expected = ["(0, 8]"]
        assert result == expected, f"Expected {expected} != {result} result"
