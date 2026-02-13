# Write a function to check if a number is a Fibonocci Prime.

N = int(input())

def is_prime():
    if N <= 1:
        return False
    else:
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                return False
    return True

def is_fibonacci():
    a = 0
    b = 1

    while b < N:
        a, b = b, a + b
    return b == N or N == 0

def fibonacci_prime(N):
    if is_prime() and is_fibonacci():
        print("Yes")
    else:
        print("No")

fibonacci_prime(N)