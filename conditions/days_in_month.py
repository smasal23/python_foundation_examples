# You will be provided with a number. Print the number of days in the month corresponding to that number.
# Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

number = input()

if not number.isdigit(): # Check whether input is in digits, if no print error and if yes convert into integer and then proceed.
    print("Error")
else:
    number = int(number)

def days_in_month(number):
    if number == 2:
        return 28
    elif number in [1,3,5,7,8,10,12]:
        return 31
    elif number in [4,6,9,11]:
        return 30
    else:
        return "Error"

print(days_in_month(number))