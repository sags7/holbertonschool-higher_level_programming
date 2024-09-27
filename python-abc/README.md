# Python - Abstract Classes and Interfaces

## Python OOP - Abtract Class, Interface, Subclassing
**Introduction:**
Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

**Learning Objectives:**
- **Abstract Classes:** Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
- **Interfaces and Duck Typing:** Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
- **Subclassing Standard Base Classes:** Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
- **Method Overriding:** Employ method overriding to alter or enhance the behavior of base class methods.
- **Multiple Inheritance:** Understand and apply multiple inheritance to form complex relationships between classes.
- **Mixins:** Utilize mixins to compose behavior across unrelated classes.

**Resources:**
- Python 3 Object-Oriented Programming
- ABC — Abstract Base Classes
- Real Python - Object-Oriented Programming (OOP) in Python 3
- Corey Schafer - OOP Playlist
- sentdex - Python OOP Tutorial

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. It’s recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.


## Tasks

## 0. Abstract Animal Class and its Subclasses

**Background:**
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s ABC package facilitates the creation of abstract base classes.

**Objective**:
Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.

**Create two subclasses of Animal:** Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.

**Resources:**
Python ABC documentation: https://docs.python.org/3/library/abc.html

**Instructions:**

**Setting up the Abstract Class:**
- Import the necessary components from the abc module.
- Define the Animal class, ensuring it inherits from ABC to mark it as abstract.
- Inside the Animal class, declare an abstract method named sound using the @abstractmethod decorator.

**Implementing the Subclasses:**
- Create a subclass named Dog that inherits from the Animal class.
- Implement the sound method in the Dog class to return the string “Bark”.
- Similarly, create a subclass named Cat that also inherits from the Animal class.
- Implement the sound method in the Cat class to return the string “Meow”.

**Hints:**
- The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
- If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a TypeError.

```
$ cat main_00_abc.py 
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main_00_abc.py 
Bark
Meow
Traceback (most recent call last):
  File "main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

**GitHub repository:** holbertonschool-higher_level_programming
**Directory:** python-abc
**File:** task_00_abc.py


## 1. Shapes, Interfaces, and Duck Typing

**Background:**
Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

**Objective:**
- Create an abstract class named Shape with two abstract methods: area and perimeter.
- Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
- Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
- Test the shape_info function with instances of both Circle and Rectangle.

**Resources:**
- Python ABC documentation: https://docs.python.org/3/library/abc.html
- Concept of Duck Typing: https://realpython.com/lessons/duck-typing/

**Instructions:**

**Shape Abstract Class:**
- Define an abstract class Shape using the ABC package.
- Within Shape, declare two abstract methods: area and perimeter.

**Circle and Rectangle Classes:**
- Create a Circle class that inherits from Shape. The constructor (__init__) should accept a radius. Implement the area and perimeter methods.
- Create a Rectangle class, also inheriting from Shape. Its constructor should accept the width and height. Implement the area and perimeter methods.

**shape_info Function:**
- Define a function named shape_info that takes a single argument.
- Without explicitly checking the type of the argument, call its area and perimeter methods (relying on duck typing).
- Print the area and perimeter of the shape passed to the function.

**Testing:**
- Instantiate a Circle and a Rectangle.
- Pass each object to the shape_info function and observe the output.

**Hints:**
While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
Duck typing in the shape_info function implies that you shouldn’t use isinstance checks. Instead, trust that the passed object adheres to the Shape interface.

```
$ cat main_01_duck_typing.py 
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

$ ./main_01_duck_typing.py 
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

**GitHub repository:** holbertonschool-higher_level_programming
**Directory:** python-abc
**File:** task_01_duck_typing.py