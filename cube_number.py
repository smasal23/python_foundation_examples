# You are given three numbers A, B & C. Print the largest amongst these three numbers.
A = float(input())
B = float(input())
C = float(input())

Largest = max(A, B, C)
# Had to include the conditional statement to satisfy both float and integers inputs simultaneously over all test cases.
if Largest.is_integer(): # Built_in python function to check if the number is integer.
    print(int(Largest))
else:
    print(Largest)