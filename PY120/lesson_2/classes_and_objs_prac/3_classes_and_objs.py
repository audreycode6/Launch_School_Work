'''Add a new setter property for name that takes either
 a first name or full name, and knows how to set the
  first_name and last_name properties appropriately. 
 Use the following code to test your code:'''

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}".strip()
    
    @name.setter
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    def __str__(self):
        return self.name

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

# bob = Person('Robert Smith')
# rob = Person('Robert Smith')

# print(bob.name == rob.name) # True, names are ==
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")