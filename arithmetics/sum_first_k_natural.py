# Write a program to print the sum of the first K natural numbers.
K = int(input())

def sum_natural(K):
    if K > 100000:
        return "Input Size : n <= 100000"

    total = 0                               # or just return K * (K + 1) // 2 instead of the loop.
    for i in range(1, K + 1):
        total += i
    return total

print(sum_natural(K))