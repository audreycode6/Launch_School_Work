'''We have a list of events and want to check
whether a specific date is available (i.e., 
no events planned for that date). However, 
the function always returns the wrong value.
'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}
''' original debug: the return values should be swapped
def is_date_available(date):
    if date in events: # in is just checking it exists in list 
        # so we actually want to return False bc that means 
        # the date is unavailable and vice versa if not in list than it is available
        return True

    return False

print(is_date_available("2023-08-14"))  # True
print(is_date_available("2023-08-16"))  # False
'''

def is_date_available(date):
    if date in events: 
        return False

    return True

# OR keep original and just add not in front of in
    #  if date not in events: 

print(is_date_available("2023-08-14"))  # False
print(is_date_available("2023-08-16"))  # True