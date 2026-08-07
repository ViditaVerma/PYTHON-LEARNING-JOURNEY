           # 🐍 Day 8 Mini Project

# Let's make something practical.

            # 📅 Month Finder
# Requirements
# Create a tuple of all 12 months.

# months = (
# "January",
# "February",
# ...
# )

# Ask the user to enter a month number (1–12).
#    Example:
# Enter month number: 8
  # Output:
# Month: August

months=("jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec")
value=int(input("enter the month number: "))
print("month :", months[value-1])

                  # Day 8 Mini Project - Student Information System
# Requirements

# Create a dictionary that stores a student's information.

# Ask the user for:

# Name
# Age
# Course

# Store all the data inside a dictionary.
# Example:

# student = {
#     "name": "Vidita",
#     "age": 21,
#     "course": "BCA"
# }

# Then print:

# ========= STUDENT DETAILS =========

# Name   : Vidita
# Age    : 21
# Course : BCA

# ===================================

student = {}

student["name"]=input("enter your name :")
student["age"]=int(input("enter your age:"))
student["course"]=input("enter your course :")

for key,value in student.items():
    print(f"{key}:{value}")

field=input("enter field to serach:")
print(student.get(field,"opps not found "))


#              Day 8 Mini Project - Course Enrollment System
# Python Students

# Rahul
# Vidita
# Aman

# SQL Students

# Vidita
# Rohit
# Priya
                 # Step 1

# Create two sets.

# python_students = {"Rahul", "Vidita", "Aman"}
# sql_students = {"Vidita", "Rohit", "Priya"}

              # Ask the user:

# Enter a new Python student:
# Add that student to the Python set.

                  # Step 3

# Ask the user: # Enter a student to remove:
# Remove the student using discard().

# (So the program doesn't crash if the name isn't found.)

python_students = {"Rahul", "Vidita", "Aman"}
sql_students = {"Vidita", "Rohit", "Priya"}

new_student=input("ENTER A NEW PYTHON STUDENT:")
python_students.add(new_student)
print("welcome to python course ,",new_student)

remove_student=input("enter a student to remove :")
sql_students.discard(remove_student)
python_students.discard(remove_student)
print("GOOD LUCK 111")

print("====================== COURSE REPORT =====================================")
print("PYTHON STUDENTS                :", python_students)
print("SQL STUDENTS                   :", sql_students)
print("ALL STUDENTS                   :", python_students.union(sql_students))
print("STUDENTS LEARNING BOTH         :", python_students.intersection(sql_students))
print("STUDENTS LEARNING ONLY PYTHON  :", python_students.difference(sql_students))
print("STUDENTS LEARNING ONLY SQL     :", sql_students.difference(python_students))
print("TOTAL UNIQUE STUDENTS          :", len(python_students.union(sql_students)))
print("==============================================================================")
