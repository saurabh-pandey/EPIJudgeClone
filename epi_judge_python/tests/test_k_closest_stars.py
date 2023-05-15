import math

from tests.test_base import TestBase

import pdb

class TestKClosestStars(TestBase):
    def test_example1(self):
        stars = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        k = 2
        # pdb.set_trace()
        k_closest_stars = self.solve(stars, k)
        expected = [(1, 0, 0), (2, 0, 0)]
        self._check(expected, k_closest_stars)
    
    def test_example2(self):
        stars = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        k = 3
        k_closest_stars = self.solve(stars, k)
        expected = [(1, 0, 0), (2, 0, 0), (3, 0, 0)]
        self._check(expected, k_closest_stars)
    
    def test_example3(self):
        stars = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        k = 4
        k_closest_stars = self.solve(iter(stars), k)
        expected = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        self._check(expected, k_closest_stars)
    
    def test_example4(self):
        stars = [(-1, 0, 0), (-2, 0, 0), (-3, 0, 0), (-4, 0, 0),
                 (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        k = 2
        k_closest_stars = self.solve(iter(stars), k)
        expected = [(-1, 0, 0), (1, 0, 0)]
        self._check(expected, k_closest_stars)
    
    def test_example5(self):
        stars = [(-1, 0, 0), (-2, 0, 0), (-3, 0, 0), (-4, 0, 0),
                 (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]
        k = 4
        k_closest_stars = self.solve(iter(stars), k)
        expected = [(-2, 0, 0), (-1, 0, 0), (1, 0, 0), (2, 0, 0)]
        self._check(expected, k_closest_stars)

    def _check(self, expected, result) -> None:
        assert len(expected) == len(result), f"Length mismatch"
        for coord1, coord2 in zip(expected, sorted(result)):
            assert all(math.isclose(c1, c2) for c1, c2 in zip(coord1,
                                                              coord2)), (
                f"Mismatch in coords")
