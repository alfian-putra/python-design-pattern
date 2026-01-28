#!/usr/bin/python3

class Singleton():
    instance = None

    def __new__(self):
        if self.instance==None:
            self.instance = super().__new__(self)
        return self.instance

a = Singleton()
b = Singleton()

print(a==b)