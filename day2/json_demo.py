# JSON - JavaScript Object Notation
# What is JSON
# JSON is a universal data format used to store and transfer data. Every app you've ever used stores data in JSON somewhere.

# {
#     "name": "Sam",
#     "age": 22,
#     "skills": ["Python", "Git", "Linux"]
# }
# Looks exactly like Python dictionary that's why Python and JSON work so well together
# Why JSON over text file
# txt file - storing structured data is messy
# JSON - structured, clean, universal

# Every language - Pyton, Java script, Java, etc can read JSON. It's the universal language of data

import json
import os

# JSON Demo

# Writing a dictionary to JSON
student = {
    "name": "Sam",
    "age": 22,
    "city": "Mumbai",
    "marks": 85,
    "skills": ["Python", "Git", "Linux"],
    "is_employed": False
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file written!")

# Reading JSON back

with open("student.json", "r") as file:
    loaded = json.load(file)

print(loaded)
print(type(loaded))                 # <class 'dict'>
print(f"Name: {loaded['name']}")
print(f"Skills: {loaded['skills']}")

# List of dictionaries
students = [
    {"name": "Sam",   "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Rahul", "marks": 67},
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Students JSON written!")

# Reading list of dictionaries 
with open("students.json", "r") as file:
    loaded_students = json.load(file)   # json.load() reads the JSON file and converts back to Python dictionary automatically

print(f"Total students: {len(loaded_students)}")
for student in loaded_students:
    print(f"{student['name']}: {student['marks']}")

# Updating JSON
# Load modify save back
with open("students.json", "r") as file:
    students_data = json.load(file)

# Add a new student
students_data.append({"name": "Arjun", "marks": 78})

# Save back
with open("students.json", "w") as file:
    json.dump(students_data, file, indent=4)

print("\nAfter adding Arjun:")
with open("students.json", "r") as file:
    updated = json.load(file)

for student in updated:
    print(f"{student['name']}: {student['marks']}")

# Check if file exists before loading
filename = "unknown.json"
if os.path.exists(filename):
    with open(filename, "r") as file:
        data = json.load(file)
else:
    print(f"\n{filename} does not exist!")

# Always remember 
# json.dump(data, file)  - Python to JSON file
# json.load(file) - JSON file to Python

# same for string just instead of file write string
# json.dumps(data)  - Python to JSON string
# json.load(string) - JSON string to Python