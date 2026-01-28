#!/usr/bin/python3

from abc import ABC

class Tool(ABC):
    def __init__(self, name, function):
        self.name = name
        self.function = function
    
    def __str__(self):
        return f"Using {self.name} for {self.function.name}"

class Function(ABC):
    def __init__(self, name):
        self.name = name
    
class Pencil(Tool):
    def __init__(self, usage):
        super().__init__('Pencil', usage)
                
class Pen(Tool):
    def __init__(self, usage):
        super().__init__('Pen', usage)

class Drawing(Function):
    def __init__(self):
        super().__init__("drawing")

class Writing(Function):
    def __init__(self):
        super().__init__("writing")

penForDrawing = Pen(Drawing())
pencilForDrawing = Pencil(Drawing())
penForWriting = Pen(Writing())
pencilForWriting = Pencil(Writing())

print(penForDrawing)
print(pencilForDrawing)
print(penForWriting)
print(pencilForWriting)