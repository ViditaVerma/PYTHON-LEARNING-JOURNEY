# Q1 # name = "Python"
    # Print:
# First character
# Last character
# Length
name="python"
print(name[0])
print(name[-1])
print(len(name))

# Q2
# city = "New Delhi"

# Print:

# First 3 characters
# Last 5 characters (using slicing)
# Full string
city = "New Delhi"
print(city[0:3])
print(city[4:9])
print(city[:])

# Q3 # course = "Data Analyst"
# Print:
# First word only
# Last word only
course = "Data Analyst"
print(course[0:4])
print(course[5:12])

# Q4 # movie = "Interstellar"
   # Print:
# First character
# Middle 5 characters
# Last character
movie = "Interstellar"
print(movie[0])
print(movie[4:9])
print(movie[-1])

# Q1
# name = "vidita verma"
   # Print:
# Uppercase
# Title Case
# Capitalize
name = "vidita verma"
print(name.upper())
print(name.title())
print(name.capitalize())

# Remove the extra spaces
text = "     Python Developer     "
print(text.strip())
print(text.find("e"))
# Finds the index of the first occurrence.
text = "Python Developer"
print(text.find("e"))

# Counts how many times a character or word appears.
print(text.count("e"))

# Q3
sentence = "I love Excel"
# Replace Excel with SQL.
print(sentence.replace("Excel","SQL"))

# Q4 # word = "Mississippi"
# Print:
# Index of first "s"
# Number of "s"
word="Mississippi"
print(word.find("s"))
print(word.count("s"))

# Q5 ⭐ Challenge
# message = "    hello python world    "
# Print the output as:  HELLO PYTHON WORLD
message = "    hello python world    "
print(message.strip().upper())

# Q1
# email = "vidita@gmail.com"
   # Print:
# Does it end with .com?
# Does it start with "vidita"?
email = "vidita@gmail.com"
print(email.endswith(".com"))
print(email.startswith("vidita"))

# Q2 # Print:
# Does it end with .pdf?
# Does it end with .docx?
filename = "report.pdf"
print(filename.endswith(".pdf"))
print(filename.endswith(".docx"))

# Q3
# website = "https://openai.com"
    # Print:
# Does it start with "https"?
# Does it start with "http"?
website = "https://openai.com"
print(website.startswith("https"))
print(website.startswith("http"))

# ⭐ Mini Challenge

# Without using if-else, print whether this email is valid based on whether it ends with .com.

# email = input("Enter email: ")

email = input("Enter email: ")
print(email.endswith(".com"))