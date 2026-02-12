# Given an integer N, find if it is divisible by 11
# N >= 1
# 1 <= No. of digits in N <= 1000

N = int(input())

if N < 1:
    print("Error")
elif N > 1000:
    print("Error")
else:
    if N % 11 == 0:
        print("YES")
    else:
        print("NO")