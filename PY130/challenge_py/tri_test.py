import unittest
from easy_tri import Triangle

class TestTriangle(unittest.TestCase):
    # @unittest.skip
    def test_equilateral_equal_sides(self):
        triangle = Triangle(2, 2, 2)
        self.assertEqual(triangle.kind, "equilateral")

    # @unittest.skip
    def test_larger_equilateral_equal_sides(self):
        triangle = Triangle(10, 10, 10)
        self.assertEqual(triangle.kind, "equilateral")

    # @unittest.skip
    def test_isosceles_last_two_sides_equal(self):
        triangle = Triangle(3, 4, 4)
        self.assertEqual(triangle.kind, "isosceles")

    # @unittest.skip
    def test_isosceles_first_last_sides_equal(self):
        triangle = Triangle(4, 3, 4)
        self.assertEqual(triangle.kind, "isosceles")

    # @unittest.skip
    def test_isosceles_first_two_sides_equal(self):
        triangle = Triangle(4, 4, 3)
        self.assertEqual(triangle.kind, "isosceles")

    # @unittest.skip
    def test_isosceles_exactly_two_sides_equal(self):
        triangle = Triangle(10, 10, 2)
        self.assertEqual(triangle.kind, "isosceles")

    # @unittest.skip
    def test_scalene_no_equal_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.kind, "scalene")

    # @unittest.skip
    def test_scalene_larger_no_equal_sides(self):
        triangle = Triangle(10, 11, 12)
        self.assertEqual(triangle.kind, "scalene")

    # @unittest.skip
    def test_scalene_no_equal_sides_descending(self):
        triangle = Triangle(5, 4, 2)
        self.assertEqual(triangle.kind, "scalene")

    # @unittest.skip
    def test_small_triangles_are_legal(self):
        triangle = Triangle(0.4, 0.6, 0.3)
        self.assertEqual(triangle.kind, "scalene")

    # @unittest.skip
    def test_no_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    # @unittest.skip
    def test_negative_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, -5)

    # @unittest.skip
    def test_size_inequality_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    # @unittest.skip
    def test_size_inequality_is_illegal_2(self):
        with self.assertRaises(ValueError):
            Triangle(7, 3, 2)

    # @unittest.skip
    def test_size_inequality_is_illegal_3(self):
        with self.assertRaises(ValueError):
            Triangle(10, 1, 3)

    # @unittest.skip
    def test_size_inequality_is_illegal_4(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 2)

if __name__ == "__main__":
    unittest.main()