#!/usr/bin/python3

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        # TODO
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

square = Square(20)
squareAdapter = SquareToRectangleAdapter(square)
print("now calculate_area can be implemented to our squareAdapter : ")
print(calculate_area(squareAdapter))
