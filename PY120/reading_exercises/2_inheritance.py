'''Create a mix-in for the Car and Truck classes
from the previous exercise that lets you operate 
the turn signals: signal left, signal right, and signal off.
Use the following code to test your code.'''

'''algo:
make mixin that works for Car and Truck classes
-lets you operate turn signals:
    -signa_left()
    -signal_right()
    - signal_off()'''

class SignalMixin:
    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print("Signalling right")

    def signal_off(self):
        print("Signal is now off")

class Vehicles:
    vehicle_count = 0

    def __init__(self):
        Vehicles.vehicle_count += 1

    @classmethod  
    def vehicles(cls):
        return Vehicles.vehicle_count
   
class Car(SignalMixin, Vehicles):
    def __init__(self):
        super().__init__()

class Truck(SignalMixin, Vehicles) :
    def __init__(self):
        super().__init__()

class Boat(Vehicles):
    def __init__(self):
        super().__init__()

car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()
truck1 = Truck()
truck2 = Truck()
boat1 = Boat()
boat2 = Boat()


car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
# boat1.signal_left() 
# AttributeError: 'Boat' object has no attribute
# 'signal_left'


print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicles.mro())
print(SignalMixin.mro())

'''output:
[<class '__main__.Car'>, <class '__main__.SignalMixin'>, <class '__main__.Vehicles'>, <class 'object'>]
[<class '__main__.Truck'>, <class '__main__.SignalMixin'>, <class '__main__.Vehicles'>, <class 'object'>]
[<class '__main__.Boat'>, <class '__main__.Vehicles'>, <class 'object'>]
[<class '__main__.Vehicles'>, <class 'object'>]
[<class '__main__.SignalMixin'>, <class 'object'>]'''