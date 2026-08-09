# Q1.Create a file named notes.txt.
# Requirement: Use open() with write mode ("w").

files=open("file.txt","w")
files.write("vidita")
files.close()

with open("file.txt","w") as files:
    files.write("vidhita")
print(files)    

# Q2.Read the contents of notes.txt using Python and print the complete content in the terminal.
# Requirement: Use read mode ("r").
with open("file.txt","r") as files:
    data= files.read()

print(data)    


# Q3 — Append to a File
# Add the following line to the existing notes.txt file:
# Excel
# Requirement: Use append mode ("a").

with open("file.txt","a") as files:
    files.write("\nvidhita")
print(files)  

# Use read() and print the complete file.
with open("file.txt","r") as files:
    print(files.read()) 

# Use readline() and print only the first line.
with open("file.txt","r") as files:
    print(files.readline()) 

# Use readlines() and print all lines as a list.
with open("file.txt","r") as files:
    print(files.readlines()) 

# Use a for loop to print each line separately.    
with open("file.txt","r") as files:
    for line in files:
        print(line)

# Create this list: # skills = ["Python\n", "SQL\n", "Power BI\n", "Excel\n"]
# Then use writelines() to write these into file.txt.    

skills = ["Python\n", "SQL\n", "Power BI\n", "Excel\n"]
with open("file.txt","w") as files:
    files.writelines(skills)
with open("file.txt","r") as files:
    print(files.read())

                # Q1 — File Handling Practice
# Create a list of student names:
# students = ["Vidita\n", "Rahul\n", "Aman\n", "Priya\n"]

# Requirements:
# Create a new file named students.txt.
# Use writelines() to write all student names into the file.
# Open the same file in read mode.
# Use read() to read and print the complete file content.  
students=["vidita\n","rahul\n","aman\n","priya\n"]  
files=open("students.txt","w")
files.writelines(students)
files.close()
with open("students.txt","r") as files:
    print(files.read())

     # Q2 — Practical File Handling
# Create a file named skills.txt containing:
# Python
# SQL
# Power BI
# Excel

# Requirements:
# Store the skills in a list.
# Use writelines() to write them to skills.txt.
# Open the file in read mode.
# Use a for loop to print each skill on a separate line.
# Do not use readlines() for this question.
with open("skills.txt","w") as skill:
    skill.writelines(["python\n","SQL\n","excel\n"])
with open("skills.txt","r") as skill:
    for lines in skill:
        print(lines)

                # Q3 — Append Practice
# Create skills.txt with:
# Python
# SQL
# Power BI

# Then append the following two skills without deleting the existing content:

# Excel
# Tableau
# Requirements:
# Use "w" mode to create/write the initial skills.
# Use "a" mode to add Excel and Tableau.
# Finally, use "r" mode and read() to print the complete file.

with open("skills.txt","w") as files:
    files.writelines(["python\n","SQL\n","power bi\n"])
with open("skills.txt","a") as files:
    files.writelines(["excel\n","tableau\n"])    
with open("skills.txt","r") as files:
    print(files.read())

                  # Exception Handling
# Q1 — Practice
# Write a Python program that asks the user to enter their age.

# Requirements:

# Use try-except.
# Convert the input into an integer.
# If the user enters a valid number, print:
# Your age is: <age>
# If the user enters something that cannot be converted to an integer, print:
# Invalid age. Please enter a number.  
try:
    age=int(input("ENTER YOUR AGE:"))
    print(f"YOUR AGE IS {age}")
except ValueError:
    print("please enter in number")

# Q2 —  Write a Python program that asks the user to enter two numbers and divides the first number by the second.

# Requirements:
# Use try-except.
# Convert both inputs into integers.
# Print the result of the division.
# Handle the situation when the user enters 0 as the second number.
# Print:
# Cannot divide by zero.

try:
    a=int(input("ENTER 1ST NUMBER:"))
    b=int(input("ENTER 2ST NUMBER:"))
    DIVI= (a/b)
    print("THE DIVISION IS :",DIVI)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError :
    print("cannot divide by zero")   

# Q. Write a Python program that asks the user to enter their marks.

# Requirements:

# Use try-except-else.
# Convert the input into an integer.
# If the input is not a valid number, print:
# Invalid marks.
# If the input is valid, use else to print:
# Marks entered successfully: <marks>
try:
    marks=int(input("enter your marks:"))
except ValueError:
    print("INVALID MARKS")
else:
    print(f"marks entered sucessfully {marks}")        

# Write a Python program that asks the user to enter a number.

# Requirements:

# Use try-except-finally.
# Convert the input into an integer.
# If the input is invalid, print:
# Invalid number.
# Always print:
# Program execution completed.
try:
    number=int(input("ENTER THE NUMBER:"))
except ValueError:
    print("invalid number")
else:
    print(f"number added sucessfully {number}") 
finally:
    print("PROGRAM EXECUTION COMPLETED")        

                         # Mini Challenge
           # Question — Student Marks Validator
# Create a Python program that asks the user to enter student marks.

# Requirements:

# Use try-except-else-finally.
# Convert marks to an integer.
# Handle invalid input using ValueError.
# If marks are successfully entered:
# Print the marks.
# Print "PASS" if marks are 50 or above.
# Otherwise print "FAIL".
# Always print:
# Student marks processing completed.
try:
    marks=int(input("enter your marks:"))
except ValueError:
    print("marks entered are invalid")    
else:
    if(marks>=50):
        print("PASS")
    else:
        print("FAIL")
finally:
    print("Student Marks Processing Completed")           