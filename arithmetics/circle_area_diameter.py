# Write a program, to find the area of a circle when the diameter is given . The input diameter is an integer and the output
# area should be a floating point variable with 2 point precision.
from math import pi
D = int(input())

Area = pi * ((D / 2) ** 2)

print(f"{Area:.2f}")