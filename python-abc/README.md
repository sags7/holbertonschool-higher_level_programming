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

~~~
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