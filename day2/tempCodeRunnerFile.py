# Modules

# import random
# import datetime
# import math
# import os
# import sys

# # Random module
# print("Random")

# # Random integer between 1 and 10
# print(random.randint(1, 10))

# # Random float between 0 and 1
# print(random.random())

# # Random choice from list
# fruits = ["apple","banana","mango","grape"]
# print(random.choice(fruits))

# # Shuffle list
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)

# # Random sample - pick 3 unique items
# print(random.sample(fruits, 2))

# # Date and Time module

# print("\n DATETIME")

# # Current date and time
# now = datetime.datetime.now()
# print(now)
# print(type(now))

# # Formatted date
# print(now.strftime("%d/%m/%Y"))  # 13/05/2026
# print(now.strftime("%d-%m-%Y %H:%M"))   # 13-05-2026 14:30
# print(now.strftime("%A, %B, %d, %Y")) # Wednesday, May 13 2026

# # Specific parts
# print(f"Year: {now.year}")
# print(f"month: {now.month}")
# print(f"Day: {now.day}")
# print(f"Hour: {now.hour}")
# print(f"Minute: {now.minute}")

# # Date arithmetic 
# today = datetime.date.today()
# birthday = datetime.date(2003, 8, 15)   # Change to your birthday
# age_days = today - birthday
# print(f"You are {age_days.days} days old!")

# # Future date
# future = today + datetime.timedelta(days=30)
# print(f"30 days from now: {future}")

# # Math module
# print("\n Math")

# print(math.pi)          # 3.14159...
# print(math.sqrt(16))    # 4.0
# print(math.pow(2, 10))  # 1024.0
# print(math.floor(4.9))  # 4
# print(math.ceil(4.1))   # 5
# print(abs(-5))          # use abs() directly actually
# print(abs(-5))          # 5

# # OS module

# print("\n OS")

# print(os.getcwd())                  # Current directory
# print(os.listdir("."))              # files in current folder
# print(os.path.exists("test.txt"))   # check file exist

# # sys module
# print("\n SYS")
# print(sys.version)
# print(sys.platform)

# # Installing external modules with pip
# # These are not Built In modules into python - we install them 

# # Install 
# # pip install requests
# # pip install colorama

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code) # 200 means success
# print(type(response))


# # Requests = make HTTP requests, call APIs
# # flask = Build web apps
# # fastapi = Build REST APIs
# # sqlalchemy = Database ORM
# # pandas = Data analysis
# # colorama Colored terminal output

# # Importing your own module

# import sys
# sys.path.append("day2") # tell python where to find it

# import my_module

# print(my_module.greet("Sam"))
# print(my_module.add(5, 3))
# print(my_module.PI)

# # Import specific things
# from my_module import greet, PI
# print(greet("Priya"))
# print(PI)