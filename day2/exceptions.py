# Exception handling

# Till now the program crashes when something goes wrong
# age = int(input("Enter age: "))
# User types "hello" instead of a number
# ValueError: invalid literal for int()
# Program dies completely!

# Exception handling makes yout program survive errors gracefully

# Exception Handling

# Without exception handling
# age = int(input("Enter age: ")) # Crashes if user types "hello"

# With exception handling
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Invalid input! Please enter a number.")

print("Program continues...")   # this runs even after error

# Multiple except block

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print(f"Something went wrong: {e}")

# Try/except/else/finally

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That's not a number!")

except ZeroDivisionError:
    print("Can't divide by zero!")

else:
    # runs ONLY if no error occured
    print(f"Result is: {result}")

finally:
    # ALWAYS runs - error or no error
    print("Thank you for using the calculator")

# try      -  always runs first
# except   -  only if error occurs
# else     -  only if NO error
# finally  -  ALWAYS runs no matter what

# Why finally - Closing database connections, closing files, cleanup tasks - things that MUST happen regardless

# Real world example - safe file reader

import os 
def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None

    except PermissionError:
        print(f"No permission to read '{filename}'!")
        return None
    finally:
        print(f"Attempted to read: {filename}")

# Test 
content = read_file_safely("test.txt")
if content:
    print(content)

content2 = read_file_safely("missing.txt")
print(content2)

# Raising your own exceptions

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be more than 150!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")

# raise let's you throw an error when something is wrong - just like Python does internally

# Combining with loops - keep asking until valid

# This is extremely useful in real prjects
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            print("Please enter a valid age!")
            continue
        break   # Valid input - exit loop
    except ValueError:
        print("Numbers only please!")

print(f"Your age is: {age}")

# Exercise 1
# Build a safe calculator
# Keep asking for input until valid
# Handle:
#   - Non-number input (ValueError)
#   - Division by zero (ZeroDivisionError)
#   - Invalid operation (not +, -, *, /)
# Show result and ask if user wants to continue

# Expected flow:
# Enter first number: hello     ← ValueError caught
# Enter first number: 10        ← valid
# Enter second number: 0        ← valid
# Enter operation (+,-,*,/): /  ← ZeroDivisionError caught
# Enter second number: 5        ← valid
# Enter operation (+,-,*,/): /
# Result: 2.0
# Continue? (yes/no): no
# Goodbye!


# Individual operation functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b   # ZeroDivisionError triggers here if b = 0


# Main calculator function
def safe_calculator():
    while True:
        try:
            # Get input
            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            # Perform operation
            if operation == "+":
                result = add(number1, number2)
            elif operation == "-":
                result = sub(number1, number2)
            elif operation == "*":
                result = mul(number1, number2)
            elif operation == "/":
                result = div(number1, number2)
            else:
                print(" Invalid operation! Use +, -, *, / only")
                continue   # go back to top of loop

        except ValueError:
            print(" Numbers only please!")
            continue

        except ZeroDivisionError:
            print(" Cannot divide by zero!")
            continue

        else:
            # Only runs if zero errors occurred
            print(f" {number1} {operation} {number2} = {result}")

        # Ask to continue
        again = input("Continue? (yes/no): ").lower()
        if again == "no":
            print("Goodbye!")
            break


# Run the calculator
safe_calculator()