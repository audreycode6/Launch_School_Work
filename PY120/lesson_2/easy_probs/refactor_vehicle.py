'''Refactor these classes so they all use a common superclass, 
and inherit behavior as needed.'''
'''TODO: 
-all initializers have make and model, (truck also tacks in 1 extra : payload)
- all have get wheel method but have unique reuturn #'
    - Car: 4, motorcycle:2, truck:6
- all have: info method: exactly the same
    '''
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self._payload = payload

    @property
    def payload(self):
        return self._payload

    def get_wheels(self):
        return 6


car_test = Car('saturn', 'vue')
truck_test = Truck('ford', 'tuff', 5500)
moto_test = Motorcycle('foo', 'bar')

print(car_test.info())
print(truck_test.info())
print(truck_test.payload) # bc decorator dont use () after payload
print(moto_test.info())

print(car_test.get_wheels())
print(truck_test.get_wheels())
print(moto_test.get_wheels())