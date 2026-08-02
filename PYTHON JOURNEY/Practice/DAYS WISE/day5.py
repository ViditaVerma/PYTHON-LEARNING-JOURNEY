                  # while loop 
   # Print numbers
# 1
# 2
# 3
# 4
# 5
count = 1 
while count <= 5:
    print(count)
    count += 1

# Q2 # Print
# 10
# 9
# 8
# ...
# 1
# using a while loop.
count=10
while count >=1:
    print(count)
    count -= 1

# Ask the user: # Enter password:
# Keep asking until the user enters # python123
  # Then print
# Login Successful    
while True:
 password = input("enter the password:")

 if password == "python123":
   print("login sucessful")
   break
 print("wrong password")

# Q4
# Print numbers from 1 to 10.
# Skip 5.
# (Hint: Use continue.) 
count= 1
while count <= 10:
  if count == 5:
     count += 1
     continue 
print(count)
count += 1