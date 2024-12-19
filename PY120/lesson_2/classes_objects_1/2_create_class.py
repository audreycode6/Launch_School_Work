'''2.Create an empty class named Cat.
3.  create an instance of Cat and assign it to a variable named kitty.
4. add a __init__ method that prints I'm a cat! when a new Cat 
    object is instantiated.

5. , add a parameter to __init__ that provides a name for the Cat object. 
    Use an instance variable to print a greeting with the provided name. 
    (You can remove the code that displays I'm a cat!.)

6. move the greeting from the __init__ method to an instance method named
     greet that prints a greeting when invoked. 
     Make sure you write some code that invokes the method.


'''
class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


kitty = Cat('Sophie')
kitty.greet()
