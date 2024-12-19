'''Using the code below, determine the method 
resolution order (MRO) used when accessing the 
cat1.color property. Only list the classes that
 are checked by Python when searching for the color 
 attribute. Do not use the mro method.'''

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)
'''MRO: [<class: Cat, Animal]'''