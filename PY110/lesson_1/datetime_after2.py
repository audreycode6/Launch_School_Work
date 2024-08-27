'''How would these functions change if you could use the Python's datetime.datetime class?'''
MINUTES_PER_DAY = 1440 # 60 min * 24 hrs
MINUTES_PER_HR = 60
from datetime import datetime

def after_midnight(time_str):
    '''datetime.strptime() doesn't recognize "24:00" as a valid time.
    the valid range for hours is 00 to 23 
    + no more need for: total_minutes % MINUTES_PER_DAY '''
    if time_str == "24:00":
        time_str = "00:00"

    time_obj = datetime.strptime(time_str, "%H:%M") # e.g. 1900-01-01 00:00:00
    total_minutes = (time_obj.hour * MINUTES_PER_HR) + time_obj.minute

    return total_minutes

def before_midnight(time_str):
    total_minutes = after_midnight(time_str)

    return (MINUTES_PER_DAY - total_minutes) % MINUTES_PER_DAY

# Tests
print(after_midnight("00:00"))#  == 0)     # True
print(after_midnight("12:34"))# == 754)   # True
print(after_midnight("24:00"))#== 0)     # True
print(before_midnight("24:00"))# == 0)    # True
print(before_midnight("00:00") )#== 0)    # True
print(before_midnight("12:34"))# == 686)  # True