# Write a Program to Find ASCII Value of Character
char = input().strip()

if len(char) != 1:
    print("Error")
else:
    print(ord(char))