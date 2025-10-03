"""
triangle.py
A program to classify triangles by side lengths.
"""

def classify_triangle(a, b, c):
    """
    Classify a triangle given three side lengths.

    Returns:
        - "Equilateral" if all three sides are equal
        - "Isosceles" if exactly two sides are equal
        - "Scalene" if all three sides are different
        - "Invalid" if the side lengths cannot form a valid triangle
        - Appends " Right" if it is also a right triangle
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    result = ""

    if a == b == c:
        result = "Equilateral"
    elif a == b or b == c or a == c:
        result = "Isosceles"
    else:
        result = "Scalene"

    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        result += " Right"

    return result

