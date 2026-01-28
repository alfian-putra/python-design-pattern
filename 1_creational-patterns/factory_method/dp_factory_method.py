#!/usr/bin/python3

from abc import ABC

class Vehicle(ABC):
    def __init__(self, name, color):
        self.name=name
        self.color=color
    
    def __str__(self):
        return f"{self.color} {self.name}"

class Bicycle(Vehicle):
    def __init__(self, color):
        self.name="bicycle"
        self.color = color
    
class Car(Vehicle):
    def __init__(self, color):
        self.name="car"
        self.color = color

class VehicleFactory():
    def produce(self,vehicle, color):
        if vehicle=="bicycle":
            return Bicycle(color)
        elif vehicle=="car":
            return Car(color)
        
factory = VehicleFactory()

redCar = factory.produce("car","red")
blueBicycle = factory.produce("bicycle","blue")

print(redCar)
print(blueBicycle)
        