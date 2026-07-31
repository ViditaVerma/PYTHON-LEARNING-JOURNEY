print("FIRST DAY OF LEARNING PYTHON !")
# Store your:
# Name
# Age
# City
# College
#  Print them using f-strings.
name="vidita"
age=21
city="new delhi"
college="GGSIPU"
print(f"hello my name is {name} ,i am {age} year old . i live in {city} and i am BCA graduate from {college}")

# Ask the user:
# Name
# Favorite color
name=input("Enter your name:") # input() is string data type by default
color=input("Enter your fav color:")
print(f"wow {name} , {color} is mine fav too")

# Take two numbers as input 
# # Print:
# Sum
# Difference
# Product
# Division
number1=int(input("enter the 1st number:"))
number2=int(input("enter the 2nd number:"))
sum=(number1 + number2)
diff=(number1 - number2)
pro=(number1 * number2)
div=(number1 / number2)
print(f"SUM IS: {sum}")
print(f"DIFFERENCE IS: {diff}")
print(f"PRODUCT IS: {pro}")
print(f"DIVISION IS: {div}")

# Take:
# Name
# Age
name=input("WHAT IS YOUR NAME? :")
AGE=int(input("YOUR AGE? :"))
sum=(AGE + 1)
print(f"hello {name} , next year ypu will be {sum} year old ")

#/////////////////////////////////// CHALLENGE  /////////////////////
                         # Write a program that asks:
# Enter your monthly salary:
      # Then print:
# Monthly Salary : ₹50000
# Annual Salary  : ₹600000
salary=int(input("ENTER YOUR MONTHLY SALARY :"))
annual= (salary * 12)
print(f"MONTHLY SALARY : {salary}")
print(f"ANNUAL SALARY : {annual}")
