#!/usr/bin/python3


class person:
    def __init__(self, name, age):
        self._name= name
        self._age= age
    
    # using property to sett a getter and setter 
    @property
    def name(self):
        return self._name

    # by default name only have getter 
    # so we will create a setter method for name 
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

john = person("john", 30)

print("john name is : " + john.name)

john.name = "John doe"

print("now john name is : "+john.name)
