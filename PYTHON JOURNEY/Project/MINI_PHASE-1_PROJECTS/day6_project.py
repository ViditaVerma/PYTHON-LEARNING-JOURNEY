                                    # 🎓 Student Result System
                                    # 🐍 Day 6 Mini Project

# This combines:

# ✅ Functions
# ✅ Parameters
# ✅ Return
# ✅ if-else
# ✅ User Input
# Requirements

# Create 3 functions.

# Function 1
# get_grade(marks)
    # Return:
# A → 90+
# B → 75–89
# C → 50–74
# Fail → Below 50

# Function 2
# is_pass(marks)
   # Return:
# True
# if marks are 50 or above, otherwise
# False

# Function 3
# student_result(name, marks)

# It should print something like:

# ========== RESULT ==========
# Name  : Vidita
# Marks : 92
# Grade : A
# Status: Pass
# ============================
def get_grade(marks):
    if(marks>=90):
        return"GRADE A"
    elif(marks>=75):
        return"GRADE B"
    elif(marks>=50):
        return"GRADE C"
    else:
        return"fail"

def is_pass(marks):
    if marks>=50:
        return True
    else:
        return False

def student_result(name,marks):
    print("////////////////// RESULT /////////////////")
    print("NAME:", name)
    print("marks:", marks)
    print(f"GRADE: {get_grade(marks)} ")
    print("STATUS :",is_pass(marks))
    print("//////////////////////////////////////////////")

student_result("vidita", 94)
