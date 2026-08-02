           # Question 1
 # a = 20
 # b = 6
#  Print:

# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Power
a = 20
b = 6
print("addition :", a + b)
print("subtraction :", a - b)
print("multiplication:", a * b)
print("division :", a / b)
print("floor division :", a // b)
print("modulus :", a % b)
print("power:", a ** b)

# Take two numbers from the user # Print all seven operations.
a=int(input("enter the 1st number :"))
b=int(input("enter the 2nd number :"))
print("addition :", a + b)
print("subtraction :", a - b)
print("multiplication:", a * b)
print("division :", a / b)
print("floor division :", a // b)
print("modulus :", a % b)
print("power:", a ** b)

# The user enters: # Monthly Salary
       # Print:
# Annual Salary
# Monthly Bonus (10%)
# Total Salary After Bonus
salary=int(input("ENTER YOUR MONTHLY SALARY:"))
annual= (salary * 12)
print(f"annual salary is : {annual}")
bonus= salary * (10/100)
print(f"monthly bonus is : {bonus}")
after_bonus = salary + bonus
print(f"total salary after bonus is : {after_bonus}")
annual_bonus= annual +( bonus * 12)
print(f"total annual salary after bonus is : {annual_bonus}")

# The user enters :  Total Students # Each classroom holds 30 students.
    # Print:
# Number of full classrooms
# Remaining students
enter=int(input("enter the total number of students :"))
students= 30
print("full classroom :", (enter//students) )
print("remaining students are :", (enter % students))

# movie ticket costs ₹250.
    # Ask the user:
# Number of tickets
   # Print:
# Total Price # If the customer buys 5 or more tickets, give a 10% discount.
cost= 250
tickets=int(input("enter the number of tickets you want to buy :"))
total_price= cost * tickets
discount= total_price - (total_price *(10/100))
if(tickets >= 5):
    print(f"total amount with discount is: {discount}")
    print(" enjoy your movie ")
else:
    print(f"total amount is : {total_price}")
    print(" enjoy your movie ")

              #  Comparison Operators
#   The comparison doesn't print a sentence—it gives a Boolean value:
print(10==10)
print(15 > 2)
print(8!=5)
print(7 <= 7)
print(100 < 50)
print(25 >= 25)

# Ask the user for their age.
      # Print:
# Eligible to Vote # or
# Not Eligible
age=int(input("ENTER YOUR AGE:"))
if(age>=18):
    print("you are eligible to vote ")
else:
    print("not eligible ")    

# Ask the user for a number.
   # Print:
# Positive
# Negative
# Zero
number=int(input("enter the number:"))
if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

# Ask the user for marks.
     # Print:
# A (90+)
# B (75–89)
# C (50–74)
# Fail (<50)

marks=int(input("enter the marks :"))
if(marks>=90):
    print("grade A")

elif(marks>=75):
    print("grade B")  

elif(marks>=50):
    print("grade c") 

else :
    print("FAIL")          


# Ask the user for a password.
# Store the correct password inside the program.
  # If it matches:
# Login Successful
#   # Otherwise:
# Wrong Password 
ask=input("ENTER THE PASSWORD:")
password= "Haapy1"
if(password == ask):
    print("login sucessfully")
else:
    print("wrong password")    