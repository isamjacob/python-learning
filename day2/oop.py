# Day 2 OOP (Object Oriented Programming)
# Why OOP Without OOP - messy
# student1_name = "Sam"
# student1_age = 22
# student1_marks = 85

# student2_name = "Priya"
# student2_age = 19
# student2_marks = 92

# 100 students = 300 variables

# With OOP - Clean

# student1 = Student("Sam", 22, 85)       # Class Students not defined yet just an example to show the importance of OOP
# student2 = Student("Priya", 19, 92)
# 100 students = 100 lines

# Class is the blue print or the template
# Object is the actual thing made from the template

# Example

# Class = blue print
# class Student:
#     ...

# # Objects = actual students made from the blue print
# student1 = Student("Sam", 22)
# student2 = Student("priya", 19)
# student3 = Student("Rahul", 20)

# These were all the basic knowledge about OOP for better understanding

class Student:
    
    # __init__ is the consturctor
    # called automatically when you create an object
    def __init__(self, name, age, marks):
        self.name = name    # Store name in object
        self.age = age      # Store age in object  
        self.marks = marks  # Store marks in object

    def introduce(self):
        print(f"Hi! I am {self.name}, {self.age} years old.")
    
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Makrs: {self.marks}")
        print(f"Grade: {self.get_grade()}")
        print("-" * 20)

# Creating objects 
student1 = Student("Sam", 22, 85)
student2 = Student("Priya", 19, 92)
student3 = Student("Rahul", 20, 45)

# Using objects
student1.introduce()
student2.introduce()

student1.display()
student2.display()
student3.display()

# EXPLAINATION
# Class Student - Definnes a new blueprint called Student. Capital letters is the convention for class names

# __init__ - The Constructor, __init__ runs automatically the moment you create an object

# Self - what is it ?
# Self refers to the current object itself. Self is how the object refers to its own data. Without it, the method wouldn't know which student's data to use

# Methods - Functions inside a class
# A method is just a function inside a class. The only difference - first parameter is always self.
# You never pass self manually - Python does it for you 

# Exercise 1 

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner  # Store owner name 
        self.balance = balance  # Store starting balance

    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: {self.balance}")
        print("-" * 30)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} deposited!")
        print(f"New balance: {self.balance}")
        print("-" * 30)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds!")
            print(f"You tried: {amount}")
            print(f"Available: {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn!")
            print(f"New balance: {self.balance}")
        print("-" * 30)

account = BankAccount("Sam", 1000)
account.display()          # show starting balance
account.deposit(500)       # add 500 → balance = 1500
account.withdraw(200)      # remove 200 → balance = 1300
account.withdraw(2000)     # not enough! → insufficient funds
account.display()          # show final balance

# Inheritance 

# In real life - a child inherits traits from praents. Same in Python - a child class inherits everything from the parent class
# Why do we need
# Without inheritance:
# We need to repeat the same code everywhere
# with Inheritance:
# we just need to add unique stuff in the new child class other thing will be inherited from parent class

# Inheritance 

# Parent Class
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping....")
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("-" * 20)

# Child class - inherits from animal
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Woof") # Call parent __init__
        self.tricks = []                    # Dog's own attribute
    
    def learn_tricks(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} knows no tricks yet!")

class Cat(Animal):
    def __init__ (self, name, age, is_indoor):
        super().__init__(name, age, "Meow")
        self.is_indoor = is_indoor              # cat's own attribute

    def display(self):                          # Over ride parent method
        super().display()                       # cal parent display
        indoor = "Indoor" if self.is_indoor else "Outdoor"
        print(f"Type: {indoor} cat")
        print("-" * 20)

# TESTING
dog1 = Dog("Bruno", 3)
cat1 = Cat("Whiskers", 2, True)

# Dog using inherited methods
dog1.speak()       # inhereted from Animal
dog1.eat()         # inhereted from Animal
dog1.display()     # inhereted from Animal

# Dog using its own methods
dog1.learn_tricks("Sit")
dog1.learn_tricks("Roll_Over")
dog1.show_tricks()

print()

# Cat using inhereted methods 
cat1.speak()    # inhereted from Animal
cat1.eat()      # inhereted from Animal
cat1.display()  # overridden - shows extra info


# Exercise 1

# Create a parent class called Employee:
# Attributes: name, employee_id, salary
# Methods:
#   display()     → prints name, id, salary
#   give_raise(amount) → increases salary

# Create two child classes:

# 1. Manager(Employee)
#    Extra attribute: team_size
#    Extra method: hold_meeting() → 
#        prints "Manager {name} is holding meeting with {team_size} people"

# 2. Developer(Employee)
#    Extra attribute: programming_language
#    Extra method: write_code() →
#        prints "{name} is writing {language} code"

# Test:
# manager = Manager("Rahul", "M001", 80000, 10)
# dev = Developer("Sam", "D001", 60000, "Python")

# manager.display()
# manager.give_raise(10000)
# manager.hold_meeting()

# dev.display()
# dev.give_raise(5000)
# dev.write_code()


# Parent class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print(f"Name:   {self.name}")
        print(f"ID:     {self.employee_id}")
        print(f"Salary:  {self.salary}")
        print("-" * 30)

    def give_raise(self, amount):
        self.salary = self.salary + amount
        print(f"{self.name} got a raise of {amount}!")
        print(f"New salary: {self.salary}")
        print("-" * 30)


# Child class 1
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def hold_meeting(self):
        print(f"Manager {self.name} is holding meeting with {self.team_size} people")
        print("-" * 30)


# Child class 2
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing {self.programming_language} code")
        print("-" * 30)


# Testing
manager = Manager("Rahul", "M001", 80000, 10)
dev = Developer("Sam", "D001", 60000, "Python")

manager.display()
manager.give_raise(10000)
manager.hold_meeting()

dev.display()
dev.give_raise(5000)
dev.write_code()