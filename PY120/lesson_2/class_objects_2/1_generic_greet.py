'''Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.'''
'''TODO:
-Cat class
- def init
-generic_greeting method: prints "Hello! I'm a cat!"'''

class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")
kitty = Cat()
# Cat.generic_greeting() # "Hello! I'm a cat!"
print(type(kitty).generic_greeting())