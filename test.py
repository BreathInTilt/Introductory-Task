import unittest
from Geometry import Circle, Triangle, Shape, compute_area
from math import pi


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_triangle_is_right_angled_true(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_triangle_is_right_angled_false(self):
        triangle = Triangle(4, 5, 6)
        self.assertFalse(triangle.is_right_angled())

    def test_circle_area_with_zero_radius(self):
        circle = Circle(0)
        self.assertEqual(circle.area(), 0)

    def test_circle_area_with_negative_radius(self):
        circle = Circle(-5)
        self.assertRaises(ValueError, circle.area)

    def test_triangle_area_with_zero_sides(self):
        triangle = Triangle(0, 0, 0)
        self.assertRaises(ValueError, triangle.area)

    def test_triangle_area_with_negative_sides(self):
        triangle = Triangle(-3, 4, 5)
        self.assertRaises(ValueError, triangle.area)

    def test_nonexistent_triangle(self):
        triangle = Triangle(1, 2, 3)
        self.assertRaises(ValueError, triangle.area)

    def test_almost_right_angled_triangle(self):
        triangle = Triangle(5, 5, 7)
        self.assertFalse(triangle.is_right_angled())

    def test_compute_area_with_unknown_shape(self):
        class Square(Shape):
            def __init__(self, side_length):
                self.side_length = side_length

            def area(self):
                return self.side_length ** 2

        square = Square(4)
        self.assertEqual(compute_area(square), 16)


if __name__ == "__main__":
    unittest.main()
