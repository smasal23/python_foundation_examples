# Write a code to get an integer N and print the digits of the integer.

N = int(input())

def print_digits(N):
    Digits = str(abs(N))
    return " ".join(Digits)

print(print_digits(N))