           # ⭐ Mini Project
           # ATM PIN Verification

# Requirements:

# Correct PIN = 1234
# User gets 3 attempts
# If PIN is correct:
# Print "Access Granted"
# Stop the loop
# If wrong:
# Print "Wrong PIN"
# After 3 wrong attempts:
# Print "Card Blocked"

# This project combines:

# while
# if
# break
# Counting attempts
attempt=0
while True:    
 pin=int(input("ENTER THE ATM PIN :"))
 if pin == 1234:
  print("ACCESS GRANTED")
  break
 attempt += 1
 if pin != 1234:
  print("WRONG PIN ")
 if attempt == 3:
   print("CARD BLOCK")
   break

