#! python

import os, re , shutil 

american_dates =re.compile(r'''
                            ^(.*?) #text before
                            ((0|1)?\d) #Months
                           (-|/)
                           ((0|1|2|3)?\d) #Months
                           (-|/)
                           ((19|20)\d\d) #years
                           (.*?)$ #othertext
                           ''', re.VERBOSE)
datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)
british_date = []

files = os.listdir(r'C:\Users\Anjal\Desktop\Dates')

for dates in files:
    searching = american_dates.search(dates)

    if searching == None:
        continue

    text = searching.group(1)
    month =searching.group(2)  + searching.group(4)
    days = searching.group(5) + searching.group(7)
    year = searching.group(8)
    text2 =searching.group(10)

    inbritish = text + days + month + year + text2
    british_date.append(inbritish)
    americanfile = searching.group(0)



shutil.move(r"C:\Users\Anjal\Desktop\Dates\%s"%(americanfile) ,  r"C:\Users\Anjal\Desktop\Dates\%s"%(inbritish) )