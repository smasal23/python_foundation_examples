# Write a program to get a string as input and reverse the string without using temporary variable.

A = input()
lst = list(A)
rev = []

for i in range(len(lst) - 1, -1, -1):
    print(lst[i])

print("".join(rev))