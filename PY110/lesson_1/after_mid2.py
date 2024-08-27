'''As seen in the previous exercise, the time of day can be 
represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.'''

'''P:
in: string: time of day '##:##' 24 hr format
out: int: number of minutes before / after midnight, range (0,1440)
e:
- dont use datetime module
- 24hr format
- 2 functions: before midnight, after_midnight
- max min in day: 1440, min returned must be within that range (no negatives)
i:
?'s:
'''

'''e:
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
'''

'''d:
convert hours to min
add hour_min + min = minutes_passed
if before midnight: MAX_MIN-1440 - minutes_passed
if after midnight : minutes_passed
hr = slice(0,2) min = slice(3, 5) -> coerce to int to use

'''

'''a:
1. take in str input: time '##:##'
2. 2 functions:
  1. after_mid(str):
    2. calc total minutes of time:
        - hour_min = str(0,2)
        - min_min = str(3:5)
        - total_min = int(hour_min + min_min)
    3. return total_min
    1. before mid(str):
    2. calc total minutes of time: -- call after_mid()
        - hour_min = str(0,2)
        - min_min = str(3:5)
        - total_min = int(hour_min + min_min)
    3. calc time before midnight:
        - min_before_mid = MAX_MIN-1440 - total_min
    4. return min_before_mid

'''
MINUTES_PER_DAY = 1440 # 60 min * 24 hrs
MINUTES_PER_HR = 60

def after_midnight(time_str):
    hour_minutes = int(time_str[:2]) * MINUTES_PER_HR
    min_minutes = int(time_str[3:])
    ''' % MINUTES_PER_DAY for when total_mins == MINUTES_PER_DAY -> reassigned to 0
    rather than if statement: if total_time == MINUTES_PER_DAY ...'''
    total_minutes = (hour_minutes + min_minutes) % MINUTES_PER_DAY

    return total_minutes 

def before_midnight(time_str):
    total_minutes = after_midnight(time_str)
    remaining_time = (MINUTES_PER_DAY - total_minutes) % MINUTES_PER_DAY

    return remaining_time

print(after_midnight("00:00") == 0)     # True
print(after_midnight("12:34") == 754)   # True
print(after_midnight("24:00")== 0)     # True
print(before_midnight("24:00") == 0)    # True
print(before_midnight("00:00")== 0)    # True
print(before_midnight("12:34") == 686)  # True