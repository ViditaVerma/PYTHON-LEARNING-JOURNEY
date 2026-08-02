# Ask:
  # Age
  # Has ID (True/False)
# Print:
# Eligible
# Not Eligible
age = int(input("enter your age : "))
has_id = input("DO you have ID? :").lower()
if(age >= 18 and has_id=="yes"):
    print("you are eligible")
else:
    print("not eligible ")    

# Q2 # Ask:
# # Student?
# Coupon?
   # If either is True:
# Print:
# Discount Available    
is_student = input("are you a student?(yes/no) :").lower()
have_coupon = input("do yoy have coupon ?(yes/no) :").lower()
if(is_student == "yes" or have_coupon == "yes"):
    print("discount available!!")
else:
    print("sorry no discount available.") 

# Ask:
# logged_in = False
# Use not.
  # Print:
# Please Login 
logged_in= input("are you login ? (yes/no) ").lower()
if not (logged_in == "yes"):
    print("please login")
else:
 print("welcome")       

               #  Mini Project
# Bank ATM Access

 # Conditions:
# Age ≥ 18
# Correct PIN
# Account Active

 # Only if all are true: # Access Granted
 # Else: # Access Denied

print("WELCOME TO OUR BANKS")
age= int(input("enter your age :"))
entered_pin = int(input("enter your pin :"))
acc_status =input("enter your account status (active/not active) :")
if(age >= 18 and entered_pin == 1111 and acc_status == "active"):
    print("✅ access granted  ✅")
else:
    print("access denied , go to customer support service ")    

                              # loop concept
 # Q1
# Print "Hello Python" 5 times.
for i in range(5):
    print("HELLO PYTHON")
# Q2
# Print numbers from 1 to 10.
for i in range(1,11):
    print(i)
# Q3
# Print even numbers from 2 to 20.
for i in range(2,21,2):
  print(i)    
# Q4
# Print odd numbers from 1 to 19.
for i in range(1,20,2):
    print(i)
# Q5
# Print numbers from 10 to 1 (countdown).
for i in range(10,0,-1):
  print(i)