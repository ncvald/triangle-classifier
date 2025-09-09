def classify_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    
    result = ""

    if a == b ==c:
        result = "equilateral"
    elif a == b or b ==c or a ==c:
        result = "isosceles"

    else:
        result = "scalene"

    sides = sorted([a,b,c])
    if sides [0]**2 + sides[1]**2== sides [2]**2:
        result += "right"

        return result
    