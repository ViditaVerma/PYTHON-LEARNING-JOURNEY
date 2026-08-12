# Q1.Create a class named Student.
  # Then create two objects:
# student1
# student2
class student:
    pass
student_a=student()
student_b=student()

# Create a Student class with:  name, age
# Use __init__() to store these values.

# Then create:
# student1 → Vidita, 21
# student2 → Rashi, 22
# Finally print both students' names and ages.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


student1=student("vidita",21)        
student2=student("krish",22)

print(student1.name, student1.age)
print(student2.name, student2.age)

# Create a Student class with:
# name
# course

# Use __init__() and self to store both values.
# Create:
# student1 → Vidita, Python
# student2 → Rashi, SQL

# Then print each student's name and course.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
studentt=student("vidita",23)
print(studentt.name,studentt.age)        

#  Create a Student class with: name
# a method called introduce()

# The introduce() method should print: 
# Create one student object and call the method.
class student:
    def __init__(self,name):
        self.name=name
    def introduce(self):  
        print(f"hello my name is {self.name}")  
student2=student("vidita")
print(student2.name)        
student2.introduce()        

# Create a class called Employee.
   # Requirements:
# Use __init__() to store:
# name
# role
# salary
# Create a method called show_details() that prints all three details.
# Create two employee objects with different details.
class employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    def show_details(self):
        print(f"name  :{self.name}")    
        print(f"role  :{self.role}")    
        print(f"salary:{self.salary}")  

employee1=employee("vidita","HR manager",25000) 
employee1.show_details()        
employee2 = employee("Rashi", "Data Analyst", 40000)
employee2.show_details()