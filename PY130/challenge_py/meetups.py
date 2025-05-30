from datetime import date

class Meetup():
    VALID_DESCRIPTOR = {
        "first": 0, 
        "second": 1, 
        "third": 2, 
        "fourth": 3, 
        "fifth": 4, 
        "last": -1
        }
    VALID_DAY_OF_WEEK = [
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
        ]
    VALID_TEENTH = [13, 14, 15, 16, 17, 18, 19]
    MONTH_WITH_30_DAYS = [4, 6, 9, 11]

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def day(self, day_of_week, descriptor):
        month_dict = self._get_month_data()
        day_of_week_data = month_dict[day_of_week]

        if descriptor == "teenth":
            for num in day_of_week_data:
                if num in Meetup.VALID_TEENTH:
                    return date(self.year, self.month, num)

        descriptor_length = Meetup.VALID_DESCRIPTOR[descriptor]
        if descriptor_length > len(day_of_week_data)- 1:
            return None

        date_num = day_of_week_data[descriptor_length]

        return date(self.year, self.month, date_num)

    def _get_month_data(self):
        current_month = {day: [] for day in Meetup.VALID_DAY_OF_WEEK}
        first_weekday = self.first_weekday_of_month()
        days_in_month = list(range(1, self.total_days_in_month() + 1))
        last_day_of_month = self.total_days_in_month()

        start_adding_dates = False
        day_count = 0
        while True:
            for day, lst in current_month.items():
                if day == first_weekday:
                    # don't start adding date numbers until
                    # we are a first_weekday
                    start_adding_dates = True

                if start_adding_dates:
                    lst.append(days_in_month[day_count])
                    day_count += 1
                    if day_count == last_day_of_month:
                        # current_month dict is filled out
                        return current_month

    def first_weekday_of_month(self):
        first_day_of_month = date(self.year, self.month, 1)
        return Meetup.VALID_DAY_OF_WEEK[date.weekday(first_day_of_month)]

    def total_days_in_month(self):
        if self.month == 2:
            if self.is_leap_year():
                total_days_in_month = 29
            else:
                total_days_in_month = 28

        elif self.month in Meetup.MONTH_WITH_30_DAYS:
            total_days_in_month = 30

        else:
            total_days_in_month = 31

        return total_days_in_month

    def is_leap_year(self):
        return (
            (self.year % 4 == 0) and
            (not (self.year % 100 == 0) or (self.year % 400 == 0))
            )

"""Meetups PEDAC:
P:
    -in: 2 args: 
        -month number and 
        - year number
    -out:
        - date object when day instance is called
    -e:
        -construct objects that representa meet up date
        - object should be able to determine exact date 
            of the meeting in the specified month and year
        - Meetup class:
            - takes in month number (1-12) and year (e.g 2025)
            - day() instance method, returns the
              date(year, month_num, date_num)
                - takes in 2 args: day_of_week  and descriptor
                    -descriptor (1st-fifth, + last, and teenth)
                        -teenth = it guaranteed that 
                        each day of the week (Monday, Tuesday, ...) 
                        will have exactly one date that is the 
                        "teenth" of that day in 
                        every month. That is, every month 
                        has exactly one "teenth" 
                        Monday, one "teenth" Tuesday, etc. 
                        The fifth day of the month 
                        may not happen every month, but some 
                        meetup groups like that
                        irregularity.
                - return the date(year,month, date) # need to find date
                - else None if no applicapable date descriptor/month/year
    -i:
        - date method from datetime used to represent full 
        date (year, month_num, date_num)

    -?:
    datetime.date: class datetime.date(year, month, day)
        All arguments are required. Arguments must be
          integers, in the following ranges:
        MINYEAR <= year <= MAXYEAR
        1 <= month <= 12
        1 <= day <= number of days in the given month and year
        If an argument outside those ranges is given, 
        ValueError is raised.
    - how to determine day_num:
        -can i get a nested list that stores (weekday and
         its corresponding number) 
        for each day in the month and year that is passed?


    - date.weekday()
        Return the day of the week as an integer, where Monday is 0 
        and Sunday is 6. For example, date(2002, 12, 4).weekday() == 2,
          a Wednesday. See also isoweekday().
Other constructors, all class methods:
E: test_meetups.py
D:
"""