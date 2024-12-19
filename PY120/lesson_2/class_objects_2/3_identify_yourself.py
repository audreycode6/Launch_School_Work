'''Using the following code, 
add a method named identify that returns the calling object.'''
class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def identify(self):
        return self

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.identify())
# <__main__.Cat object at 0x10508c8d0>
# The object ID (0x105...) may vary