import unittest

from geom2d.point import Point
from geom2d.rect import Rect
from geom2d.rects import make_rect_containing, make_rect_containing_with_margin
from geom2d.size import Size


class TestRect(unittest.TestCase):
    def test_equality(self):
        rect = Rect(Point(1, 2), Size(3, 4))
        self.assertEqual(Rect(Point(1, 2), Size(3, 4)), rect)

    def test_make_rect_containing_points(self):
        points = [Point(4, 7), Point(-2, 1), Point(3, 10)]
        expected = Rect(Point(-2, 1), Size(6, 9))
        self.assertEqual(expected, make_rect_containing(points))

    def test_make_rect_containing_single_point(self):
        point = Point(4, 7)
        expected = Rect(point, Size(0, 0))
        self.assertEqual(expected, make_rect_containing([point]))

    def test_make_rect_containing_with_margin(self):
        points = [Point(0, 0), Point(2, 4)]
        expected = Rect(Point(-1, -1), Size(4, 6))
        self.assertEqual(expected, make_rect_containing_with_margin(points, 1))
