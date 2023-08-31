#! python

import re, pyperclip

text = pyperclip.paste()
print(text)

detection = re.compile(r'(\d?\d)/(\d?\d)/(\d\d\d\d)')
dates = detection.search(text)

days, month, year = dates.groups()
days = int(days)
month = int(month)
year = int(year)

if month == 4 or 6 or 9 or 11:
    if not days<= 30:
        print(dates.group() + " is not valid date")
    else:
        print(dates.group() + " is a valid date")

elif month == 2:
    if year % 4 == 0:
        if not days<= 29:
            print(dates.group() + " is not valid date")
        else:
            print(dates.group() + " is valid date")
    
    else:
        if not days<=28:
            print(dates.group() + " is not valid date")
        else:
            print(dates.group() + " is valid date")

else:
    if not days<=31:
        print(dates.group() + "is not vaild date")
    else:
        print(dates.group() + " is valid date")
