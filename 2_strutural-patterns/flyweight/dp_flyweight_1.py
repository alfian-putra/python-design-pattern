#!/usr/bin/python3

class Data():
    def __init__(self, data):
        self.data = data

class dataFactory():
    def __init__(self):
        self.data= {}
    
    def add_data(self, id, data):
       if not id in self.data:
           self.data[id] = Data(data)
       else:
           print("Using existing data")
    def get_data(self, id):
        return self.data[id]
    

factory = dataFactory()

factory.add_data("d1", "data 1")
factory.add_data("d1", "data 1")
factory.add_data("d2", "data 2")
print(factory.data)
