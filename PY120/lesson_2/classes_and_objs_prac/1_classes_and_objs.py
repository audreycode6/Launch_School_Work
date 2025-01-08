'''Given the following code, create the Person class needed 
to make the code work as shown:'''
'''
-need Person class
- name instance variable
-optional add getter and setter for name 
    - use property decorator for getter and setter'''

class Person:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert