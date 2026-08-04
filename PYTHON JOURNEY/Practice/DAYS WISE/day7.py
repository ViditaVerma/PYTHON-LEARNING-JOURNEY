# Q1
# Create a list of 5 fruits.
# Print all fruits one by one using indexing.
fruit_list=["orange","mango","banana","apple","kiwi"]
print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])
print(fruit_list[3])
print(fruit_list[4])

# Create a list: # numbers = [10, 20, 30, 40, 50]
    # Print:
# First element
# Last element
# Third element
numbers = [10,20,30,40,50]
print(numbers[0])
print(numbers[4])
print(numbers[-1])
print(numbers[2])

# Q3 # Create a list of your favorite movies.
# Replace the third movie with another one.
#  Print the updated list.
fav_movies=["my name","pavane","escape rooom","liitle forest"]
print(fav_movies)
fav_movies[2]="spider man"
print(fav_movies)

# Q4 # Create a list of 5 cities.
   # Print:
# First city
# Last city
# Total number of cities
cities=["NEW DELHI","MUMBAI","KOLKATA","BANGALORE","CHENNAI"]
print(cities[0])
print(cities[-1])
print(len(cities))
#  ////////////////////////////    PART2     ////////////////////
# Q1 # fruits = ["Apple", "Banana"]
   # Add:
# Mango
# Orange

# using append()
fruits = ["Apple", "Banana"]
fruits.append("mango")
fruits.append("orange")
print(fruits)

# Q2 # numbers = [10, 20, 40, 50]
# Insert: # 30 # at index 2.
numbers = [10, 20, 40, 50]
numbers.insert(2,30)
print(numbers)

# Q3  colors = ["Red", "Blue", "Green", "Yellow"]
#  Remove: Green  using remove()
colors = ["Red", "Blue", "Green", "Yellow"]
colors.remove("Green")
print(colors)

# Q4 # cities = ["Delhi", "Mumbai", "Kolkata", "Chennai"]
#  Remove the last city using pop().
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai"]
cities.pop(-1)
print(cities)

# Q5 ⭐ Challenge
# animals = ["Dog", "Cat", "Lion"]

# Perform these operations in order:
# Append "Tiger"
# Insert "Rabbit" at index 1
# Remove "Cat"
# Pop the last element
animals = ["Dog", "Cat", "Lion"]
animals.append("tiger")
print(animals)
animals.insert(1,"rabbit")
print(animals)
animals.remove("Cat")
print(animals)
animals.pop(-1)
print(animals)

# //////////////////////// PART 3 ////////////////////////
# Q1 # numbers = [8, 2, 6, 1, 9]
# Sort the list.
numbers = [8, 2, 6, 1, 9]
numbers.sort()
print(numbers)
# Q2  names = ["Vidita", "Rahul", "Aman"]
#  Reverse the list.
names = ["Vidita", "Rahul", "Aman"]
names.reverse()
print(names)

# Q3 # subjects = ["Python", "SQL", "Excel", "Power BI"]
  # Check:
# "SQL" is in the list.
# "Java" is not in the list.
# Print both results.
subjects = ["Python", "SQL", "Excel", "Power BI"]
print("SQL" in subjects)
print("JAVA" not in subjects)

# Q4 ⭐
# colors = ["Red", "Blue", "Green", "Yellow"]
# Use a for loop to print each color.
colors = ["Red", "Blue", "Green", "Yellow"]
for rang in colors:
    print(rang)

# Q5 ⭐⭐ (Challenge)
# marks = [90, 85, 70, 95, 88]

# Using a for loop:
marks = [90, 85, 70, 95, 88]
for num in marks:
    print(num,"passed")
