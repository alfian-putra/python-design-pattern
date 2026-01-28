# Structural Design Pattern : Adapter

Adapter Design Pattern is a structural pattern that acts as a bridge between two incompatible interfaces, allowing them to work together (Geeks for Geeks). The keyword is a __bridge__, and __unrelated/incompatible interfaces__. One of the great real life example of Adapter design pattern is mobile charger. Mobile battery needs 3 volts to charge but the normal socket produces either 120V (US) or 240V (India). So the mobile charger works as an adapter between mobile charging socket and the wall socket (DigitalOcean).

Now we are going to the code that i got from [this course](https://www.udemy.com/course/design-patterns-python/). In this code we have a function `calculate_area()` to calculate the area of rectangle in the other side we have a `Square()` class that have an atribute side. Now the objective is how we make a function`calculate_area()` would be compatible to calculate the area of `Square()` object.

We can solve this problem by make `SquareToRectangleAdapter` which has responsibility to make `Square` object can be implemented as `Rectangle`. In `SquareToRectangleAdapter` we make an object that has `width` and `height`  (We got this from `Square.side`).

Now `calculate_area` can calculate the area of `Square` that bridged with `SquareToRectangleAdapter`.