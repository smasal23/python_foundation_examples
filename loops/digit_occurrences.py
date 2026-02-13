# num1 and num2 such that 0 <= num1 <= 99999999 and 0 <= num2 <=9.
# You have to find number of occurrences of input num2 in input num1.

num1 = int(input())
num2 = int(input())
# num1 = int(input())
# num2 = int(input())
# print(num1.count(num2)) - answer
def number_occurences(num1, num2):
    if num1 <= 0 or num1 >= 99999999:
        return "Invalid Num1"

    if num2 <= 0 or num2 > 9:
        return "Invalid Num2"

    return str(num1).count(str(num2))

print(number_occurences(num1, num2))