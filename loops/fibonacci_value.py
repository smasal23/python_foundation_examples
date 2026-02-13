# For this question, you will write a program that generates values from the Fibonacci sequence. The Fibonnaci sequence is
# recursively defined by:Fn = Fn - 1 + Fn - 2Using the following seed values:F0 = 0, F1 = 1Given a number n,
# print the nth value of the Fibonacci sequence.

n = int(input())

def fib_seq(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

print(fib_seq(n))
