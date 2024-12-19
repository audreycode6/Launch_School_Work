'''create a class named Person.

When you instantiate a Person object, 
you should pass in one argument 
that contains the person's name.

If no arguments are given,
 the Person object should be 
 instantiated with a name of "John Doe".
'''
'''
-make Person class
-define __init__ method: takes in name arg
    - if no arg given default name is John Doe
- make a getter for name'''
class Person:

    def __init__(self, name='John Doe'):
        self._nam1_  = name

    @property
    def name(self):
        return self._name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew