# Explanation of some Object Oriented Programming (OOP) concepts
In this repo, I would explain some concepts of Object Oriented Programming. The code will be in python to serve as an example to help understand this concepts.


## Encapsulation
Encapsulation means to keep the data of an object in a private state inside a class. We want to do this so other objects do not gain access to it directly. However, there is a way to gain inderect access to the correspondidng data using predetermined methods (or functions). In simple words, the only way to gain access to the object's data is by the methods that have been already predetermined.  

In the code I wrote using python, I will be using the example of  object. The t-shirt will have a color, a brand, a size, and a state if the t-shirt is dirty or not; this data can only be accessed using methods that I have already wrote.

- [House Blueprint](/houseBlueprint.py)

<br>


## Abstraction
Abstraction would be something similar to encapsulation, because still the data from the object is not accessible directly.

Think of black box that you do not know what is inside, you use it but somehow gets your job done without knowing how. 

In my script I used the built-in function pow(), in this case I used this function to find the power of THAT number. I was able to used this function to find the solution, that built-in function has code written to find the result and when you use it but you do not need to know exactly what the code is doing.

- [Math Problems](/mathProblems.py)

<br>


## Inheritance
Thinking about inheritance, it is easier to think that you have a blueprint for a house, and you want to make several houses using that blueprint.

So basically, you are reusing what we have already in that blueprint, the new object (the child) INHERITS everything from the parent, but still the child will have new characteristics that will make it different from the parent. These new characteristics will be new functions that we can add to the child object.

- [Summer House](/makingHouses.py)

<br>


## Polymorphism
The meaning of "Polymorphism" is “many forms”. Continuing with the example of the blueprint for a house, since we are able to use inheritance to make new houses, we are able to make houses but make them somehow different. Now from the code in python, we can see that all the houses will have windows, doors, and ceiling. However, we want the houses to look different, so we can use the predetermined functions that we got by inheritance, but we can make changes to every object and make our houses diffrent.

- [Winter House](/winterVacationHouse.py)
