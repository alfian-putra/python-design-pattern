# Creational Design Pattern : Singleton

The Singleton Design Pattern ensures that a class has only one instance and provides a global access point to it. It is used when we want centralized control of resources, such as managing database connections, configuration settings or logging (geeksforgeeks). The government is an excellent example of the Singleton pattern. A country can have only one official government. Regardless of the personal identities of the individuals who form governments, the title, “The Government of X”, is a global point of access that identifies the group of people in charge (Refactoring.guru).

In python we can using magic method in python which \_\_new\_\_. Whenever a class is instantiated, two methods are called :

    __new__ : Responsible for creating a new instance of the class.
    __init__ : Initializes the instance.

Unlike \_\_init\_\_, which is used for setting up an object after it has been created, \_\_new\_\_ is responsible for creating and returning the new instance itself (geeksforgeeks).