'''added a few more methods for our Dog class.
    Create a new class called Cat, 
    which can do everything a dog can, except fetch.
    Assume the methods do the exact same thing. 
    Hint: don't copy and paste any methods from Dog into Cat; 
    come up with a class hierarchy instead.
'''
class Pet():
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'
    def fetch(self):
        return 'fetching!'
class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'  
class Cat(Pet):
    def speak(self):
        return 'meow!'

pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

# print(pet.run())              # running!
# print(kitty.run())            # running!
# print(kitty.speak())          # meow!
# try:
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
#     # AttributeError 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"
print(Pet.mro())
print(Cat.__mro__)
print(Dog.__mro__)
print(Bulldog.__mro__)
'''OUTPUT:
(<class '__main__.Pet'>, <class 'object'>)
(<class '__main__.Cat'>, <class '__main__.Pet'>, <class 'object'>)
(<class '__main__.Dog'>, <class '__main__.Pet'>, <class 'object'>)
(<class '__main__.Bulldog'>, <class '__main__.Dog'>, <class '__main__.Pet'>, <class 'object'>)'''