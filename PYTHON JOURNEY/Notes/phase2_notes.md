DAY 10 and 11 — FILE HANDLING & EXCEPTION HANDLING

FILE HANDLING
- Learned how to create, write, append and read files using 
open().
- open() → file open/create
- "r" → read
- "w" → write/overwrite
- "a" → append
- write() → write string
- writelines() → write multiple lines
- read() → complete file
- readline() → one line
- readlines() → lines as list
- with open() → automatically closes file
- for line in file → read line by line

EXCEPTION HANDLING
- Learned how to prevent programs from crashing when errors occur.
- try → risky code
- except → handles error
- else → runs if no error
- finally → always runs
- ValueError → invalid value/input
- ZeroDivisionError → divide by zero

DAY 13 — OBJECT-ORIENTED PROGRAMMING (OOP)

OOP = Object-Oriented Programming.
It helps us organize data and functions together using classes and objects.

1. CLASS
A class is a blueprint/template for creating objects.

Syntax:
class Student:
    pass

`pass` is used when the class is empty for now.

2. OBJECT
An object is an actual instance of a class.

Example:
student1 = Student()
student2 = Student()

One class can create multiple objects.

3. __init__()
`__init__()` is a special method that runs automatically whenever an object is created.

It is mainly used to initialize/store object data.

Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Vidita", 21)

4. self
`self` refers to the current object.

self.name = name

Here:
- `name` → value/parameter received
- `self.name` → value stored inside the current object

For example:
student1.name → "Vidita"
student2.name → "Krishna"

The same `self` works for whichever object is currently being created/used.

5. ATTRIBUTES
Attributes are variables/data stored inside an object.

Example:
self.name
self.age
self.course
self.marks

We access them using the object:

student1.name
student1.age

6. METHODS
A function written inside a class is called a method.

Example:
class Student:
    def show_details(self):
        print(self.name)

Calling the method:
student1.show_details()

Methods can use the object's attributes through `self`.

7. FUNCTION vs METHOD

Function:
def greet():
    print("Hello")

Method:
class Student:
    def greet(self):
        print("Hello")

Function → generally outside a class
Method → defined inside a class

8. BASIC OOP FLOW

class
   ↓
object created
   ↓
__init__() runs automatically
   ↓
data stored using self
   ↓
methods use that data

9. EXAMPLE

class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def show_result(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

        if self.marks >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")

student1 = Student("Vidita", "Python", 90)
student2 = Student("Krishna", "SQL", 41)

student1.show_result()
student2.show_result()

10. WHAT I PRACTICED TODAY

✓ Created classes and objects
✓ Used `pass`
✓ Used `__init__()`
✓ Understood `self`
✓ Created and accessed attributes
✓ Created methods
✓ Called methods using objects
✓ Used conditions inside a method
✓ Created multiple objects from one class
✓ Built a Student Management mini project

KEY REMEMBER:

Class = Blueprint
Object = Actual instance
__init__() = Initializes object data
self = Current object
Attribute = Object's data
Method = Function inside class

DAY 13 → OOP BASICS COMPLETE ✅