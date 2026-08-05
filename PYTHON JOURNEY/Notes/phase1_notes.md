# 📝 Python Notes

## 📅 Day 1 (29 July 2026)

### ✅ Topics Learned

* Variables
* Data Types (`int`, `float`, `str`, `bool`)
* `print()`
* `input()`
* Type Casting (`int()`, `float()`, `str()`)
* f-Strings
* Basic Arithmetic Operators (`+`, `-`, `*`, `/`)

### 💡 Key Learnings

* `input()` always returns a string.
* Use type casting when numeric input is needed.
* Prefer f-strings over string concatenation.
* Variables store values that can be reused later.

### ⚠️ Improvements

* Don't use `sum` as a variable name because it is a built-in Python function.
* Use meaningful variable names (e.g., `total`, `next_age`, `annual_salary`).
* Follow Python naming style: use lowercase variable names with underscores (`monthly_salary`).
* Add spaces around operators (`age = 21` instead of `age=21`).
* Think about edge cases (e.g., division by zero).

### 🛠️ Mini Projects Completed

* Student Information System
* Salary Calculator
* Basic Arithmetic Calculator

### 📌 Revision Checklist

* [x] Variables
* [x] Data Types
* [x] Input/Output
* [x] Type Casting
* [x] f-Strings
* [x] Arithmetic Operators

## 📅 Day 2 (30 July 2026)

### ✅ Topics Learned

* Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
* Assignment Operators (`+=`, `-=`, `*=`, `/=`)
* Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
* Boolean Values (`True`, `False`)

### 💡 Key Learnings

* `/` always returns a float.
* `//` returns the whole-number quotient (floor division).
* `%` returns the remainder.
* `**` is used for exponent (power).
* `==` compares values, while `=` assigns a value.
* Comparison operators return `True` or `False`.

### 🧠 Interview Learnings

* `"21" == 21` → `False` (string vs integer)
* `"9" > "10"` → `True` (strings are compared character by character)
* String comparison is based on Unicode values, not string length.
* Python is case-sensitive (`"Vidita"` ≠ `"vidita"`).

### ⚠️ Common Mistakes

* Don't use `sum` as a variable name.
* Don't confuse `=` with `==`.
* Don't use `/` when you need `//`.
* Use meaningful variable names.

### 🛠️ Programs Completed

* Operator Calculator
* Salary Calculator
* Classroom Calculator
* Movie Ticket Price (Operators Practice)

### 📌 Revision Checklist

* [x] Arithmetic Operators
* [x] Assignment Operators
* [x] Comparison Operators
* [x] Boolean Values

## 📅 Day 3 (31 July 2026)

### ✅ Topics Learned

* `if`
* `elif`
* `else`
* Decision Making
* Conditional Execution

### 💡 Key Learnings

* `if` executes only when the condition is `True`.
* `else` executes when all previous conditions are `False`.
* `elif` is used to check multiple conditions.
* Python checks conditions from top to bottom and stops after the first matching condition.
* Correct ordering of conditions is important.

### 🧠 Interview Learnings

* Use `==` for comparison and `=` for assignment.
* Always test boundary values (e.g., age 5, 18, 60).
* Proper indentation is required in Python.
* Conditions should be written from most specific/highest priority to lowest when needed.

### ⚠️ Common Mistakes

* Writing `=` instead of `==` inside an `if`.
* Incorrect order of `elif` conditions.
* Forgetting to handle edge cases.
* Inconsistent variable names.

### 🛠️ Programs Completed

* Voting Eligibility Checker
* Grade Calculator
* Login Validation
* Movie Ticket Price Checker
* Comparison Practice

### 📌 Revision Checklist

* [x] if
* [x] elif
* [x] else
* [x] Boolean Logic
* [x] Conditional Statements

# 📅 Day 4 - Logical Operators & For Loop

## ✅ Topics Learned
- Logical Operators:
  - and
  - or
  - not
- Combining multiple conditions
- Introduction to for loop
- range(start, stop, step)
- Loop variable (i)
- Multiplication Table using for loop

## 🧠 Key Concepts

### and
Returns True only if all conditions are True.

Example:
if age >= 18 and has_id == "yes"

### or
Returns True if at least one condition is True.

Example:
if is_student == "yes" or has_coupon == "yes"

### not
Reverses a Boolean value.

Example:
not True  → False
not False → True

### for Loop
Used when we know how many times to repeat something.

Syntax:
for i in range(start, stop, step):

## ⚠️ Mistakes I Made
- Used = instead of == inside if conditions.
- Confused the use of not.
- Thought step meant "counting" instead of "adding".
- Forgot that the stop value is not included.

## 💡 Summary
- Use and when every condition must be True.
- Use or when any one condition is enough.
- Use not to reverse True/False.
- range(start, stop, step)
- Stop value is excluded.

# 📅 Day 5 - While Loop

## ✅ Topics Learned
- while loop
- while True
- break
- continue
- ATM PIN Verification Mini Project

## 🧠 Key Concepts

### while
Repeats while a condition is True.

Example:
while count <= 5:

### while True
Creates an infinite loop.
The loop runs until break is executed.

### break
Stops the current loop immediately.

### continue
Skips the remaining code of the current iteration and starts the next iteration.

### attempt += 1
Shortcut for:
attempt = attempt + 1

Used to increase a counter.

## ⚠️ Mistakes I Made
- Thought while True prints forever automatically.
- Thought break ends the whole program.
- Confused break with continue.
- Didn't understand why input() is inside the loop.
- Forgot that break is only used when we want to exit the loop completely.

## 💡 Summary
- while is used when the number of repetitions is unknown.
- while True is useful for login systems and menus.
- break exits the loop.
- continue skips the current iteration.
- Counters are commonly updated using += 1.

# 🐍 Day 6 - Functions

## 📚 Topics Covered
- Functions
- Function Calling
- Parameters
- Multiple Parameters
- Return
- Boolean Return
- Functions Calling Functions
- Student Result Mini Project

---

## What is a Function?

A function is a reusable block of code that performs a specific task.

Syntax:

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello")
```

Calling a function:

```python
greet()
```

---

## Parameters

Parameters allow us to pass values into a function.

Example:

```python
def student(name):
    print(f"Hello {name}")

student("Vidita")
```

---

## Multiple Parameters

```python
def add(a, b):
    print(a + b)
```

---

## Return

The `return` keyword sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b

answer = add(5, 4)
print(answer)
```

### Difference Between print() and return()

| print() | return |
|---------|---------|
| Displays output | Sends value back |
| Cannot be reused | Can be stored in a variable |
| Ends after printing | Can be used later |

---

## Returning Boolean Values

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

---

## Function Calling Another Function

```python
def get_grade(marks):
    return "A"

def student_result():
    print(get_grade(95))
```

---

## Mini Project

🎓 Student Result System

Concepts Used:
- Functions
- Parameters
- Return
- if-elif-else
- Boolean Values

---

## Common Mistakes

❌ Forgetting ()

```python
greet
```

✅ Correct

```python
greet()
```

---

❌ Forgetting Parameters

```python
student()
```

✅ Correct

```python
student("Vidita")
```

---

❌ Forgetting to print a returned value

```python
add(4,5)
```

✅ Correct

```python
print(add(4,5))
```

or

```python
answer = add(4,5)
print(answer)
```

---

## Key Points

- Functions reduce code repetition.
- Parameters make functions flexible.
- return sends a value back.
- print() only displays output.
- Functions can call other functions.

---

## Status

✅ Day 6 Completed

# 🐍 Day 7 - Lists

## 📚 Topics Covered

- Lists
- Indexing
- Negative Indexing
- Nested Indexing
- Updating Elements
- len()
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- in / not in
- for Loop with Lists

---

## What is a List?

A list stores multiple values inside a single variable.

Lists are:
- Ordered
- Mutable
- Allow duplicate values

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

## Indexing

Positive Indexing:

```text
Apple   Banana   Mango
0        1        2
```

Negative Indexing:

```text
Apple   Banana   Mango
-3       -2       -1
```

Example:

```python
print(fruits[0])
print(fruits[-1])
```

---

## Updating Elements

```python
fruits[1] = "Orange"
```

---

## len()

Returns the total number of elements.

```python
print(len(fruits))
```

---

## Nested Indexing

```python
fruits[-1][1]
```

Step 1:

```python
fruits[-1]
```

↓

```text
"Mango"
```

Step 2:

```python
"Mango"[1]
```

↓

```text
a
```

---

# List Methods

## append()

Adds an element at the end.

```python
fruits.append("Orange")
```

---

## insert()

Adds an element at a specific index.

```python
fruits.insert(1, "Orange")
```

---

## remove()

Removes an element using its value.

```python
fruits.remove("Banana")
```

---

## pop()

Removes an element using its index.

```python
fruits.pop(1)
```

If no index is given:

```python
fruits.pop()
```

It removes the last element.

---

## sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

---

## reverse()

Reverses the order of the list.

```python
numbers.reverse()
```

---

## in Operator

Checks if an element exists.

```python
print("SQL" in subjects)
```

---

## not in Operator

Checks if an element does not exist.

```python
print("Java" not in subjects)
```

---

## for Loop with Lists

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

The loop stores one element at a time in the variable.

---

## Difference

### append() vs insert()

| append() | insert() |
|-----------|----------|
| Adds at the end | Adds at a specific index |

---

### remove() vs pop()

| remove() | pop() |
|-----------|--------|
| Removes by value | Removes by index |
| Doesn't return removed element | Returns removed element |

---

## Common Mistakes

❌ Using remove() with an index.

```python
fruits.remove(1)
```

✅ Correct

```python
fruits.pop(1)
```

---

❌ Confusing value and index.

❌ Forgetting indexing starts from 0.

❌ Forgetting negative indexing starts from -1.

---

## Key Points

- Lists are mutable.
- Positive indexing starts from 0.
- Negative indexing starts from -1.
- append() adds at the end.
- insert() adds at a specific index.
- remove() removes by value.
- pop() removes by index.
- sort() arranges elements.
- reverse() reverses the order.
- in and not in check membership.
- for loop is used to traverse a list.

---

## Status

✅ Day 7 Completed
# 📅 Day 8 - Python Notes
# Topic: Tuples & Dictionaries

---

# 🔹 Tuple

A tuple is an ordered collection of items.

- Written using ()
- Ordered
- Allows duplicate values
- Cannot be modified (Immutable)

Example:

```python
fruits = ("Apple", "Banana", "Mango")
```

---

# 🔹 Accessing Tuple Elements

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])      # Apple
print(fruits[-1])     # Mango
```

---

# 🔹 Tuple Length

```python
print(len(fruits))
```

Output:

```
3
```

---

# 🔹 Loop Through a Tuple

```python
for fruit in fruits:
    print(fruit)
```

Output:

```
Apple
Banana
Mango
```

---

# 🔹 Single Element Tuple

Wrong:

```python
number = (5)
```

This is an integer.

Correct:

```python
number = (5,)
```

The comma makes it a tuple.

---

# 🔹 Dictionary

A dictionary stores data as Key : Value pairs.

- Written using {}
- Keys are unique
- Values can be duplicated
- Data is accessed using keys instead of indexes

Example:

```python
student = {
    "name": "Vidita",
    "age": 21,
    "course": "BCA"
}
```

---

# 🔹 Access Values

```python
print(student["name"])
print(student["age"])
```

Output:

```
Vidita
21
```

---

# 🔹 Add or Update Values

```python
student["city"] = "Delhi"

student["age"] = 22
```

---

# 🔹 get()

Safely access a value.

```python
print(student.get("course"))
```

If the key doesn't exist:

```python
print(student.get("salary"))
```

Output:

```
None
```

Provide a default value:

```python
print(student.get("salary", "Not Found"))
```

Output:

```
Not Found
```

---

# 🔹 keys()

Returns all keys.

```python
print(student.keys())
```

Output:

```
dict_keys(['name', 'age', 'course'])
```

---

# 🔹 values()

Returns all values.

```python
print(student.values())
```

Output:

```
dict_values(['Vidita', 21, 'BCA'])
```

---

# 🔹 items()

Returns key-value pairs.

```python
print(student.items())
```

Output:

```
dict_items([
('name', 'Vidita'),
('age', 21),
('course', 'BCA')
])
```

---

# 🔹 Loop Through Dictionary Keys

```python
for key in student:
    print(key)
```

Output:

```
name
age
course
```

---

# 🔹 Loop Through Dictionary Values

```python
for value in student.values():
    print(value)
```

Output:

```
Vidita
21
BCA
```

---

# 🔹 Loop Through Dictionary (Keys + Values)

```python
for key, value in student.items():
    print(f"{key} : {value}")
```

Output:

```
name : Vidita
age : 21
course : BCA
```

---

# ⭐ Interview Questions

### Difference between List and Dictionary

| List | Dictionary |
|------|------------|
| Uses [] | Uses {} |
| Access by Index | Access by Key |
| Ordered | Key-Value Pair |

---

### Difference between student["city"] and student.get("city")

```python
student["city"]
```

- Gives **KeyError** if the key doesn't exist.

```python
student.get("city")
```

- Returns **None** (or a default value if provided) instead of an error.

---

### Difference between Tuple and List

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Can be modified | Cannot be modified |

---

# 📝 Mini Project: Student Information System

Concepts Used:

- Dictionary
- User Input
- Loop
- items()
- get()

Example:

```python
student = {}

student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["course"] = input("Enter your course: ")

print("\n===== STUDENT DETAILS =====")

for key, value in student.items():
    print(f"{key} : {value}")

field = input("\nEnter field to search: ")

print(student.get(field, "Oops! Not Found"))
```

---

# 📚 Day 8 Summary

✅ Tuples

✅ Tuple Indexing

✅ Tuple Looping

✅ Dictionary

✅ Key-Value Pairs

✅ Add & Update Values

✅ get()

✅ keys()

✅ values()

✅ items()

✅ Loop Through Dictionary

✅ Student Information System Mini Project
# 📅 Day 8 - Python Notes
# Topic: Tuples, Dictionaries & Sets

---

# 🔹 Tuple

A tuple is an ordered collection of items.

- Uses ()
- Ordered
- Allows duplicate values
- Immutable (Cannot be changed)

Example:

```python
fruits = ("Apple", "Banana", "Mango")
```

---

# 🔹 Tuple Indexing

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])      # Apple
print(fruits[-1])     # Mango
```

---

# 🔹 Tuple Length

```python
print(len(fruits))
```

---

# 🔹 Loop Through Tuple

```python
for fruit in fruits:
    print(fruit)
```

---

# 🔹 Single Element Tuple

Wrong

```python
number = (5)
```

Correct

```python
number = (5,)
```

A comma makes it a tuple.

---

# 🔹 Dictionary

A dictionary stores data in **Key : Value** pairs.

- Uses {}
- Keys are unique.
- Values can be duplicate.
- Access data using keys instead of indexes.

Example

```python
student = {
    "name": "Vidita",
    "age": 21,
    "course": "BCA"
}
```

---

# 🔹 Access Values

```python
print(student["name"])
print(student["age"])
```

---

# 🔹 Add or Update Data

```python
student["city"] = "Delhi"

student["age"] = 22
```

---

# 🔹 get()

Safely accesses a value.

```python
print(student.get("course"))
```

If the key doesn't exist:

```python
print(student.get("salary"))
```

Output

```
None
```

Default value:

```python
print(student.get("salary", "Not Found"))
```

---

# 🔹 keys()

Returns all keys.

```python
print(student.keys())
```

---

# 🔹 values()

Returns all values.

```python
print(student.values())
```

---

# 🔹 items()

Returns key-value pairs.

```python
print(student.items())
```

---

# 🔹 Loop Through Dictionary

Only Keys

```python
for key in student:
    print(key)
```

Only Values

```python
for value in student.values():
    print(value)
```

Keys & Values

```python
for key, value in student.items():
    print(f"{key} : {value}")
```

---

# 🔹 Set

A set is an unordered collection of unique values.

- Uses {}
- Unordered
- Mutable
- Does NOT allow duplicate values.

Example

```python
numbers = {1, 2, 3, 4}
```

---

# 🔹 Duplicate Values

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output

```
{1, 2, 3, 4}
```

Duplicates are automatically removed.

---

# 🔹 Empty Set

Wrong

```python
data = {}
```

This creates a dictionary.

Correct

```python
data = set()
```

---

# 🔹 add()

Adds a new element.

```python
fruits.add("Mango")
```

---

# 🔹 remove()

Removes an element.

```python
fruits.remove("Banana")
```

⚠️ Gives **KeyError** if the element doesn't exist.

---

# 🔹 discard()

Removes an element safely.

```python
fruits.discard("Orange")
```

If the element doesn't exist, no error is generated.

---

# 🔹 len()

Returns total number of elements.

```python
print(len(fruits))
```

---

# 🔹 Loop Through a Set

```python
for fruit in fruits:
    print(fruit)
```

**Note:** Sets are unordered, so the output order may change.

---

# 🔹 union()

Combines two sets and removes duplicates.

```python
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
```

Output

```
{1,2,3,4,5}
```

---

# 🔹 intersection()

Returns common elements.

```python
print(A.intersection(B))
```

Output

```
{3}
```

---

# 🔹 difference()

Returns elements present in the first set but not in the second.

```python
print(A.difference(B))
```

Output

```
{1,2}
```

```python
print(B.difference(A))
```

Output

```
{4,5}
```

**Difference depends on the order of the sets.**

---

# ⭐ Interview Questions

### Difference between List and Set

| List | Set |
|------|-----|
| Uses [] | Uses {} |
| Ordered | Unordered |
| Allows Duplicates | Does Not Allow Duplicates |
| Access using Index | No Indexing |

---

### Difference between remove() and discard()

| remove() | discard() |
|-----------|-----------|
| Gives KeyError if item doesn't exist | No Error if item doesn't exist |

---

### Difference between union() and intersection()

| union() | intersection() |
|----------|----------------|
| Combines all unique elements | Returns only common elements |

---

### Difference between Tuple and List

| Tuple | List |
|--------|------|
| Uses () | Uses [] |
| Immutable | Mutable |
| Ordered | Ordered |

---

# 📝 Mini Project - Student Course Enrollment System

## Concepts Used

- Set
- add()
- discard()
- union()
- intersection()
- difference()
- len()
- User Input

Example

```python
python_students = {"Rahul", "Vidita", "Aman"}
sql_students = {"Vidita", "Rohit", "Priya"}

new_student = input("Enter a new Python student: ")
python_students.add(new_student)

remove_student = input("Enter student to remove: ")

python_students.discard(remove_student)
sql_students.discard(remove_student)

print("\n========== COURSE REPORT ==========")

print("Python Students :", python_students)
print("SQL Students :", sql_students)
print("All Students :", python_students.union(sql_students))
print("Learning Both :", python_students.intersection(sql_students))
print("Only Python :", python_students.difference(sql_students))
print("Only SQL :", sql_students.difference(python_students))
print("Total Unique Students :", len(python_students.union(sql_students)))

print("===================================")
```

---

# 📚 Day 8 Summary

✅ Tuples

✅ Tuple Indexing

✅ Loop Through Tuple

✅ Dictionaries

✅ keys()

✅ values()

✅ items()

✅ get()

✅ Dictionary Mini Project

✅ Sets

✅ add()

✅ remove()

✅ discard()

✅ union()

✅ intersection()

✅ difference()

✅ Student Course Enrollment System Mini Project

---

# 🎯 Key Takeaways

- Tuple is **immutable**.
- Dictionary stores data in **key-value pairs**.
- Set stores **only unique values**.
- `remove()` throws an error if the item doesn't exist.
- `discard()` removes safely without an error.
- `union()` combines unique elements.
- `intersection()` returns common elements.
- `difference()` returns elements present only in the first set.
- `len(set)` gives the total number of unique elements.