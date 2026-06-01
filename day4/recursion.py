# what is recurssion

# A function that calls itself until it reaches a base case

# def countdown(n):
#     if n == 0:          # base case — STOP
#         print("Done!")
#         return
#     print(n)
#     countdown(n - 1)    # calls itself!

# countdown(5)
# 5, 4, 3, 2, 1, Done!

# Real life analogy:

# Standing between two mirrors — you see infinite reflections of yourself. Each reflection contains another reflection. Recursion is the same — function contains itself.

# Every recursive function needs TWO things:

# 1. BASE CASE  → when to STOP (prevents infinite loop)
# 2. RECURSIVE CASE → call itself with smaller problem

# def countdown(n):
#     print(n)
#     countdown(n-1)

# Recursion

# Example 1: Factorial

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    return n * factorial(n - 1)

print(factorial(5)) # 120
print(factorial(0)) # 1
print(factorial(10))  # 3628800

#  Example 2: Fibonacci 
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Each number = sum of previous two

def fibonacci(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8
print(fibonacci(10))  # 55

# Example 3: Sum of list 
def sum_list(numbers):
    # base case — empty list
    if len(numbers) == 0:
        return 0
    # recursive case
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))   # 15

# Example 4: Power
# 2^10 = 1024

def power(base, exp):
    # base case
    if exp == 0:
        return 1
    # recursive case
    return base * power(base, exp - 1)

print(power(2, 10))   # 1024
print(power(3, 4))    # 81

# Example 5: Reverse string
def reverse_string(s):
    # base case
    if len(s) == 0:
        return ""
    # recursive case
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))   # olleh
print(reverse_string("python"))  # nohtyp

# Recurssion vs Iteration

# Factorial — iterative way
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Factorial — recursive way
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

# Both give same answer!
print(factorial_iterative(5))   # 120
print(factorial_recursive(5))   # 120

# Exercise 1 - Count down:

# Print numbers from n down to 1 using recursion
# countdown(5) → 5, 4, 3, 2, 1

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

# Testing
countdown(5)

# Exercise 2 - Sum of digits:

# Find sum of digits of a number using recursion
# sum_digits(1234) → 10  (1+2+3+4)
# Hint: n % 10 gives last digit
#       n // 10 removes last digit

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

# Testing
print(sum_digits(1234))   # 10
print(sum_digits(999))    # 27
print(sum_digits(0))      # 0

# Exercise 3 - Check palindrome:

# Check if string is palindrome using recursion
# is_palindrome("racecar") → True
# is_palindrome("hello")   → False
# Hint: compare first and last char
#       then recurse on middle

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Testing
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("madam"))     # True
print(is_palindrome("a"))         # True

# Exercise 4 - Flatten nested list:

# Flatten a nested list using recursion
# flatten([1, [2, 3], [4, [5, 6]]]) → [1, 2, 3, 4, 5, 6]
# Hint: if item is a list → recurse
#       if item is a number → add to result

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Testing
print(flatten([1, [2, 3], [4, [5, 6]]]))     # [1, 2, 3, 4, 5, 6]
print(flatten([1, [2, [3, [4, [5]]]]]))      # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3]))                     # [1, 2, 3]