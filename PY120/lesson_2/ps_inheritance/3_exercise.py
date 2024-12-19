'''Using the following code, modify Truck to accept a
    second argument when instantiating a new Truck object. 
    Name the parameter bed_type. Ensure that the Car 
    constructor continues to accept only one argument.'''

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self._bed_type = bed_type
    
    @property
    def bed_type(self):
        return self._bed_type

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'