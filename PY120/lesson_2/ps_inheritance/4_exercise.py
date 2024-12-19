'''Given the following code, modify Truck.start_engine 
    by appending 'Drive fast, please!' to the return value
    of Vehicle.start_engine. The 'fast' in 'Drive fast, please!'
    should be taken from the value of the speed argument.'''

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        # self.speed = speed
        '''^ Because you aren't using speed outside of the method 
        or needing to persist its value, it works perfectly fine
        without assigning it to self.speed.
          
        You would use self.speed = speed when you need to store
        the value of speed as part of the object's state,
        so it can be accessed by other methods or at a later time.'''
        return f'{super().start_engine()} Drive {speed}, please!'

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!