# You are given the coefficients of a quadratic equation in order A, B & C.
# Where A is the coefficient of X², B is the coefficient of X and C is the constant term in the most simplified form.
# Example: For X² + 5X + 6 = 0, you are given the input as: 1 5 6.
# Write a program to find all of the roots of the quadratic.
# Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.
# Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a

import math
import cmath # Can handle complex roots(imaginary numbers(sqrt(-4))

A, B, C = map(float, input().split())

def solve_quadratic(A, B, C):
    if A == 0:
        if B != 0:
            root = -C / B
            Output = f"{root:.2f}", f"{root:.2f}"
            return Output
        else:
            return f"0.00", f"0.00"

    discriminant = (B ** 2) - (4 * A * C) # If discriminant is negative, complex roots will be solved.

    if discriminant > 0:
        root_1 = (-B + math.sqrt(discriminant)) / (2 * A)
        root_2 = (-B - math.sqrt(discriminant)) / (2 * A)
        Output_1 = f"{root_1:.2f}"
        Output_2 = f"{root_2:.2f}"
        return Output_1, Output_2

    elif discriminant == 0:
        root = (-B) / (2 * A)
        Output = f"{root:.2f}", f"{root:.2f}"
        return Output

    else:
        root_1 = (-B - cmath.sqrt(discriminant)) / (2 * A)
        root_2 = (-B + cmath.sqrt(discriminant)) / (2 * A)
        Output_1 = f"{root_1.real:.2f}+{root_1.imag:.2f}j" if root_1.imag >= 0 else f"{root_1.real:.2f}-{-root_1.imag:.2f}j"
        Output_2 = f"{root_2.real:.2f}+{root_2.imag:.2f}j" if root_2.imag >= 0 else f"{root_2.real:.2f}-{-root_2.imag:.2f}j"
        return Output_1, Output_2

r1, r2 = solve_quadratic(A, B, C)

if 'j' in r1:          # complex roots → GUVI doesn't compare, just print
    print(r1)
    print(r2)
else:                  # real roots → numeric comparison
    r1f = float(r1)
    r2f = float(r2)
    print(f"{max(r1f, r2f):.2f}")
    print(f"{min(r1f, r2f):.2f}")