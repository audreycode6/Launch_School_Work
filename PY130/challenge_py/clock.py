"""Clock PEDAC:
P:
    -in:
    -out:
    -e:
        - create a clock independent of date
        - add and subtract minutes from the time
          represented by given CLock object
            -should not mutate clock objects when adding or subbing 
                -- create a new Clock object
                    --be able to add more than a day of time
                    - clock.at() +|- # (# = minutes)
                    - define __add__ method: 
                    - define __sub__ method:

        - 2 clocks thast represent same time shoild be equal to each other.
            - need to define an __eq__
        -cannot use date/time functionality just arithmentic operations
        - Clock class
            - at() class method: takes hour as 1st arg and min as 2nd arg
                ` returns string of time "00:00" format 
    -i:
        - 24:00 == "00:00"
    -?:
E: test_clock.py
D:
"""
class Clock():
    MINUTES_IN_HOUR = 60
    MAX_HOURS = 24
    MINUTES_IN_DAY = 1440

    def __init__(self, hour=0, minute=0):
        self._hours = hour
        self._minutes =  minute

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @classmethod
    def at(cls, hour=0, minute=0):
        return Clock(hour, minute)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, minutes_to_add):
        current_time_minutes = self._get_time_in_minutes()
        new_time = current_time_minutes + minutes_to_add

        new_hours = self._convert_to_24_hour(new_time) % Clock.MAX_HOURS
        new_minutes = self._get_remaining_minutes(new_time)

        return Clock(new_hours, new_minutes)

    def __sub__(self, minutes_to_sub):
        current_time_minutes = self._get_time_in_minutes()
        new_time = (
            (current_time_minutes - minutes_to_sub) % Clock.MINUTES_IN_DAY
            )

        new_hours = self._convert_to_24_hour(new_time)
        new_minutes = self._get_remaining_minutes(new_time)

        return Clock(new_hours, new_minutes)

    def _get_time_in_minutes(self):
        return (self.hours * Clock.MINUTES_IN_HOUR) + self.minutes

    def _convert_to_24_hour(self, new_time):
        return new_time // Clock.MINUTES_IN_HOUR

    def _get_remaining_minutes(self, new_time):
        return new_time % Clock.MINUTES_IN_HOUR

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return (
            self.hours == other.hours and
            self.minutes == other.minutes
            )