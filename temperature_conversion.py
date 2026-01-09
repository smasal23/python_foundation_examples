# You are given with a number A i.e. the temperature in Celsius.
# Write a program to convert this into Fahrenheit. Note: In case of decimal values, round-off to two decimal places.

A = float(input())

def conversion(A):
    fahrenheit = (A * (9 / 5)) + 32
    return f"{fahrenheit:.2f}"

print(conversion(A))