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


                # Multiplication Table

# Ask the user to enter a number.

# Example:
# Enter a number: 7

# Output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
number=int(input("enter the number:"))
for  i in  range (1,11):
    print(f"{number} x {i} =", (number * i))
    # print(f"{number} x {i} = {number * i}")