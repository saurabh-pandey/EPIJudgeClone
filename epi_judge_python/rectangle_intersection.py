import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from tests.test_rectangle_intersection import TestRectangleIntersection

from typing import Optional, Tuple

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle_v1(r1: Rect, r2: Rect) -> Rect:
    '''
    My version
    '''
    def intersect_axis(coords) -> Optional[Tuple]:
        coords.sort(key= lambda c: c[0])
        if (coords[0][1] == coords[1][1]) and (coords[1][0] < coords[2][0]):
            return None
        return (coords[1][0], (coords[2][0] - coords[1][0]))
    
    x_coords = [(r1.x, 1), (r1.x + r1.width, 1),
                (r2.x, 2), (r2.x + r2.width, 2)]
    intersect_x = intersect_axis(x_coords)
    if not intersect_x:
        return Rect(0, 0, -1, -1)
    x_min, new_width = intersect_x
    y_coords = [(r1.y, 1), (r1.y + r1.height, 1),
                (r2.y, 2), (r2.y + r2.height, 2)]
    intersect_y = intersect_axis(y_coords)
    if not intersect_y:
        return Rect(0, 0, -1, -1)
    y_min, new_height = intersect_y
    return Rect(x_min, y_min, new_width, new_height)

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    return intersect_rectangle_v1(r1, r2)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    TestRectangleIntersection(intersect_rectangle_v1).run_tests()
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
