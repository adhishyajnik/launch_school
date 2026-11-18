"""
Print the method resolution order for cars, trucks, boats, and vehicles as
defined in the previous exercise.
"""


class SignalMixin:
    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signalling right")

    def signal_off(self):
        print("Signal is now off")


class Vehicle:
    num_vehicles = 0

    def __init__(self):
        Vehicle.num_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.num_vehicles


class Car(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()


class Truck(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()


class Boat(Vehicle):
    def __init__(self):
        super().__init__()


print(type.mro(Car))
print(type.mro(Truck))
print(type.mro(Boat))
print(type.mro(Vehicle))
