# Given a number N and array of N integers, print the sum between the smallest and largest number.
N = int(input())
arr = list(map(int, input().split()))

if len(arr) != N:
    print("Invalid Input")
else:
    print(min(arr) + max(arr))