from tests.test_base import TestBase

from k_closest_stars import Star

class TestKClosestStars(TestBase):
    def test_example1(self):
        stars = [Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(4, 0, 0)]
        k = 2
        k_closest_stars = self.solve(iter(stars), k)
        expected = [Star(1, 0, 0), Star(2, 0, 0)]
        assert k_closest_stars == expected, (
            f"Expected = {expected}, result = {k_closest_stars}")
    
    def test_example2(self):
        stars = [Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(4, 0, 0)]
        k = 3
        k_closest_stars = self.solve(iter(stars), k)
        expected = [Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0)]
        assert k_closest_stars == expected, (
            f"Expected = {expected}, result = {k_closest_stars}")
    
    def test_example3(self):
        stars = [Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(4, 0, 0)]
        k = 4
        k_closest_stars = self.solve(iter(stars), k)
        expected = [Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(3, 0, 0)]
        assert k_closest_stars == expected, (
            f"Expected = {expected}, result = {k_closest_stars}")
    
    def test_example4(self):
        stars = [Star(-1, 0, 0), Star(-2, 0, 0), Star(-3, 0, 0), Star(-4, 0, 0),
                 Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(4, 0, 0)]
        k = 2
        k_closest_stars = self.solve(iter(stars), k)
        expected = [Star(-1, 0, 0), Star(1, 0, 0)]
        assert k_closest_stars == expected, (
            f"Expected = {expected}, result = {k_closest_stars}")
    
    def test_example5(self):
        stars = [Star(-1, 0, 0), Star(-2, 0, 0), Star(-3, 0, 0), Star(-4, 0, 0),
                 Star(1, 0, 0), Star(2, 0, 0), Star(3, 0, 0), Star(4, 0, 0)]
        k = 4
        k_closest_stars = self.solve(iter(stars), k)
        expected = [Star(-1, 0, 0), Star(-2, 0, 0), Star(1, 0, 0),
                    Star(2, 0, 0)]
        assert k_closest_stars == expected, (
            f"Expected = {expected}, result = {k_closest_stars}")
