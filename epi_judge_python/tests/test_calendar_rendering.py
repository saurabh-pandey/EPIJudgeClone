from tests.test_base import TestBase


class TestCalendarRendering(TestBase):
    def test_example1(self):
        events = [(1, 2), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9),
                  (12, 15), (4, 5), (9, 17)]
        result = self.solve(events)
        expected = 3
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_example2(self):
        events = [(1, 2), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9),
                  (12, 15), (4, 5), (9, 17), (9, 10)]
        result = self.solve(events)
        expected = 4
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_single(self):
        events = [(1, 2)]
        result = self.solve(events)
        expected = 1
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_disjoint(self):
        events = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        result = self.solve(events)
        expected = 1
        assert result == expected, f"Expected {expected} != {result} result"
    
    def test_pyramid(self):
        events = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]
        result = self.solve(events)
        expected = 5
        assert result == expected, f"Expected {expected} != {result} result"
