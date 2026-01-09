# You are provided with two numbers. Find and print the smaller number.
A_1, B = map(int, input().split())

if A_1 > B:
    print(B)
else:
    print(A_1)