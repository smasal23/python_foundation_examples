# Write a Program to Clear the Rightmost Set Bit of a Number.

N2 = int(input())

result = N2 & (N2 - 1)  # Subtracting 1 flips the rightmost 1 to 0; ANDing (&) removes that bit

print(result)