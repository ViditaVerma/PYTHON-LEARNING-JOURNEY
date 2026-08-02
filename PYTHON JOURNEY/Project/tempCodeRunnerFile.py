attempt=1
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