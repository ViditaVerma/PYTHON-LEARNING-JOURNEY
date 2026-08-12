     # 🧩 Mini Challenge — Student Management

# Create a class called Student.

# Requirements:

# Store:
# name
# course
# marks
# Create a method show_result() that:
# prints student's name and course
# prints PASS if marks ≥ 50
# otherwise prints FAIL
# Create 2 students with different marks.
class student:
    def __init__(self,name,course,marks):
        self.name=name
        self.course=course
        self.marks=marks
    def show_result(self):
        print(f"name  :{self.name}")   
        print(f"course:{self.course}") 
        print(f"marks:{self.marks}") 
        if(self.marks >= 50):
            print("result: PASS")  
        else:
            print("FAIL")  

student1=student("vidita",'python',90)             
student2=student("krishna","sql",91) 
student2=student("bhima","python",40) 
student1.show_result()
student2.show_result()
            