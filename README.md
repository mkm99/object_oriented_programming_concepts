[![Build Status](https://travis-ci.com/mkm99/object_oriented_programming_concepts.svg?branch=master)](https://travis-ci.com/mkm99/object_oriented_programming_concepts)

# Explanation of some Object Oriented Programming (OOP) concepts
In this repo, I would explain some concepts of Object Oriented Programming. Examples are written in Python to help understanding concepts. Every concept includes a piece of code to illustrate the explanation. Additionally, I added a link to go to the python file respectively.


## Encapsulation
Encapsulation means to keep the data of an object in a private state inside a class. We want to do this so other objects do not gain access to it directly. However, there is a way to gain access to the correspondidng data using predetermined methods (or functions). In simple words, the only way to gain access to the object's data is by the methods that have already written to modify or display their value.  

In the python script, I will be using the example of a House object. The house will have size, color, number of windows, number of doors, and if it has a backyard; this data can only be accessed using methods that I have already wrote.

```
class House:
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        self.size = size
        self.color = color
        self.num_of_windows = num_of_windows
        self.num_of_doors = num_of_doors
        self.backyard = backyard

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_windows(self):
        return self.num_of_windows

    def get_doors(self):
        return self.num_of_doors

    def get_bool_backyard(self):
        return self.backyard

    def do_We_Need_garage(self):
        return ""
```

#### You can access the script clicking in the link ####
- [House Blueprint](/houseBlueprint.py)

<br>


## Abstraction
Abstraction would be something similar to encapsulation, because still the data from the object is not accessible directly.

Think of a box that you do not know what is inside, you use it but somehow gets your job done without knowing how. 

In my script I used the built-in function log() and sqrt() from the math library, in this case I used these functions to find the logarithm and the square root of a number. I was able to used these functions to find the solution, those built-in functions have code written to find the result and when you use them, but you do not need to know exactly what the code is doing.

```
class Logarithm:
    def logarithm(antilogarithm, base):
        return log(antilogarithm, base)

class SquareRoot:
    def squareRoot(radicant):
        return sqrt(radicant)`

```

#### You can access the script clicking in the link ####
- [Math Problems](/mathProblems.py)

<br>


## Inheritance
Thinking about inheritance, it is easier to think that you have a blueprint for a house, and you want to make several houses using that blueprint.

So basically, you are reusing what we already have in that blueprint, the new object (the child) **inherits** everything from the parent, but still the child will have new characteristics that will make it different from the parent. These new characteristics will be new functions that we can add to the child object.

```
class SummerHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)
        
        
class WinterHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)

```


#### You can access the script clicking in the link ####
- [Making Houses](/makingHouses.py)

<br>


## Polymorphism
The meaning of "Polymorphism" is “many forms”. Continuing with the example of the blueprint for a house, since we are able to use inheritance to make new houses, we can make them somehow different. Now if you take a look in the python script, we can see that all the houses will have a size, color, windows, doors, and a backyard. However, we want the houses to look different, but we can make changes to every object usig methods. In my script, the houses are different if they have a garage or not. So I wrote a function where the presence of a garage by printing out a statement. 

```
class SummerHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)

    def do_We_Need_garage(self):
        return "Yes, we need a garage!"


class WinterHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)

    def do_We_Need_garage(self):
        return "No, we do not need a garage!"
```


#### You can access the script clicking in the link ####
- [Making Houses](/makingHouses.py)
