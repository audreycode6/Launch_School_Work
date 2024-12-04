'''Some people believe that Fridays that fall on 
the 13th day of the month are unlucky days. Write a
function that takes a year as an argument and returns
the number of Friday the 13ths in that year. 
You may assume that the year is greater than 1752, 
which is when the United Kingdom adopted the modern Gregorian Calendar.
You may also assume that the same calendar will 
remain in use for the foreseeable future.
'''

'''P:
in: year as arg: int
out: int; # of Friday the 13ths in that year
e:
- year is greater than 1752
- use modern Gregorian Calendar to calculate
i:
?:
- how to use modern gregorian calendar to count # of fridays the 13ths
'''
import datetime

MONTHS = range(1, 13)
DAY = 13
FRIDAY = 4

def friday_the_13ths(year):
    friday_count = 0

    for month in MONTHS:
        date_format = datetime.date(year, month, DAY)
        if date_format.weekday() == FRIDAY:
            friday_count += 1

    return friday_count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True