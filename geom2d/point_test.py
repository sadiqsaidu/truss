import math
import unittest

from geom2d.point import Point
from geom2d.vector import Vector


class TestPoint(unittest.TestCase):

    def test_distance_to(self):
        p = Point(1, 2)
        q = Point(4, 6)
        expected = 5
        actual = p.distance_to(q)

        self.assertAlmostEqual(expected, actual)

    def test_distance_to_is_symmetric(self):
        p = Point(-3, 7)
        q = Point(2, -5)
        self.assertAlmostEqual(p.distance_to(q), q.distance_to(p))

    def test_distance_to_self_is_zero(self):
        p = Point(3.5, -2.1)
        self.assertAlmostEqual(0.0, p.distance_to(p))

    def test_distance_to_along_axes(self):
        origin = Point(0, 0)
        self.assertAlmostEqual(7, origin.distance_to(Point(7, 0)))
        self.assertAlmostEqual(7, origin.distance_to(Point(0, -7)))

    def test_distance_to_diagonal(self):
        self.assertAlmostEqual(math.sqrt(2), Point(0, 0).distance_to(Point(1, 1)))

    def test_add_points(self):
        expected = Point(5, 8)
        actual = Point(1, 2) + Point(4, 6)
        self.assertEqual(expected, actual)

    def test_add_returns_point(self):
        self.assertIsInstance(Point(1, 2) + Point(3, 4), Point)

    def test_add_does_not_mutate_operands(self):
        p = Point(1, 2)
        q = Point(3, 4)
        _ = p + q
        self.assertEqual(Point(1, 2), p)
        self.assertEqual(Point(3, 4), q)

    def test_subtract_points_returns_vector(self):
        result = Point(4, 6) - Point(1, 2)
        self.assertIsInstance(result, Vector)
        self.assertEqual(Vector(3, 4), result)

    def test_subtract_points_direction(self):
        self.assertEqual(Vector(-3, -4), Point(1, 2) - Point(4, 6))

    def test_subtract_same_point_is_zero_vector(self):
        p = Point(5, 5)
        self.assertEqual(Vector(0, 0), p - p)

    def test_displaced_default_times(self):
        p = Point(1, 2)
        self.assertEqual(Point(4, 6), p.displaced(Vector(3, 4)))

    def test_displaced_multiple_times(self):
        p = Point(1, 2)
        self.assertEqual(Point(7, 10), p.displaced(Vector(3, 4), times=2))

    def test_displaced_negative_times(self):
        p = Point(1, 2)
        self.assertEqual(Point(-2, -2), p.displaced(Vector(3, 4), times=-1))

    def test_displaced_zero_times(self):
        p = Point(1, 2)
        self.assertEqual(p, p.displaced(Vector(3, 4), times=0))

    def test_displaced_returns_new_point(self):
        p = Point(1, 2)
        moved = p.displaced(Vector(1, 1))
        self.assertIsNot(p, moved)
        self.assertEqual(Point(1, 2), p)

    def test_displaced_and_subtract_round_trip(self):
        p = Point(1, 2)
        q = Point(7, -3)
        self.assertEqual(q, p.displaced(q - p))

    def test_equal_points(self):
        self.assertEqual(Point(1, 2), Point(1, 2))

    def test_equal_to_itself(self):
        p = Point(1, 2)
        self.assertEqual(p, p)

    def test_equal_within_tolerance(self):
        self.assertEqual(Point(1, 2), Point(1 + 1e-12, 2 - 1e-12))

    def test_not_equal_different_x(self):
        self.assertNotEqual(Point(1, 2), Point(1.1, 2))

    def test_not_equal_different_y(self):
        self.assertNotEqual(Point(1, 2), Point(1, 2.1))

    def test_not_equal_to_other_types(self):
        self.assertNotEqual(Point(1, 2), (1, 2))
        self.assertNotEqual(Point(1, 2), Vector(1, 2))
        self.assertNotEqual(Point(1, 2), None)

    def test_str(self):
        self.assertEqual('(1, 2)', str(Point(1, 2)))

    def test_str_with_floats(self):
        self.assertEqual('(1.5, -2.25)', str(Point(1.5, -2.25)))


if __name__ == '__main__':
    unittest.main()