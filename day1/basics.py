# VARIABLES & DATA TYPES
name = "Sam"    #string or texts are always written in onverted commas
age = 22
height = 5.10
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# TO CHECK DATA TYPES
print(type(name))           #These are the four building blocks of python
print(type(age))
print(type(height))
print(type(is_student))

# STRING OPERATIONS
name = "sam"

print(name.upper())             # Some of the methods you can do on strings 
print(name.title())
print(name.replace("s","S"))
print(len(name))

# f - strings 
age = 22                                                        # f-string looks cleaner or we can use "+" operator as well to concatinate 
print(f"My name is {name.title()} and I am {age} years old")

#String checks
email = "sam@gmail.com"             #Some more functions to be done on strings 
print(email.startswith("sam"))
print(email.endswith(".com"))
print("@" in email)


# USER INPUT

# Always remember that input is always a string if not specified 

name = input("Enter your name: ")
print(f"Hello {name}")

'''age = input("Enter your age: ")
print(age + 5)'''                  #This will throw an error 

#Two methods for solution
# 1
age = input("Enter your age: ")
age = int(age)                  #converting to integer
print(age + 5)


# 2
age = int(input("Enter your age: "))    #Does the same thing
print(age + 5)

# Conversions

#string to float

height = float(input("Enter your height: "))
print(f"Your height is {height}")

# integer to string
num = 100 
text = str(num)
print(type(text))

#Boolean conversions
print(int(True))    # 1
print(int(False))   # 0
print(bool(0))      # False
print(bool(1))      # True 
print(bool(""))     # False
print(bool("Sam"))  # True

# Empty string is always False 
# Any text is always True


# Practical example

# TO DO 
'''Ask user for two numbers
add them, subtract, multiply, divide,
print all results using f string'''

num1 = float(input("Enter the first number "))
num2 = float(input("Enter second number "))

Add = num1 + num2
print(f"The Addition of {num1} & {num2} is {Add}")

Sub = num1 - num2
print(f"The Substraction of {num1} & {num2} is {Sub}")

Mul = num1 * num2
print(f"The multiplication of {num1} & {num2} is {Mul}")

Div = num1 / num2
print(f"The Division of {num1} & {num2} is {Div}")


#Exercise 2
# Ask user for their name, age, and city
# Calculate what year they were born
# Print a sentence like:
# "Hi Sam! You are from Mumbai.
#  You were born in 2003.
#  In 10 years you will be 32 years old."


name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city name: ")

# Year they were born

year = 2026 - age 

# After 10 years they would be

year_10 = age + 10 

print(f"Hi {name}! You are from {city}")
print(f"You were born in {year}")
print(f"In 10 years you will be {year_10} years old.")



# CONDITIONALS

# Basic if/else
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Understanding all operators it always returns true or false 

print(10 > 5)   # True - greater than
print(10 < 5)   # False - less than
print(10 == 10) # True - equal to 
print(10 != 5)  # True - not equal to 
print(10 >= 10) # True Greater than or equal 
print(10 <= 9)  # False - less than or equal 


# IF - ELIF - ELSE
 # GRADE CALCULATOR

marks = int(input("Enter your marks (0 - 100): "))

if marks >= 90:
    grade = "A"
    message = "Outstanding!"
elif marks >= 75:
    grade = "B"
    message = "Very Good!"
elif marks >= 60:
    grade = "C"
    message = "Good"
elif marks >= 40:
    grade = "D"
    message = "Need improvement"
else:
    grade = "F"
    message = "Please study harder!"

print(f"Your grade is: {grade}")
print(f"{message}")


# AND OR NOT

age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ")

# AND - Both statements must be true 
if age >= 18 and has_id == "yes":
    print("Entry allowed")
else:
    print("Entry denied")

# OR at least ONE condition must be True
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendence %: "))

if marks >= 40 or attendance >= 75:
    print("Eligible to appear for exam")
else:
    print("Not eligible")

# NOT - reverse True/False
is_raining = False
if not is_raining:
    print("Go outside!")
else:
    print("Stay inside!")


# Nested if else 

# Loan elligibility checker
age = int(input("Enter age: "))
salary = int(input("Enter salary"))
credit_score = int(input("Enter credit score (300 - 900): "))

if age >= 21:
    if salary >= 25000:
        if credit_score >= 700:
            print("LOAN APPROVED")
        else:
            print("Loan denied - low credit score")
    else:
        print("Loan denied - salary too low")
else:
    print("Loan denied - must be 21 or older")

# EXERCISE 1

# Ask user for a number
# Print if positive / negative / zero
# Print if even / odd
# Print if divisible by both 3 and 5

num = int(input("Enter the number: "))  # input

# To determine Positive Negative and Zero
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Checking odd and even

if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")

# Check if the number is divisible by both 3 and 5 

if num % 3 == 0 and num % 5 == 0:
    print(f"The number {num} is divisible by both")
else:
    print("The number is not divisible by 3 and 5")

# Exercise 2 
# Create variables:
#correct_username = "sam"
#correct_password = "python123"

# Ask user to enter username and password
# If both match → print "Login successful! Welcome Sam"
# If username wrong → print "Username not found"
# If password wrong → print "Wrong password"

#username = input("Enter username: ")
#password = input("Enter password: ")


# Correct Password
correct_username = "sam"
correct_password = "python123"

# Input by the user
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful Welcome Sam")
    else:
        print("Wrong Password")
else:
    print("Username not found")

# Exercise 3

# A shop gives discounts based on purchase amount:
# Above 5000 → 20% discount
# Above 2000 → 10% discount
# Above 1000 → 5% discount
# Below 1000 → no discount

# Ask user for purchase amount
# Calculate and print final amount after discount

# #Input from user 

# amount = float(input("Enter purchase amount: ₹"))

# # conditional statements according to the questions
# if amount > 5000:
#     print("Congratulations! you got 20%\ discount")
#     print(f"Original billing amount {amount} final price after discount to be paid {amount * 20/100}")

# elif amount > 2000:
#     print("Congratulations! you got 10%\ discount")
#     print(f"Original billing amount {amount} final price after discount to be paid {amount * 10/100}")

# elif amount > 1000:
#     print("Congratulations! you got 5%\ discount")
#     print(f"Original billing amount {amount} final price after discount to be paid {amount * 5/100}")

# else:
#     print("Sorry no discount")
#     print(f"{amount} to be paid....")

# Input from user
amount = float(input("Enter purchase amount: ₹"))

# Conditional statements
if amount > 5000:
    discount = amount * 20 / 100
    final_price = amount - discount
    print(f"Congratulations! You got 20% discount")
    print(f"Original amount: ₹{amount}")
    print(f"Discount: ₹{discount}")
    print(f"Final price to be paid: ₹{final_price}")

elif amount > 2000:
    discount = amount * 10 / 100
    final_price = amount - discount
    print(f"Congratulations! You got 10% discount")
    print(f"Original amount: ₹{amount}")
    print(f"Discount: ₹{discount}")
    print(f"Final price to be paid: ₹{final_price}")

elif amount > 1000:
    discount = amount * 5 / 100
    final_price = amount - discount
    print(f"Congratulations! You got 5% discount")
    print(f"Original amount: ₹{amount}")
    print(f"Discount: ₹{discount}")
    print(f"Final price to be paid: ₹{final_price}")

else:
    print("No discount available")
    print(f"Amount to be paid: ₹{amount}")


# LOOPS
# For and while 

# Use for - when you know how many times repeat
# Use while - when we need to repeat until the condition becomes false
# Basic loop

for i in range (5): # prints: 0 1 2 3 4
    print (i)       # range(5) starts from 0 by default

# What is range 

# Range 

# In Python, range() is a built-in function used to generate a sequence of integers.

range (5)   # Print digit from 0 to 4
range (1,6) # Print digit from 1 to 5
range (0,11,2)  # Print digit form 0 to 11 with difference of 2... 0,2,4,6,8,10
range (10,0,-1) # Print digit form 10 to 1

# Range(Start, stop, step)

# looping through srting

for char in "Python":
    print(char)        # Prints each letter on a new line 

# Loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate 
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # 0: apple
    # 1: banana
    # 2: mango

# While loop

# Basic while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Real life example ATM PIN Checker
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter pin: ")
    if pin == correct_pin:
        print("Access granted!")
        break # Exit loop immediatly
    else:
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Wrong PIN. {remaining} attempts left.")

if attempts == 3:
    print("Card blocked!")


# Break and Continue statement
# Break - exits loop immediatly
# continue - skips the current iteration and keep going

# Break example

for i in range(10):
    if i == 5:
        break # stops when i reaches 5
    print(i) # prints: 0, 1, 2, 3, 4

# Continue example
for i in range(10):
    if i % 2 == 0:
        continue  # Skips even numbers
    print(i) # prints: 1, 3, 5, 7, 9

# Useful loop patterns 

# Pattern 1 - collecting results in a list
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares) # [1, 4, 9, 16, 25]

# Pattern 2 - summing numbers
total = 0
for i in range(1,101):
    total += i
print(f"Sum 1-100: {total}")    # 5050

# pattern 3 - finding something
numbers = [3, 7, 2, 9, 1, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest: {largest}")    # 9

# Pattern 4 - counting occurrences
sentence = "hello world how are you"
count = 0
for char in sentence:
    if char == "o":
        count += 1
print(f"Letter 'o' appears {count} times")

# Exercise 1

# Ask user for a number
# Print its multiplication table from 1 to 10
# Output should look like:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

num = int(input("Enter your number: "))
for i in range(1,11):
    a = num * i
    print(f"{num} x {i} = {a}")

# Exercise 2

# Print this pattern using loops:
# *
# **
# ***
# ****
# *****

height = int(input("Enter the height of the triangle: "))

for i in range(1,height + 1):
    print("*" * i)

# Exercise 3

# Secret number is 7
# Keep asking user to guess
# If guess is too high → print "Too high!"
# If guess is too low  → print "Too low!"
# If correct → print "Correct! You got it in X attempts!" and stop

secret_number = 7
attempts_1= 0

while True:
    guess = int(input("Enter your guess: "))
    attempts_1 += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts_1} attempts!")
        break

# Exercise 4 - FizzBuzz

# Print numbers 1 to 50
# But:
# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If divisible by both → print "FizzBuzz"
# Otherwise → print the number

for i in range(1,51):       # Range
    if i % 3 == 0 and i % 5 == 0: # Checking conditions
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Functions

# functions are of two types build in and user defined
# build in are print(), input(), int(), len(), range() etc

# without functions we need to write same thing every time we need 
# with function we can just call the function whenever we need 

# Write Once Use Anywhere

# Structure of a funcction

# def function_name(parameters):
#     # code here
#     return result

# def — keyword that defines a function
# function_name — what you call it (snake_case)
# parameters — inputs the function receives (optional)
# return — output the function gives back (optional)

# Different types of functions

# Type 1: No parameters, no return 

def greet():
    print("Hello Welcome to Python.")

greet() # calling the function
greet() # call it again - reusable!
greet() # and again!

# Type 2: With parameters

# parameters are the input you pass in 
def greet_user(name, age):
    print(f"Hello {name}! You are {age} years old.")

greet_user("Sam", 22)   # name="Sam", age=22
greet_user("priya", 19) # name="Priya", age=19 
greet_user("Rahul", 25) # name="Rahul", age=25 

# parameter vs argurment

# def greet_user(name, age): # name, age  are PARAMETERS (Defined in the function)

# greet_user("Sam", 22)   # "Sam", 22 are ARGURMENTS (Passed when calling)

# With Return Value

# return sends a value BACK to whoever called the function
def add(a,b):
    result = a + b
    return result

# The returned value can be stored or used directly
total = add(5,3)
print(total)            # 8
print(add(10,20))       # 30
print(add(100, 200))    # 300

# what happens withou return

def add_no_return(a, b):
    result = a + b
    # no return!

value = add_no_return(5,3)
print(value)    # None function returned nothing

# Type 4 default parameters

# Default value used when argurment not provided 
def greet_with_title(name, title = "Mr"):
    print(f"Hello, {title}. {name}!")

greet_with_title("Sharma")           # Hello, Mr. Sharma!
greet_with_title("Priya", "Ms")      # Hello, Ms. Priya!
greet_with_title("Kumar", "Dr")      # Hello, Dr. Kumar!

# Type 5 Multiple return values 

# Python can return multiple values at once 
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    return total, average, largest, smallest 

# Unpack all 4 returned values

total, avg, high, low = get_stats([10, 20, 30, 40, 50])
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Highest: {high}")
print(f"Lowest: {low}")         # Here python does't care about names it checks the position

# Exercise 1 

# Write a function is_even(n)
# Returns True if n is even, False if odd
# Test: is_even(4) → True
#       is_even(7) → False

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
# Exercise 2 

# Write a function calculator(a, b, operation)
# operation can be: "add", "subtract", "multiply", "divide"
# Return the result
# calculator(10, 2, "divide")   → 5.0
# calculator(5, 3, "add")       → 8
# calculator(10, 3, "subtract") → 7

def calculator(a, b, operation):
    if operation == "divide":
        result = a/b
        return result
    elif operation == "add":
        result = a + b
        return result
    elif operation == "multiply":
        result = a * b 
        return result
    elif operation == "subtract":
        result = a - b
        return result
    else:
        print("Enter valid operetion from add or subtract or multiply or divide")

# Exercise 3 String function

# Write a function check_palindrome(word)
# A palindrome reads same forwards and backwards
# "racecar" → True
# "hello"   → False
# Hint: word == word[::-1]  reverses a string

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
# Exercise 4
# Write a function calculate_bmi(weight_kg, height_m)
# BMI = weight / (height * height)
# If BMI < 18.5  → print "Underweight"
# If BMI < 25    → print "Normal"
# If BMI < 30    → print "Overweight"
# else           → print "Obese"
# Also return the BMI value

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg/(height_m * height_m)

    if bmi < 18.5:
        print("Underweight")
        return bmi
    elif bmi < 25:
        print("Normal")
        return bmi
    elif bmi < 30:
        print("Overweight")
        return bmi
    else:
        print("Obese")
        return bmi
    

# DSA
# LIST
# The most used data sturcture in Python. Like an array that can hold anything

students = ["Sam", "Priya","Rahul","Arjun"]

# Acessing items - indexing starts at 0
print(students[0]) # Sam - First item
print(students[-1]) # Arjun - last item
print(students[1:3]) # ['Priya', 'Rahul'] - Slicing

# Modifying 
students.append("Neha")     # add to end 
students.insert(1, "Kiran") # add at index 1
students.remove("Rahul")    # remove by value
students.pop()              # removes last item
students.pop(0)             # removes at index 0

# Useful operations
print(len(students))        # Length
print(sorted(students))     # sorted copy
print(students.count("Sam"))# count occurrences
print("Sam" in students)    # check if exists True/False

# looping
for student in students:
    print(student)

# loop with index
for index, student in enumerate(students):
    print(f"{index + 1}. {student}")

# List of numbers
numbers = [5, 2, 8, 1, 9, 3]
print(min(numbers)) # 1
print(max(numbers)) # 9
print(sum(numbers)) # 28
numbers.sort()      # sort in place
print(numbers)      # [1, 2, 3, 5, 8, 9]


# List comprehension

# Normal way
squares = []
for i in range(1, 6):
    squares.append(i**2)

# List comprehension way - same result
squares = [i**2 for i in range (1,6)]
print(squares) # [1, 4, 9, 16, 25]

# with condition
evens = [i for i in range (20) if i % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8, 10, 12, 16, 18]

# Real world example
names = ["sam", "priya", "rahul", "arjun"]
upper_names = [names.upper() for name in names]
print(upper_names)  # ['SAM', 'PRIYA', 'RAHUL', 'ARJUN']


# TUPLE
# Like list but locked - cannot be changed after creation

coordinates = (28.6, 77.2)     # Latitude, longitude
rgb = (255, 128, 0)             # color values
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Accessing - same as list
print(coordinates[0])   # 28.6
print(days[-1])         # Sun
print(days[0:5])        # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Cannot modify - this will throw an error
# coordinates[0] = 10 # Type error 

# Why use tupples?
# 1. Data that should never change
# 2. Faster than lists
# 3. Can be used as dictionary keys 

# Unpacking
lat, lon = coordinates
print(f"Latitude:{lat}, Longitude:{lon}")

# Tuple with one item needs a comma 
single = (42, ) # Tuple
not_tuple = (42)   # This is just a number in brackets

# Dictionary
# Key value pairs. Like a real dictionary - word(key) and meaning(value)

student = {
    "name": "Sam",
    "age": 22,
    "city": "Mumbai",
    "marks": 85,
    "subjects": ["Python", "DSA", "Networking"]
}

# Accessing values
print(students["name"])         # Sam
print(student.get("age"))       # 22
print(student.get("phone", "Not found"))    # Not found - safe!

# Never use [] for accessing if key might not exist
# student["phone"] # KeyError crash!
# student.get("phone", "Not found") # Safe

# Adding and updating
student["email"] = "sam@gmail.com"  # add new key
student ["age"] = 23                # update existing 

# Removing
del student["city"]             # delete a key
popped = student.pop("marks")   # remove and return value
print(popped)                   # 85

# Looping
for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

print(student.keys())   # all keys
print(student.values()) # all values

# Check if key exists
if "name" in student:
    print("Name exists!")

# Nested dictionary
company = {
    "name": "Techcorp",
    "location": "Banglore",
    "employees": {
        "CEO": "Rahul",
        "CTO": "Priya",
        "Developer": "Sam"
    }
}

print(company["employees"]["CTO"])  # Priya

# SET
# Unordered collection - no duplicates ever

tags = {"python", "coding", "python", "dsa", "coding"}
print(tags)     # {'Python', 'coding', 'dsa'} - duplicates gone!

# Adding and ramoving
tags.add("linux")
tags.remove("dsa")
tags.discard("html")    # remove if exists, no error if not

# check membership - faster than list 
print("python" in tags) # True

# Set operation - very powerful
skills_required = {"Python", "sql", "linux", "git"}
my_skills = {"python", "git", "javascript"}


# What skills do I have that are required?
matched = skills_required & my_skills
print(f"Missing skills: {matched}")     # {'sql', 'linux'}

# All skills combined
all_skills = skills_required | my_skills
print(f"All skills: {all_skills}")

# Remove duplicates from a list using set
numbers = [1, 2, 2, 3, 3, 3, 4, 4]
unique  = list(set(numbers))
print(unique)   # [1, 2, 3, 4]


# Exercise 1 

# Create a list of 5 student names
# Sort them alphabetically
# Print only names longer than 4 characters
# Print the list in reverse order

names = ["Sam", "Priya","Rahul","Arjun", "Rohit"]
names.sort()

for name in names:
    if len(name) > 4:
        print(name)

names.reverse()
print(names)

# Exercise 2 Dictionary:

# Create a dictionary for yourself:
# name, age, city, skills (list), is_employed
# Write a function called print_profile(person)
# that takes this dictionary and prints:
# "Name: Sam
#  Age: 22
#  City: Mumbai
#  Skills: Python, Git, Linux
#  Status: Looking for work"  ← based on is_employed


# Creation of dictionary
person = {
    "name": "Sam",
    "age": 22,
    "city": "Mumbai",
    "skills": ["Python", "Git", "Linux"],
    "is_employed": False
}

# Defining of function
def print_profile(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print(f"Skills: {', '.join(person['skills'])}")

    if person["is_employed"]:
        status = "Employed"
    else:
        status = "Looking for work"

    print(f"Status: {status}")

# Calling of function
print_profile(person)

# Exercise 3 - Real world combo

# You have a list of students (list of dictionaries)
students = [
    {"name": "Sam",   "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Rahul", "marks": 67},
    {"name": "Arjun", "marks": 45},
    {"name": "Neha",  "marks": 78},
]

# 1. Print all student names and marks
# 2. Find and print the topper (highest marks)
# 3. Print names of students who passed (marks >= 60)
# 4. Calculate and print class average

# Printing all names and marks 
for student in students:
    print(f"{student['name']}: {student['marks']}")

# finding topper
topper = students[0]    # Assume first students is topper

for student in students:
    if student["marks"] > topper["marks"]:
        topper = student # Found someone better, update topper

print(f"\nTopper: {topper['name']} with {topper['marks']} marks")

# Students who passed

for student in students:
    if student["marks"] >= 60:
        print(f"{student['name']}: {student['marks']}")

# Class average

total = 0 
for student in students:
    total += student["marks"]

average = total / len(students)
print(f"\nClass Average: {average}")
