import unittest

from geom2d.line import Line
from geom2d.point import Point
from geom2d.vector import Vector


class TestLine(unittest.TestCase):
    def test_parallel_lines(self):
        l1 = Line(Point(0, 0), Vector(1, 1))
        l2 = Line(Point(10, 10), Vector(2, 2))
        self.assertTrue(l1.is_parallel_to(l2))

    def test_perpendicular_lines(self):
        l1 = Line(Point(0, 0), Vector(1, 0))
        l2 = Line(Point(0, 0), Vector(0, 1))
        self.assertTrue(l1.is_perpendicular_to(l2))

    def test_parallel_through_point(self):
        original = Line(Point(0, 0), Vector(1, 1))
        point = Point(5, 2)
        actual = original.parallel_through(point)
        self.assertEqual(point, actual.base)
        self.assertEqual(original.direction, actual.direction)

    def test_perpendicular_through_point(self):
        original = Line(Point(0, 0), Vector(1, 0))
        point = Point(5, 2)
        actual = original.perpendicular_through(point)
        self.assertEqual(point, actual.base)
        self.assertEqual(Vector(0, 1), actual.direction)

    def test_parallel_lines_no_intersection(self):
        l1 = Line(Point(0, 0), Vector(1, 1))
        l2 = Line(Point(10, 10), Vector(1, 1))
        self.assertIsNone(l1.intersection_with(l2))

    def test_lines_intersection(self):
        l1 = Line(Point(50, 0), Vector(0, 1))
        l2 = Line(Point(0, 30), Vector(1, 0))
        actual = l1.intersection_with(l2)
        expected = Point(50, 30)
        self.assertEqual(expected, actual)