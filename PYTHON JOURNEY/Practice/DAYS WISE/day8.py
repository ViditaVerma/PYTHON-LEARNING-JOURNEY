# Q1  # Create a tuple of 5 fruits.
    # Print:
# First fruit
# Last fruit
# Total fruits
fruits=("apple","mango","orange","kiwi","watermellon")
for i in fruits:
    print(i)

print(fruits[0] )
print(fruits[-1] )
print(len(fruits ))

# Q2 # Create: # numbers = (10,20,30,40,50)

# Print:
# Index 2
# Index -2

numbers = (10,20,30,40,50)
print(numbers[2])
print(numbers[-2])

# Q3 # Create a tuple of your favorite movies.  
# Print all movies using a for loop.
movies=("pavane","my name","spiderman","moana")
for i in movies:
    print(i)

# Q1 # Create a dictionary
#  name
# age
# city
# Print all three values separately.
info={"name":"vidita",
      "age":21,
      "city":"new delhi "}
print(info["name"])
print(info["age"])
print(info["city"])

# Q2 # Create
# car = {
# "brand":"BMW",
# "model":"X5",
# "year":2024
# }
      # Print
# Brand
# Model
car = {
"brand":"BMW",
"model":"X5",
"year":2024
}
print(car["brand"])
print(car["model"])

# Q3  Create
# book = {
# "title":"Atomic Habits",
# "author":"James Clear"
# }
   # Add
# price : 499
# Print the dictionary.
book = {
"title":"Atomic Habits",
"author":"James Clear"
}
book["price"]=499
print(book)

            #   Dictionary Methods
#Q1 # student = {
#     "name": "Vidita",
#     "age": 21,
#     "city": "Delhi" }
  # Print:
# All keys
# All values
# All items
student = {
    "name": "Vidita",
    "age": 21,
    "city": "Delhi"
}
print(student.keys())
print(student.values())
print(student.items())

# Print only the values.
print(student.values())

# Q3
# car = {
#     "brand": "BMW",
#     "model": "X5"
# }

# Use get() to print:
# brand
# year
car = {
    "brand": "BMW",
    "model": "X5"
}
print(car.get("brand"))
print(car.get("year"))

# Q1
# student = {
#     "name": "Vidita",
#     "age": 21,
#     "city": "Delhi"
# }

# Print only the keys using a loop.
student = {
    "name": "Vidita",
    "age": 21,
    "city": "Delhi"
}
for key in student:
    print(key)

# Print only the values using a loop.
for value in student.values():
    print(value)

# Print in this format:
# name : Vidita
# age : 21
# city : Delhi

# using .items().    
for key,value in student.items():
    print(key, ":", value)  

# ///////////////////////////////// SETS////////////////////
# Q1  Create a set of 5 colors.
# Print the set. 
colors={"red","green","orange","yellow","pink"}
for i in colors:
    print(i)   
# ADD THE NEW COLOR
colors.add("blue")
print(colors)
#REMOVE ANY COLOR  by remove()
colors.remove("green") # we can also use discard() same as remove but dosnt give error when elemet is not in the set 
print(colors)
# remove color by discard()
colors.discard("magenta")
print(colors)

# Q. subjects = {"Python", "SQL", "Excel"}

# Print the total number of subjects.
subjects = {"Python", "SQL", "Excel"}
print(len(subjects))

# Use a loop to print each data
numbers = {1, 2, 2, 3, 3, 4} # set didnt give duplicate values 
for i in numbers:
    print(i)
#  UNION() ,INTERSECTION()  AND DIFERRENCE() METHOD OF SETS

#     Q1
# A = {10, 20, 30}
# B = {30, 40, 50}

# Print the union.

A = {10, 20, 30}
B = {30, 40, 50}
print(A.union(B))

# Using the same sets,
# Print the intersection
print(A.intersection(B))

# Using the same sets,
# Print:diferrence()
print(A.difference(B))

print(B.difference(A))

                    # ⭐ Challenge
# python_students = {"Vidita", "Rahul", "Aman", "Priya"}

# sql_students = {"Rahul", "Priya", "Rohit", "Vidita"}

# Print:

# All students (union)
# Students learning both (intersection)
# Students learning only Python
# Students learning only SQL

python_students = {"Vidita", "Rahul", "Aman", "Priya"}
sql_students = {"Rahul", "Priya", "Rohit", "Vidita"}
print("ALL STUDENTS IN BOTH BATCH :", python_students.union(sql_students))
print("STUDENT LEARNING BOTH PYTHON AND SQL :", python_students.intersection(sql_students))
print("STUDENT LEARNING ONLY PYTHON :", python_students.difference(sql_students))
print("STUDENT LEARNING ONLY SQL:", sql_students.difference(python_students))

# customer id is list and i are not uique so if we have to make it unique
# we convert it into sets
customer_ids = [101,102,101,103,102,104,105,104]
# converstion
unique_customers = set(customer_ids)
print(unique_customers)