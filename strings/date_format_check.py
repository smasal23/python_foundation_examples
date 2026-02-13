# Accept a string and find if it is of date format 'dd/mm/yy'.

from datetime import datetime

date_str = input().strip()

try:
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    print("Valid")
except:
    print("Not valid")
