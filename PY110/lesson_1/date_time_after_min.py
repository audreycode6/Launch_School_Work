'''
The time of day can be represented as the number of 
minutes before or after midnight. If the number of 
minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time 
is before midnight.

Write a function that takes a time using 
this minute-based format and returns the 
time of day in 24-hour format (hh:mm). Your 
function should work with any integer input.

How would you approach this problem if you could use Python's 
datetime class? Suppose you also needed to consider 
the day of the week? (Assume that delta_minutes is the 
number of minutes before or after midnight between 
Saturday and Sunday; in such a function, a delta_minutes 
value of -4231 would need to produce a return value of Thursday 01:29.)
'''

# LEFT OFF HERE, do datetime way, continue easy3 problems
'''P:
in: int, positive / negative
out: string, time ('##:##') hour and minutes before/since midnight, 24 hr time
e: 
- calculate what time it is based on int of minutes before/after midnight
- negative int = time before midnight
- positive int = time after midnight
- Assume that delta_minutes is the 
number of minutes before or after midnight between 
Saturday and Sunday; in such a function, a delta_minutes 
value of -4231 would need to produce a return value of Thursday 01:29.
i:
- 24 hr time, 1440 min in day, 60 min in hr
?'s:
'''

'''e:
print(time_of_day(-4231) == "Thursday 01:29")    # True
'''

'''algo:
1. take in int of min before or after midnight
2. find day of week: 
    -need list: DAYS_OF_WEEK = ['Sunday', 'Monday', ... 'Saturday']
    - weekday_list_index = int_input // MIN_IN_DAY-1440 % DAYS_IN_WEEK-7
    - day = DAYS_OF_WEEK[weekday_list_index]
3. convert day_minutes to 24hr time: hr, min
    - day_minutes = int_input % MIN_IN_DAY-1440
    - use datetime module: time.gmtime(secs_in_day)
        - convert day_minutes to secs: secs_in_day = day_minutes * SECS_IN_MIN-60
        - returns struct_time object (tm_year=1970, tm_mon=1, tm_mday=1, 
     tm_hour=13, tm_min=20, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
4. format time object to 24hr time string: 'hr:mn'
    - use struct_time_object
    - time.strftime(str_format, time_obj)
    - "%H:%M" 
        - %H gets hour from struct_time_obj
        - %M gets min from struct_time_obj
        - time_obj is the struct_time object references to get data
5. return formated weekday time: 'weekday ##:##'
'''

import time

DAYS_OF_THE_WEEK = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday'
]
NUM_DAYS_OF_WEEK = 7
MIN_IN_DAY = 1440
SECS_IN_MIN = 60

def time_of_day(int_min):
  weekday_index = int_min // MIN_IN_DAY % NUM_DAYS_OF_WEEK
  day_of_the_week = DAYS_OF_THE_WEEK[weekday_index]

  day_minutes = int_min % MIN_IN_DAY
  time_obj = time.gmtime(day_minutes * SECS_IN_MIN)

  formatted_time = time.strftime('%H:%M', time_obj)

  return f'{day_of_the_week} {formatted_time}'  # formatted time


print(time_of_day(-4231) == "Thursday 01:29")    # True
print(time_of_day(0))  # == "00:00")        # True
print(time_of_day(-3))  # == "23:57")       # True
print(time_of_day(35))  #== "00:35")       # True
print(time_of_day(-1437))  #== "00:03")    # True
print(time_of_day(3000))  # == "02:00")     # True
print(time_of_day(800))  # == "13:20")      # True