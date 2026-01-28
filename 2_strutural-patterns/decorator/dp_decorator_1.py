#!/usr/bin/python3

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def color(self):
        pass
    
class RedCar(Car):
    def color(self):
        return "red"

redCar= RedCar()

print("RedCar color is "+redCar.color())
