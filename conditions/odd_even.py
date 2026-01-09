# You are provided with a number check whether its odd or even.
# Print "Odd" or "Even" for the corresponding cases.
# Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

number = round(float(input()))

if number == 0:
    print("Zero")
elif number % 2 == 0:
    print("Even")
else:
    print("Odd")