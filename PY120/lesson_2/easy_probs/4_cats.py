'''Update this code so you see the following output when you run the code:'''

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Cat(Pet):
    def __init__(self, name, age, colors):
        super().__init__(name, age)
        self._colors = colors

    '''For easy access and encapsulation, getter properties
    have been introduced for each attribute. This approach
    provides a clean way of accessing the attributes without
    explicitly calling methods.'''
    @property
    def colors(self):
        return self._colors

    @property
    def info(self):
        return (f'''My cat {self._name} is {self._age} years old'''
              f''' and has {self._colors} fur.''')

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)
'''Outputs:
My cat Cocoa is 3 years old and has black fur.
My cat Cheddar is 4 years old and has yellow and white fur.'''