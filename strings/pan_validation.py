# Write a program to check whether the given string is a pan card format or not. if its pan card format print Yes otherwise No

import re
pan = input().strip()
pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.fullmatch(pattern, pan):
    print("Yes")
else:
    print("No")