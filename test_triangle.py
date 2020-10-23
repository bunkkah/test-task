from main import Triangle
import pytest


class TestAreaCalculation:
    def test_zero_numbers(self):
        triangle = Triangle((0, 0), (0, 0), (0, 0))
        assert triangle.area_calculation() == 0, "area_calculation works wrong with zero numbers"

    def test_positive_numbers(self):
        triangle = Triangle((5, 3), (2, 4), (1, 8))
        assert triangle.area_calculation() == 5.5, "area_calculation works wrong with positive numbers"

    def test_float_numbers(self):
        triangle = Triangle((5.5, 2.1), (8.4, 3.9), (6.5, 1.1))
        assert triangle.area_calculation() == 2.3500000000000005, "area_calculation works wrong with float numbers"

    def test_negative_numbers(self):
        triangle = Triangle((-5, -8), (-1, -4), (-6, -1))
        assert triangle.area_calculation() == 16.0, "area_calculation works wrong with negative numbers"

    def test_mixed_numbers(self):
        triangle = Triangle((1.1, -5), (0, 0), (123456789, 123456789))
        assert triangle.area_calculation() == 376543206.45, "area_calculation works wrong with mixed numbers"
