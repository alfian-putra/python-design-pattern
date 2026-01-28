#!/usr/bin/python3

class Bicycle():
    def __init__(self, color):
        self.color = color
    
    def clone(self):
        return Bicycle(self.color)

    def __str__(self):
        return f"{self.color} Bicycle "

class BicycleProducer():
    def __init__(self, bicycle):
        self.bicycle=bicycle
    
    def clone(self):
        return self.bicycle.clone()
    
redBicycle = Bicycle("red")
bicycleProducer = BicycleProducer(redBicycle)
newBicycle = bicycleProducer.clone()

print("New Bicycle : "+str(newBicycle))