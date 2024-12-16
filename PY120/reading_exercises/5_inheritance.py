'''We've provided new Car and Truck classes and some tests below.
Refactor them to use inheritance for as much behavior as possible.
The tests shown in the code should still work as shown:'''


'''TODO:
make a parent (superclass) (Vehicles) and store class methods (?)they can use:
    -__init__:  ( def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg  )
    - def max_range_in_miles(self):
        return self.capacity * self.mpg


could probably make static methods/ mixin for family_drive and hookup_trailer 
    since it is only print statement
- hook_up shouldnt work with Car objects 
- family_drive shouldnt work with Truck objects
- if use mix in can just pass to class that needs it!
    
'''

class Vehicles:
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicles):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicles):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car