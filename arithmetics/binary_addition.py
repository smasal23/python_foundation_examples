# Write a program to add two numbers and converting the result to binary
N, M = map(int, input().split())

Output = N + M
Binary = ""

while Output > 0:
    Bin = Output % 2
    Binary = str(Bin) + Binary
    Output = Output // 2

print(Binary)