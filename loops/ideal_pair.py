# Ideal Pairs are hard to find, especially in numbers. Two numbers are said to be a pair if the sum of the factors of one number
# (excluding the number itself) is equal to the other number and vice versa. The numbers are lost and seeking your help find their
# pair back. Your task is to help the numbers find its pair back.

N = int(input())

def ideal_pair(N):
    if N <= 1:
        return 0

    total = 1
    i = 2

    while i * i <= N:
        if N % i == 0:
            total += i
            if  i != N // i:
                total += N // i
        i += 1

    return total

output = ideal_pair(N)
if output != N and ideal_pair(output) == N:
    print(output)
else:
    print('-1')