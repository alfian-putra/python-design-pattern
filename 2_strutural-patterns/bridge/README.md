# Structural Design Pattern : Bridge

Bridge is a structural design pattern that lets you __split a large class__ or a set of closely related classes into two separate hierarchies (Refactoring.guru). In short of, in bridge design pattern large class splited into a separate hierarchy.

In this example we have 2 abstract which each of them has a 2 implementation :
- Tool : Pen, Pencil
- Function = Drawing, Writing

Now we can make a penForDrawing that is combination of `Pen` and `Drawing` and so on.