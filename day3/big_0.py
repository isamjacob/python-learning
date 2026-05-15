# Big O notation - How to measure Code speed
# Why does you this matter ?
# Imagine you have 1 million user on your app

# Solution A - takes 1 second for 1000 users
# How long for 1 million users? 1000 seconds

# Solution B - takes 1 second for 1000 users
# How long for 1 million users? 2 seconds

# Same problem, different solutions, MASSIVE difference in real world. Big O tells you which solution is better BEFORE you run it.

# What is Big O?

# Big O measures how your code slows down as data grows.
# Not the exact time - the pattern of growth.

# You have a list of N items.
# As N grows bigger and bigger - 
# how much slower does your code get ?

# The 6 most common Big O values:

# O(1)          - constant
# O(log n)      - Logarithmic
# O(n)          - Linear
# O(n log n)    - Log Linear
# O(n^2)        - Quadratic
# O(2^n)        - Exponential

# 1 - O(1) - Constant Time
# No matter how big the data - always takes same time

# Example 1 - Accessing list by index
numbers = [10, 20, 30, 40, 50]
print(numbers[0])       # Instant - dosen't matter if list has 5 or 5 million items

# Example 2 - Dictionary lookup
student = {"name": "Sam", "age": 22}
print(student["name"])  # Instant always

# Example 3 
def get_first(items):
    return items[0]     # always ONE operation

# O(1) is the best possible. Always aim for this 

# O(n) - Linear Time
# As data doubles - time doubles

# Example - Searching through a list
def find_number(numbers, target):
    for num in numbers:         # Loops through EVERY item
        if num == target:
            return True
    return False

# If list has 10 items      - upto 10 checks
# If list has 1000 items    - upto 1000 checks
# If list has 1M items      - upto 1M checks

# O(n^2) - Quadratic Time
# As data doubles - time quadruples

# Example
def find_duplicates(numbers):
    for i in range (len(numbers)):      # Outer loop - n times
        for j in range (len(numbers)):  # inner loop - n times for EACH outer
            if i != j and numbers[i] == numbers[j]:
                print(f"Duplicate: {numbers[i]}")

# If list has 10 items - 10 x 10 = 100 operations
# If list has 100 items - 100 x 100 = 10,000 operations
# If list has 1000 items - 1000 x 1000 = 1,000,000

# O(log n) - Logarithmic Time
# Example - Binary Search
# Find number in a SORTED list by cutting in half each time

def binary_search(numbers, target):
    left = 0 
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2   # Check middle

        if numbers[mid] == target:
            return mid              # found!
        elif numbers[mid] < target:
            left = mid + 1          # target is in right half
        else:
            right = mid - 1         # target is in left half
    
    return -1 # not found

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 7))    # finds index 3

# How to identify Big O by looking at code:

# One loop - O(n)
for i in range(n):
    print(i)

# Two seperate loops - O(n) still!
# (n + n = 2n - drop constant - O(n))
for i in range(n):
    print(i)
for j in range(n):
    print(j)

# Nested loops - O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)

# No loops - O(1)
print(numbers[0])
print(student["name"])

# Cutting in half each time - O(log n)
while n > 1:
    n = n // 2

# The 3 Rules of Big O:
# Rule - 1 Drop constants:

# O(2n)     - O(n)
# O(100)    - O(1)
# O(3n^2)   - O(n^2)

# Rule 2 - Drop smaller terms:

# O(n^2 + n) - O(n^2)
# O(100)     - O(n)

# Rule 3 - Different lists

# Two different lists:
for item in list_a:     # O(a)
    print(item)
for item in list_b:     # O(b)
    print(item)
# Total: O(a + b) NOT O(n)


# Big O Practice Problems

# O(1) - Constant
def get_first_last(numbers):
    return numbers[0], numbers[-1]

# O(n) - Linear
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# O(n²) - Quadratic
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# O(log n) - Logarithmic
def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Testing
numbers = [5, 2, 8, 1, 9, 3]
print(get_first_last(numbers))
print(find_max(numbers))
print(bubble_sort(numbers.copy()))
print(binary_search([1, 2, 3, 5, 8, 9], 5))

# Practice problems

# Problem 1 - Sum of all numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(numbers)
print(f"Sum: {total}")

# Problem 2 - Find all even numbers
evens = [n for n in numbers if n % 2 == 0]
print(f"Evens: {evens}")

# Problem 3 - Reverse a list
reversed_list = numbers[::-1]
print(f"Reversed: {reversed_list}")

# Problem 4 - Count occurrences
words = ["python", "java", "python", "c++", "python", "java"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"Counts: {counts}")

# Problem 5 - Find duplicates
nums = [1, 2, 3, 2, 4, 3, 5]
duplicates = set()
for n in nums:
    if nums.count(n) > 1:
        duplicates.add(n)
print(f"Duplicates: {duplicates}")