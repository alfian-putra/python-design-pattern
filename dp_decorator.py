#!/usr/bin/python3


class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return 'A circle of radius %s' % self.radius

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return 'A square with side %s' % self.side


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    r = getattr(self.shape, 'resize', None)
    if callable(r):
      self.shape.resize(factor)

  def __str__(self):
    return "%s has the color %s" %\
           (self.shape, self.color)

print("initiate object :")
circle = ColoredShape(Circle(5), 'red')
square = ColoredShape(Square(5), "green")
print(circle)
print(square)
print("resize test :")
square.resize(2)
circle.resize(2)
print(circle)

