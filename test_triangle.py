import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Invalid")

    def test_negative_or_zero(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid")
        self.assertEqual(classify_triangle(-1, 2, 2), "Invalid")

if __name__ == "__main__":
    unittest.main()
