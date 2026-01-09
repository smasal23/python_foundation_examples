# The area of an equilateral triangle is ¼(√3a²) where "a" represents a side of the triangle.
# You are provided with the side "a". Find the area of the equilateral triangle.
from math import sqrt

a = float(input())

Area_of_triangle = 0.25 * sqrt(3) * (a ** 2)
print(round(Area_of_triangle, 2))