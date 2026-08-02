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