python_students = {"Vidita", "Rahul", "Aman", "Priya"}
sql_students = {"Rahul", "Priya", "Rohit", "Vidita"}
print("ALL STUDENTS IN BOTH BATCH :", python_students.union(sql_students))
print("STUDENT LEARNING BOTH PYTHON AND SQL :", python_students.intersection(sql_students))
print("STUDENT LEARNING ONLY PYTHON :", python_students.difference(sql_students))
print("STUDENT LEARNING ONLY SQL:", sql_students.difference(python_students))