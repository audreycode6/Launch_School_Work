'''Using the code snippet provided below, 
    modify the instance variable name to indicate to developers 
    that it is intended for internal use only.
    
8. add a getter method named name and invoke it in place of self._name in greet.
9. add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again.'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet() # Hello! My name is Sophie!
kitty = Cat('Luna')
kitty.greet() # Hello! My name is Luna!