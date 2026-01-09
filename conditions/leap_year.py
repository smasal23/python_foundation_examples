# Let "A" be a year, write a program to check whether this year is a leap year or not. Print "Y" if its a leap year and "N" if its a common year.
A = int(input())

if (A % 400 == 0) or (A % 4 == 0 and A % 100 != 0): # Need to be remember logic thoroughly.
    print("Y")
else:
    print("N")