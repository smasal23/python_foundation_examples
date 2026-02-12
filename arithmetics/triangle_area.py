# Given base(B) and height(H) of a triangle find its area.
B, H = map(int, input().split())
Max_N = 1000000

if B > Max_N or H > Max_N:
    raise ValueError("Input exceeds limit.")
else:
    Area = 0.5 * B *H

print(int(Area) if Area.is_integer() else Area)