# Write a Program to check whether the given number is prime or not.
from math import sqrt
N = int(input())

if N <= 1:
    print("NOT PRIME")
else:
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print("PRIME")
    else:
        print("NOT PRIME")