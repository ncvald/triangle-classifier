import pytest
from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"

def test_scalene():
    assert classify_triangle(3, 4, 5) == "Scalene Right"  # Pythagorean triple

def test_invalid_negative():
    assert classify_triangle(-1, 2, 3) == "Invalid"

def test_invalid_triangle_inequality():
    assert classify_triangle(1, 2, 3) == "Invalid"

def test_isosceles_right():
    assert classify_triangle(1, 1, 2 ** 0.5) == "Isosceles Right"

def test_scalene_non_right():
    assert classify_triangle(2, 3, 4) == "Scalene"
