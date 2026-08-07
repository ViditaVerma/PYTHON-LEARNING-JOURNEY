               # Student Information System

 # Take these inputs:
# Name
# Age
# College
# Course
# City
# CGPA

  # Display the output like this:

# ========== STUDENT DETAILS ==========

# Name    : Vidita Verma
# Age     : 21
# College : GGSIPU
# Course  : BCA
# City    : Delhi
# CGPA    : 9.5

# =====================================

      # Use:
# input()
# int()
# float()
# f-strings

NAME=input("enter your NAME: ")
AGE=int(input("enter your AGE : "))
COLLEGE=input("enter your COLLEGE : ")
COURSE=input("enter your COURSE : ")
CITY=input("enter your CITY : ")
CGPA=float(input("enter your CGPA : "))

print("============== STUDENT DETAILS =============")
print(f"NAME    :{NAME}")
print(f"AGE     :{AGE}")
print(f"COLLEGE :{COLLEGE}")
print(f"COURSE  :{COURSE}")
print(f"CITY    :{CITY}")
print(f"CGPA    :{CGPA}")
print("=============================================")
                    #  this can be written as this also 
print("============== STUDENT DETAILS ============="
  f"NAME    :{NAME}"
  f"AGE     :{AGE}"
  f"COLLEGE :{COLLEGE}"
  f"COURSE  :{COURSE}"
  f"CITY    :{CITY}"
  f"CGPA    :{CGPA}"
  "=============================================")

