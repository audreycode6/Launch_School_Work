'''Using the following code, add a personal_greeting method that prints a message as shown below:
'''
class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def personal_greeting(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.personal_greeting()     # Hello! My name is Sophie!