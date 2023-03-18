from tests.test_base import TestBase

import collections


Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

class TestRectangleIntersection(TestBase):
    def test_example1(self):
        r1 = Rect(0, 0, 2, 2)
        r2 = Rect(1, 1, 2, 2)
        assert self.solve(r1, r2) == Rect(1, 1, 1, 1)
        assert self.solve(r2, r1) == Rect(1, 1, 1, 1)
    
    def test_example2(self):
        r1 = Rect(0, 0, 1, 1)
        r2 = Rect(2, 2, 1, 1)
        assert self.solve(r1, r2) == Rect(0, 0, -1, -1)
        assert self.solve(r2, r1) == Rect(0, 0, -1, -1)
    
    def test_inside(self):
        r1 = Rect(0, 0, 5, 3)
        r2 = Rect(1, 1, 3, 1)
        assert self.solve(r1, r2) == Rect(1, 1, 3, 1)
        assert self.solve(r2, r1) == Rect(1, 1, 3, 1)
    
    def test_congruent(self):
        r1 = Rect(0, 0, 2, 2)
        r2 = Rect(0, 0, 2, 2)
        assert self.solve(r1, r2) == Rect(0, 0, 2, 2)
        assert self.solve(r2, r1) == Rect(0, 0, 2, 2)
    
    def test_x_slit(self):
        r1 = Rect(0, 0, 3, 3)
        r2 = Rect(-1, 1, 5, 1)
        assert self.solve(r1, r2) == Rect(0, 1, 3, 1)
        assert self.solve(r2, r1) == Rect(0, 1, 3, 1)
    
    def test_x_flag(self):
        r1 = Rect(0, 0, 3, 3)
        r2 = Rect(0, 1, 3, 1)
        assert self.solve(r1, r2) == Rect(0, 1, 3, 1)
        assert self.solve(r2, r1) == Rect(0, 1, 3, 1)
    
    def test_y_slit(self):
        r1 = Rect(0, 0, 3, 3)
        r2 = Rect(1, -1, 1, 5)
        assert self.solve(r1, r2) == Rect(1, 0, 1, 3)
        assert self.solve(r2, r1) == Rect(1, 0, 1, 3)
    
    def test_y_flag(self):
        r1 = Rect(0, 0, 3, 3)
        r2 = Rect(1, 0, 1, 3)
        assert self.solve(r1, r2) == Rect(1, 0, 1, 3)
        assert self.solve(r2, r1) == Rect(1, 0, 1, 3)
    
    def test_x_line(self):
        r1 = Rect(0, 0, 2, 2)
        r2 = Rect(1, 2, 2, 2)
        assert self.solve(r1, r2) == Rect(1, 2, 1, 0)
        assert self.solve(r2, r1) == Rect(1, 2, 1, 0)
    
    def test_y_line(self):
        r1 = Rect(0, 0, 2, 2)
        r2 = Rect(2, 1, 2, 2)
        assert self.solve(r1, r2) == Rect(2, 1, 0, 1)
        assert self.solve(r2, r1) == Rect(2, 1, 0, 1)
    
    def test_corner(self):
        r1 = Rect(0, 0, 2, 2)
        r2 = Rect(2, 2, 2, 2)
        assert self.solve(r1, r2) == Rect(2, 2, 0, 0)
        assert self.solve(r2, r1) == Rect(2, 2, 0, 0)
