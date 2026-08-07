
# 🛒 Mini Project: Student Course Enrollment System
students=[]
# new_student="yes"
print("======================================")
print("      COURSE ENROLLMENT SYSTEM        ")
print("=======================================")
name=input("ENTER STUDENT NAME:")
age=input("ENTER STUDENT AGE :")
courses=set()

attempt="yes"
while attempt=="yes":
 course=input("ENTER COURSE:")
 courses.add(course)
 print("course added sucessfully")
 attempt=input("want to add another course ? (yes/no)").lower()
student={"NAME":name,
          "AGE":age,
          "COURSE":courses}
students.append(student)
print("=========================================")
print("          STUDENT REPORT                 ")
print("=========================================")
print("NAME   :",student["NAME"])
print("AGE    :",student["AGE"])
print("COURSES :",student["COURSE"])
print("TOTAL COURSE:",len(courses))



# 🏫 Student Management System (Phase 1 Final Project)
#      Features
# Add a student
# Store Name
# Store Age
# Store Course
# Store Marks
# Calculate Grade
# Pass/Fail Status
# Remove Duplicate Courses using Sets
# Search Student Information
# Display All Students
# Count Total Students
students=[]
def grade(marks):
 if marks >=90 :
   return "A"
 elif marks>=75:
   return "B+"
 elif marks >=50:
   return "B"
 else:
   return "C"

def status(marks):
  if marks>=50:
    return "pass"
  else: 
    return "fail"
  
another="yes"
while another=="yes":   
 print("===========================================")
 print("        STUDENT MANAGEMENT SYSTEM       " )
 print("===========================================")
 name=input("ENTER YOUR NAME :")
 age=int(input("ENTER YOUR AGE : "))
 course=input("ENTER YOUR COURSE:").title()
 marks=int(input("ENTER YOUR MARKS:"))
 print("==============================================")
  

 student={"NAME":name ,
 "AGE":age,
 "COURSE":course,
 "MARKS":marks,
 "GRADE": grade(marks),
 "Status": status(marks)}

 students.append(student)
 print(students)

 
 print("===========================================")
 print("             STUDENT REPORT         ")
 print("===========================================")
 print("NAME    :",name)
 print("AGE     :",age)
 print("COURSE  :",course)
 print("MARKS   :",marks)
 print("GRADE   :",grade(marks))
 print("Status  :",status(marks))
 print("=============================================")

 another=input("would you like to add another student?(yes/no) :").lower() 

passed = 0
failed = 0
courses = set()

for student in students:
    print("---------------------------------------")
    print("NAME   :", student["NAME"])
    print("AGE    :", student["AGE"])
    print("COURSE :", student["COURSE"])
    print("MARKS  :", student["MARKS"])
    print("Grade  :", student["GRADE"])
    print("Status :", student["Status"])


    courses.add(student["COURSE"])

    if student["Status"] == "pass":
        passed += 1
    else:
        failed += 1


print("\n===========================================")
print("SUMMARY")
print("===========================================")

print("Total Students :", len(students))
print("Passed         :", passed)
print("Failed         :", failed)
print("Unique Courses :", courses)

print("===========================================")
  
  


  