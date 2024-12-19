'''Suppose we're building a software system for a pet hotel business, so our classes deal with pets.
    One problem is that we need to keep track of different breeds of dogs, 
    since they have slightly different behaviors. 
    For example, bulldogs snore when they sleep, but other dogs do not.
    Okay, I have no idea if that's entirely true;
    I suspect it isn't. Let's pretend it is.

    Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"
'''
class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'
    
class Bulldog(Dog):
    def sleep(self): #override the sleep method for dogs in Bulldog class
        return 'snoring!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
bully = Bulldog()
print(bully.sleep()) # snoring!