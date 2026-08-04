# Write a function named: # greet()
   # It should print:
# Hello Vidita!
# Welcome to Python Journey.
# Let's become a Python Developer.

# Then call it 3 TIMES

def greet():
    print("Hello vidita")
    print("Welcome to python journey")
    print("Lets become a python developer")

greet()    
greet()    
greet()    

# Create another function: # motivation()
# It should print 3 motivational lines of your choice.
# Then call it 2 times.
def motivation():
    print("discipline is the only way ")
    print('WHAT YOU DO YOU GET, IF YOU DO NOTING NOTHING HAPPEN ')

motivation()    
motivation()    

# Create a function: # student(name)
# Output:
# Welcome Vidita
def student(name):
    print(f"hello {name}")

student("vidita")    
student("rahul")    
student("krishna")    

# Create: # square(number)
# If you call:
# square(5)
def square(number):
    print("square", number*number)
square(3)
square(4)
square(5)

# reate: # def add(a, b):
# It should return the sum.
def add(a,b):
 return a + b
answer=add(4,5)
print(answer)
add(9,5)
add(8,5)
add(5,5)

# Create: # def is_even(number):
# If the number is even,
# Return: # True
# Otherwise return: # False
def is_even(number):
   if number % 2 == 0:
      return True
   else:  
    return False
print(is_even(2))   
print(is_even(10))   