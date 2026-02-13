# Write a program takes in the number of terms and finds the sum of the sine series.

from math import sin, radians  # sin function requires radians for processing.
A, N1 = map(int, input().split())

result = sin(radians(A))

print(f"{result:.2f}")