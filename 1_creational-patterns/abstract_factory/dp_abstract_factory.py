#!/usr/bin/python3

class AbstractFactory():
    def produceFactory(self, factory):
        if factory=="factory1":
            return Factory1()
        elif factory=="factory2":
            return Factory2()

class Factory1():
    def produceObject(self):
        return ObjFactory1()

class Factory2():
    def produceObject(self):
        return ObjFactory2()

class ObjFactory1():
    def __str__(self):
        return "obj factory 1"

class ObjFactory2():
    def __str__(self):
        return "obj factory 2"

abstractFactory = AbstractFactory()
factory1 = abstractFactory.produceFactory("factory1")
obj1 = factory1.produceObject()
print(obj1)

factory2 = abstractFactory.produceFactory("factory2")
obj2 = factory2.produceObject()
print(obj2)