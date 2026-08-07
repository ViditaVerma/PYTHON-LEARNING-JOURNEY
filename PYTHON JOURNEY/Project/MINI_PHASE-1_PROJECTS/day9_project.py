           # 📋 Requirements

# Ask the user to enter:  Enter your full name:
# Store it in a variable called name.

# Then print a report like this:
# ========== STRING REPORT ==========
# Original Name :
# Uppercase :
# Lowercase :
# Title Case :
# Capitalize :
# Length :
# Starts with A? :
# Ends with a? :
# First index of 'a' :
# Number of 'a' :
# ===================================

             # ⭐ Bonus Part

# Ask the user to enter a sentence. # Enter a sentence:
   # Then:
# Replace "Python" with "SQL"
# Print the updated sentence.

            # ⭐⭐ Bonus Challenge
# Ask the user to enter an email. Enter your email:

# Print:
# Valid Email : True
# or
# Valid Email : False
# (No if-else.)
original_name=input("ENTER YOUR FULL NAME :")
print("========= STRING REPORT ==============")
print("ORIGINAL NAME     :", original_name)
print("UPPERCASE         :", original_name.upper())
print("LOWERCASE         :", original_name.lower())
print("TITLE CASE        :", original_name.title())
print("CAPITALIZED       :", original_name.capitalize())
print("START WITH a?     :", original_name.startswith("A"))
print("LENGTH            :", len(original_name))
print("END WITH a ?      :", original_name.endswith("a"))
print("FIRST INDEX OF a  :", original_name.find("a"))
print("NUMBER OF a       :", original_name.count("a"))
print("=============================================")

for i in range(2):
 bonus=input("ENTER A SENTENCE :").lower()
 print(bonus.replace("python","sql"))
 print("sorry for the  PRANK !!!!!")

EMAIL=input("ENTER YOUR EMAIL: ")
print("valid email :",EMAIL.endswith(".com"))