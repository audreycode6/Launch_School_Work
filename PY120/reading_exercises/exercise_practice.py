class Person:
    
    def __init__(self, first_name, last_name):
        # two instance variables to hold a person's first and last names
        self._set_full_name(first_name, last_name)
        
    @property
    def full_name(self):
        # getter method that returns the person's name as a full name 
			# (the first and last names are separated by spaces), 
			# with both first and last names capitalized correctly.
        first_name = self._first_name.capitalize()
        last_name = self._last_name.capitalize()
        return f"{first_name} {last_name}"
    
    @full_name.setter
    # setter method that takes the name from a two-element tuple. 
		# These names must meet the requirements given for the constructor.
    def full_name(self, full_name):
        first_name, last_name = full_name
        self._set_full_name(first_name, last_name)
        
    @classmethod
    def _validate(clss, full_name):
        # first_name and last_name must be only alphabetical chars
        if not full_name.isalpha():
            raise ValueError('Name must be alphabetic.')
        
    def _set_full_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name
