# Explanation of some Object Oriented Programming (OOP) concepts
In this repo, I would explain some concepts of Object Oriented Programming. The code will be in python to serve as an example to help understand this concepts.


## Encapsulation
Encapsulation means to keep the data of an object in a private state inside a class. We want to do this so other objects do not gain access to it directly. However, there is a way to gain inderect access to the correspondidng data using predetermined methods (or functions). In simple words, the only way to gain access to the object's data is by the methods that have been already predetermined.  

In the code I wrote using python, I will be using the example of  object. The t-shirt will have a color, a brand, a size, and a state if the t-shirt is dirty or not; this data can only be accessed using methods that I have already wrote.

<br>


## Abstraction
Abstraction would be something similar to encapsulation, because still the data from the object is not accessible directly.

Think of black box that you do not know what is inside, you use it but somehow gets your job done without knowing how. 

In my script I used the built-in function pow(), in this case I used this function to find the power of THAT number. I was able to used this function to find the solution, that built-in function has code written to find the result and when you use it but you do not need to know exactly what the code is doing.

<br>


## Inheritance
Thinking about inheritance, it is easier to think that you have a blueprint for a house, and you want to make several houses using that blueprint.

So basically, you are reusing what we have already in that blueprint, the new object (the child) INHERITS everything from the parent, but still the child will have new characteristics that will make it different from the parent. These new characteristics will be new functions that we can add to the child object.

<br>


## Polymorphism
Polymorphism means “many shapes” in Greek.
Say we have a parent class and a few child classes which inherit from it. Sometimes we want to use a collection — for example a list — which contains a mix of all these classes. Or we have a method implemented for the parent class — but we’d like to use it for the children, too.

This can be solved by using polymorphism.

Simply put, polymorphism gives a way to use a class exactly like its parent so there’s no confusion with mixing types. But each child class keeps its own methods as they are.

This typically happens by defining a (parent) interface to be reused. It outlines a bunch of common methods. Then, each child class implements its own version of these methods.

Any time a collection (such as a list) or a method expects an instance of the parent (where common methods are outlined), the language takes care of evaluating the right implementation of the common method — regardless of which child is passed.

Take a look at a sketch of geometric figures implementation. They reuse a common interface for calculating surface area and perimeter:

Having these three figures inheriting the parent Figure Interface lets you create a list of mixed triangles, circles, and rectangles. And treat them like the same type of object.

Then, if this list attempts to calculate the surface for an element, the correct method is found and executed. If the element is a triangle, triangle’s CalculateSurface() is called. If it’s a circle — then cirlce’s CalculateSurface() is called. And so on.

If you have a function which operates with a figure by using its parameter, you don’t have to define it three times — once for a triangle, a circle, and a rectangle.

You can define it once and accept a Figure as an argument. Whether you pass a triangle, circle or a rectangle — as long as they implement CalculateParamter(), their type doesn’t matter.

