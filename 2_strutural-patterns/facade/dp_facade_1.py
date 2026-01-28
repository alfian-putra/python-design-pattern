#! /usr/bin/python3

from abc import ABC

class Animal(ABC):
    def __init__(self, name):
        self.name=name

class Monkey(Animal):
    def __init__(self):
        super().__init__("monkey")


class Tiger(Animal):
    def __init__(self):
        super().__init__("tiger")


class Bear(Animal):
    def __init__(self):
        super().__init__("bear")

class Zoo():
    def __init__(self):
        self.animal1 = Monkey()
        self.animal2 = Tiger()
        self.animal3 = Bear() 


zoo = Zoo()

print("There are "+zoo.animal1.name+"s in the zoo.")
print("There are "+zoo.animal2.name+"s in the zoo.")
print("There are "+zoo.animal3.name+"s in the zoo.")