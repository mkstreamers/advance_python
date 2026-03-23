#19. Vehicle Rental SystemProblem: Create a rental system with a base class Vehicle and subclasses Car, Bike, and Truck. Include a rental rate for each and calculate the rental fee using overridden methods. Use class variables to track total vehicles rented.
class Vehicle:
    total_rented = 0

    def __init__(self, rate):
        self.rate = rate

    def calculate_rent(self, days):
        return self.rate * days


class Car(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rate * days


class Bike(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rate * days


class Truck(Vehicle):
    def calculate_rent(self, days):
        Vehicle.total_rented += 1
        return self.rate * days


car = Car(1000)
bike = Bike(500)
truck = Truck(2000)

print("Car Rent:", car.calculate_rent(3))
print("Bike Rent:", bike.calculate_rent(2))
print("Truck Rent:", truck.calculate_rent(1))

print("Total Vehicles Rented:", Vehicle.total_rented)