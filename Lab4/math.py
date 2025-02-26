import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
print("Output radian:", round(degree_to_radian(degree), 6))


def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = 5
base1 = 5
base2 = 6
print("Expected Output:", trapezoid_area(height, base1, base2))


def regular_polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25
print("The area of the polygon is:", round(regular_polygon_area(sides, length), 2))


def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
print("Expected Output:", parallelogram_area(base, height))
