'''The time of day can be represented as the number of 
minutes before or after midnight. If the number of 
minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time 
is before midnight.

Write a function that takes a time using 
this minute-based format and returns the 
time of day in 24-hour format (hh:mm). Your 
function should work with any integer input.

You may not use Python's datetime module.'''

MIN_IN_HOUR = 60
HOURS_IN_DAY = 24
MAX_HRS = 23

def add_zero(time):
  for idx, num in enumerate(time):
        if num < 10:
            time[idx] = '0'+ str(num)
  return time
  
def time_of_day(min_to_add):
    hours = min_to_add // MIN_IN_HOUR
    minutes = min_to_add % MIN_IN_HOUR

  # CONVERT HRS TO 24 HR TIME
    if hours > MAX_HRS: # > 24 HRS
        hours = hours // HOURS_IN_DAY
        
    if hours < 0: # NEGATIVE HOURS
        hours = HOURS_IN_DAY + hours
        if hours < -MAX_HRS: # < -24 HRS
            hours = int(abs(hours / HOURS_IN_DAY)) # imprecision with using //
            
  # FORMAT DIGITS LESS THAN 10 
    time = add_zero([hours, minutes])
    return f'{time[0]}:{time[1]}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True


''' # LS WAY:
1. take in integer of minutes before or after midnight
2. find total minutes: integer_of_min % 1440
3. convert total_minutes to hour: total_minutes // 60
4. convert total_minutes to minutes: total_minutes % 60
5. format to f{#:02d}
6. return time as string: '{hr}:{mn}'

MIN_IN_HR = 60
MIN_IN_DAY = MIN_IN_HR * 24

def time_of_day(inty):
  total_minutes = inty % MIN_IN_DAY
  hours = total_minutes // MIN_IN_HR
  minutes = total_minutes % MIN_IN_HR
  return f'{hours:02d}:{minutes:02d}'
'''