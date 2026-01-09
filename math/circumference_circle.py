# You are provided with the radius of a circle "A". Find the length of its circumference. Note:In case the output is in decimal,roundoff to 2nd decimal place.
# In case the input is a negative number, print "Error".

import math

A = float(input())

def Cal_Circumference(A):
    if A >= 0:
        Circumference = 2 * math.pi * A
        return f"{Circumference:.2f}"
    else:
        return "Error"

print(Cal_Circumference(A))