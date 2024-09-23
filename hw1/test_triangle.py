
import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle")
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles triangle")
    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle and Right triangle")
    
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene triangle and Right triangle")


# Run the tests
if __name__ == "__main__":
    unittest.main()
