from datetime import datetime

def get_hour_of_day():
    date = datetime.now()
    return date.hour

hour_of_day = get_hour_of_day()
print(hour_of_day)