import unittest
from Classify_triangle import Classify_triangle

class TestTriangleClassification (unittest.TestCase):

    def test_equilateral_triangle(self):
        # Arrange
        side_a, side_b, side_c = 5, 5, 5
        expected_result = "Equilateral triangle"
        
        # Act
        result = Classify_triangle(side_a, side_b, side_c)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_isosceles_triangle(self):
        # Arrange
        side_a, side_b, side_c = 5, 6, 4
        expected_result = "Isosceles triangle"
        
        # Act
        result = Classify_triangle(side_a, side_b, side_c)
        
        # Assert
        self.assertEqual(result, expected_result)
        
    def test_scalene_triangle(self):
        # Arrange
        side_a, side_b, side_c = 5, 6, 7
        expected_result = "Scalene triangle"
        
        # Act
        result = Classify_triangle(side_a, side_b, side_c)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_not_a_triangle(self):
        # Arrange
        side_a, side_b, side_c = 1, 2, 3
        expected_result = "Not a triangle"
        
        # Act
        result = Classify_triangle(side_a, side_b, side_c)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_zero_sides(self):
        # Arrange
        side_a, side_b, side_c = 0, 0, 0
        expected_result = "Not a triangle"
        
        # Act
        result = Classify_triangle(side_a, side_b, side_c)
        
        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

#Ilyas Oubousken








