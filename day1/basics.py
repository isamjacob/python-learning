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