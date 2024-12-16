class Vehicles:
    vehicle_count = 0

    def __init__(self):
        Vehicles.vehicle_count += 1

    @classmethod  
    def vehicles(cls):
        return Vehicles.vehicle_count
    
class Car(Vehicles):
    def __init__(self):
        super().__init__()

class Truck(Vehicles):
    def __init__(self):
        super().__init__()

class Boat(Vehicles):
    def __init__(self):
        super().__init__()

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8