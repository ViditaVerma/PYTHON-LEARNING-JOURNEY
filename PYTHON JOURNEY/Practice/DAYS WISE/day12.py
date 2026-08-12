# Write a Python program that:
# Imports the math module.
# Takes a number from the user.
# Prints its square root using math.sqrt().
import math
nu=int(input("enetr the number "))
print("SQAURE ROOT IS :",math.sqrt(nu))

# Q2  Write a Python program that:
# Imports the random module.
# Generates a random integer between 1 and 10.
# Prints the generated number.
import random
print(random.randint(1,10))

# Q3.Write a Python program that:
# Imports pi directly from the math module.
# Takes the radius of a circle from the user.
# Calculates the area using:
#     area = pi × radius²
# Print the area.

from math import pi
radius=int(input("ENTER THE RADIUS of circle :"))
area= pi*radius**2
print("area is:",area)

# Q4. Write a Python program that:
# Imports ceil and floor directly from the math module.
# Takes a decimal number from the user.
# Prints its ceiling and floor values.
from math import ceil,floor
nu=float(input("enter the number in decimal:"))
print("ceiling",ceil(nu))
print("floor",floor(nu))

# Q5.Write a Python program that:
# Imports the random module.
# Takes the user's name as input.
# Generates a random number between 1 and 100.
# Prints:
# Hello Vidita!
# Your lucky number is: 57
import random
name=input("enter your name ")
rand= random.randint(1,100)
print(f" hell0 {name}\n your lucky number is :{rand}")

# create your own module (my_module) and import it 
import my_module
my_module.greet("rashi")
result=my_module.add(10,20)
print(result)

                   # mini challange 
# Create a custom module named calculator.py.

# Inside it, create these two functions:
# add(a, b)
# multiply(a, b)

# Import your calculator module.
# Take two numbers from the user.
# Use both functions.
# Print the addition and multiplication results.
import calculator_module
a=int(input("enter first number"))
b=int(input("enter second number"))
print("ADDITION IS       :",calculator_module.add(a,b))
print("MULTIPLICATION IS :",calculator_module.multiply(a,b))
print("SUBTRACTION IS    :",calculator_module.subtract(a,b))