import math
import unittest

from geom2d.vector import Vector


class TestVector(unittest.TestCase):
    u = Vector(1, 2)
    v = Vector(4, 6)

    # ---- arithmetic -------------------------------------------------

    def test_plus(self):
        expected = Vector(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    def test_plus_is_commutative(self):
        self.assertEqual(self.u + self.v, self.v + self.u)

    def test_plus_zero_vector_is_identity(self):
        self.assertEqual(self.u, self.u + Vector(0, 0))

    def test_minus_self_is_zero_vector(self):
        self.assertEqual(Vector(0, 0), self.u - self.u)

    def test_operations_do_not_mutate_operands(self):
        a = Vector(1, 2)
        b = Vector(3, 4)
        _ = a + b
        _ = a - b
        self.assertEqual(Vector(1, 2), a)
        self.assertEqual(Vector(3, 4), b)

    def test_scaled_by(self):
        self.assertEqual(Vector(3, 6), self.u.scaled_by(3))

    def test_scaled_by_negative(self):
        self.assertEqual(Vector(-2, -4), self.u.scaled_by(-2))

    def test_scaled_by_zero(self):
        self.assertEqual(Vector(0, 0), self.u.scaled_by(0))

    def test_scaled_by_fraction(self):
        self.assertEqual(Vector(0.5, 1), self.u.scaled_by(0.5))

    def test_opposite(self):
        self.assertEqual(Vector(-1, -2), self.u.opposite())

    def test_opposite_added_gives_zero(self):
        self.assertEqual(Vector(0, 0), self.u + self.u.opposite())

    # ---- norm / normalization --------------------------------------

    def test_norm(self):
        self.assertAlmostEqual(5, Vector(3, 4).norm)

    def test_norm_of_zero_vector(self):
        self.assertAlmostEqual(0, Vector(0, 0).norm)

    def test_norm_ignores_sign(self):
        self.assertAlmostEqual(5, Vector(-3, -4).norm)

    def test_is_normal_true(self):
        self.assertTrue(Vector(1, 0).is_normal)
        self.assertTrue(Vector(0.6, 0.8).is_normal)

    def test_is_normal_false(self):
        self.assertFalse(Vector(1, 1).is_normal)
        self.assertFalse(Vector(0, 0).is_normal)

    def test_normalized(self):
        self.assertEqual(Vector(0.6, 0.8), Vector(3, 4).normalized())

    def test_normalized_has_unit_norm(self):
        self.assertTrue(self.v.normalized().is_normal)

    def test_normalized_keeps_direction(self):
        self.assertTrue(self.v.is_parallel_to(self.v.normalized()))

    def test_normalized_zero_vector_raises(self):
        with self.assertRaises(ZeroDivisionError):
            Vector(0, 0).normalized()

    def test_with_length(self):
        result = Vector(3, 4).with_length(10)
        self.assertEqual(Vector(6, 8), result)
        self.assertAlmostEqual(10, result.norm)

    def test_with_length_negative_flips_direction(self):
        self.assertEqual(Vector(-3, -4), Vector(3, 4).with_length(-5))

    # ---- dot / cross / projection ----------------------------------

    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_dot_product_is_commutative(self):
        self.assertAlmostEqual(self.u.dot(self.v), self.v.dot(self.u))

    def test_dot_product_with_self_is_norm_squared(self):
        self.assertAlmostEqual(self.v.norm ** 2, self.v.dot(self.v))

    def test_dot_product_of_perpendicular_vectors_is_zero(self):
        self.assertAlmostEqual(0, Vector(1, 0).dot(Vector(0, 5)))

    def test_cross_product(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross_product_is_anticommutative(self):
        self.assertAlmostEqual(self.u.cross(self.v), -self.v.cross(self.u))

    def test_cross_product_with_self_is_zero(self):
        self.assertAlmostEqual(0, self.u.cross(self.u))

    def test_cross_product_sign_follows_orientation(self):
        self.assertGreater(Vector(1, 0).cross(Vector(0, 1)), 0)
        self.assertLess(Vector(0, 1).cross(Vector(1, 0)), 0)

    def test_projection_over_axis(self):
        self.assertAlmostEqual(3, Vector(3, 4).projection_over(Vector(1, 0)))

    def test_projection_over_non_unit_direction(self):
        # Direction length must not affect the result.
        self.assertAlmostEqual(3, Vector(3, 4).projection_over(Vector(10, 0)))

    def test_projection_over_opposite_direction_is_negative(self):
        self.assertAlmostEqual(-3, Vector(3, 4).projection_over(Vector(-1, 0)))

    def test_projection_over_perpendicular_direction_is_zero(self):
        self.assertAlmostEqual(0, Vector(3, 0).projection_over(Vector(0, 2)))

    # ---- parallel / perpendicular ----------------------------------

    def test_are_parallel(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_are_parallel_scaled(self):
        self.assertTrue(self.u.is_parallel_to(self.u.scaled_by(-3.5)))

    def test_are_not_parallel(self):
        self.assertFalse(self.u.is_parallel_to(self.v))

    def test_zero_vector_is_parallel_to_anything(self):
        self.assertTrue(Vector(0, 0).is_parallel_to(self.u))

    def test_are_perpendicular(self):
        perp = Vector(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(perp))

    def test_are_not_perpendicular(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))

    def test_axes_are_perpendicular(self):
        self.assertTrue(Vector(1, 0).is_perpendicular_to(Vector(0, 1)))

    # ---- angles -----------------------------------------------------

    def test_angle_value_to_right_angle(self):
        self.assertAlmostEqual(math.pi / 2, Vector(1, 0).angle_value_to(Vector(0, 1)))

    def test_angle_value_to_same_direction(self):
        self.assertAlmostEqual(0, Vector(1, 1).angle_value_to(Vector(2, 2)), places=6)

    def test_angle_value_to_opposite_direction(self):
        self.assertAlmostEqual(math.pi, Vector(1, 0).angle_value_to(Vector(-1, 0)))

    def test_angle_value_to_45_degrees(self):
        self.assertAlmostEqual(math.pi / 4, Vector(1, 0).angle_value_to(Vector(1, 1)))

    def test_angle_value_is_always_non_negative(self):
        self.assertGreaterEqual(Vector(0, 1).angle_value_to(Vector(1, 0)), 0)

    def test_angle_to_counterclockwise_is_positive(self):
        self.assertAlmostEqual(math.pi / 2, Vector(1, 0).angle_to(Vector(0, 1)))

    def test_angle_to_clockwise_is_negative(self):
        self.assertAlmostEqual(-math.pi / 2, Vector(0, 1).angle_to(Vector(1, 0)))

    def test_angle_to_is_antisymmetric(self):
        self.assertAlmostEqual(self.u.angle_to(self.v), -self.v.angle_to(self.u))

    # ---- rotation / perpendicular ----------------------------------

    def test_rotated_radians_quarter_turn(self):
        self.assertEqual(Vector(0, 1), Vector(1, 0).rotated_radians(math.pi / 2))

    def test_rotated_radians_half_turn(self):
        self.assertEqual(Vector(-1, -2), self.u.rotated_radians(math.pi))

    def test_rotated_radians_negative_angle(self):
        self.assertEqual(Vector(0, -1), Vector(1, 0).rotated_radians(-math.pi / 2))

    def test_rotated_radians_zero(self):
        self.assertEqual(self.u, self.u.rotated_radians(0))

    def test_rotated_radians_full_turn(self):
        self.assertEqual(self.u, self.u.rotated_radians(2 * math.pi))

    def test_rotated_radians_preserves_norm(self):
        self.assertAlmostEqual(self.v.norm, self.v.rotated_radians(1.234).norm)

    def test_rotated_radians_matches_angle_to(self):
        angle = 0.7
        rotated = self.u.rotated_radians(angle)
        self.assertAlmostEqual(angle, self.u.angle_to(rotated))

    def test_perpendicular(self):
        self.assertEqual(Vector(-2, 1), self.u.perpendicular())

    def test_perpendicular_is_perpendicular(self):
        self.assertTrue(self.v.is_perpendicular_to(self.v.perpendicular()))

    def test_perpendicular_preserves_norm(self):
        self.assertAlmostEqual(self.v.norm, self.v.perpendicular().norm)

    def test_perpendicular_is_quarter_turn_counterclockwise(self):
        self.assertEqual(self.u.rotated_radians(math.pi / 2), self.u.perpendicular())

    # ---- sine / cosine ---------------------------------------------

    def test_sine(self):
        self.assertAlmostEqual(0.8, Vector(3, 4).sine)

    def test_cosine(self):
        self.assertAlmostEqual(0.6, Vector(3, 4).cosine)

    def test_sine_and_cosine_of_axes(self):
        self.assertAlmostEqual(0, Vector(5, 0).sine)
        self.assertAlmostEqual(1, Vector(5, 0).cosine)
        self.assertAlmostEqual(1, Vector(0, 5).sine)
        self.assertAlmostEqual(0, Vector(0, 5).cosine)

    def test_sine_squared_plus_cosine_squared_is_one(self):
        self.assertAlmostEqual(1, self.v.sine ** 2 + self.v.cosine ** 2)

    # ---- equality / str --------------------------------------------

    def test_equal_vectors(self):
        self.assertEqual(Vector(1, 2), Vector(1, 2))

    def test_equal_to_itself(self):
        self.assertEqual(self.u, self.u)

    def test_equal_within_tolerance(self):
        self.assertEqual(Vector(1, 2), Vector(1 + 1e-12, 2 - 1e-12))

    def test_not_equal_different_components(self):
        self.assertNotEqual(Vector(1, 2), Vector(1, 3))
        self.assertNotEqual(Vector(1, 2), Vector(2, 2))

    def test_not_equal_to_other_types(self):
        self.assertNotEqual(Vector(1, 2), (1, 2))
        self.assertNotEqual(Vector(1, 2), None)

    def test_str(self):
        self.assertEqual('(3, 4) with norm 5.0', str(Vector(3, 4)))


if __name__ == '__main__':
    unittest.main()