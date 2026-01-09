# Write a code get an integer number as input and print the sum of the digits.

N = int(input())

def sum_of_digits(N):
    digits = str(abs(N))
    return sum(int(i) for i in digits)

print(sum_of_digits(N))