# Python - More Classes and Objects
## Resources
**Read or watch:**
- Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))
- Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
- Class and Instance Attributes
- classmethods and staticmethods
- Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)
- str vs repr
- Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

**Requirements**

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## 0. Simple rectangle
Write an empty class Rectangle that defines a rectangle:

- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$ 
No test cases needed
```

**GitHub repository:** holbertonschool-higher_level_programming
**Directory:** python-more_classes
**File:** 0-rectangle.py


## 1. Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

- Private instance attribute: width:
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
- property def height(self): to retrieve it
- property setter def height(self, value): to set it:
- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/$ 
No test cases needed
```

**GitHub repository:** holbertonschool-higher_level_programming
**Directory:** python-more_classes
**File:** 1-rectangle.py



## 2. Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

- Private instance attribute: width:
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
- width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
- if width is less than 0, raise a ValueError exception with the message width must be >= 0
- Private instance attribute: height:
- property def height(self): to retrieve it
- property setter def height(self, value): to set it:
- height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
- if height is less than 0, raise a ValueError exception with the message height must be >= 0
- Instantiation with optional width and height: def __init__(self, width=0, height=0):
- Public instance method: def area(self): that returns the rectangle area
- Public instance method: def perimeter(self): that returns the rectangle perimeter:
- if width or height is equal to 0, perimeter is equal to 0
- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/$ 
No test cases needed
```

**GitHub repository:** holbertonschool-higher_level_programming
**Directory:** python-more_classes
**File:** 2-rectangle.py