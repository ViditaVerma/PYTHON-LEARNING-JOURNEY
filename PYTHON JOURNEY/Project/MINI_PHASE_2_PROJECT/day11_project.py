            # 📁 Mini Project: Skills Tracker
# Task
# Create a Python program that allows the user to maintain a file called skills.txt.

# The program should:

# Ask the user to enter 3 skills.
# Store those skills in a list.
# Write them to skills.txt using writelines().
# Ask the user to enter 2 more skills.
# Append those skills to the same file using "a" mode.
# Finally, open the file using "r" mode.
# Use a for loop to print each skill separately.
p_skills=[]
i=0
for i in range(3):
    skill=input("ENTER SKILL:")
    p_skills.append(skill + "\n")

with open("skill.txt","w") as files:
    files.writelines(p_skills)
more_skills=[]
for i in range(2):
    skill=input("ENTER  ANOTHER SKILL:")  
    more_skills.append(skill + "\n")

with open("skill.txt","a") as files:
    files.writelines(more_skills)    

with open("skill.txt","r") as files:
    for lines in files:
        print(lines)

         