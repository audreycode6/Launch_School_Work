'''Further Exploration
This exercise can be solved in a similar manner 
by using inheritance; a Noble is a Person, and a 
Cheetah is a Cat, and both Persons and Cats are Animals.
What changes would you need to make to this program to 
establish these relationships and eliminate 
the two duplicated __str__ methods?

Is __str__ the best way to provide the name and
title functionality we needed for this exercise? 
Might it be better to create either a different
name method (or say a new full_name method) that 
automatically accesses title and name attributes? 
There are tradeoffs with each choice -- they are worth considering.'''

'''TODO:
-noble inherits from Person
-cheetah inherits from Cat
    -establish the relationships and elminate the duplicate __Str__ methods'''

class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name, title=''): # NEW
        self.name = name
        self.title = title

    def __str__(self):  # NEW
        if self.title == '':
            return self.name
        return f"{self.title} {self.name}"

    def gait(self):
        return "strolls"
    
class Noble(Person): #NEW
    def __init__(self, name, title):
        super().__init__(name, title)

    def gait(self):
        return 'struts'

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def gait(self):
        return "saunters"

class Cheetah(Cat):
    def gait(self):
        return "runs"
    
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"