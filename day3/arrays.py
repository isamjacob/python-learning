# Arrays
# Array is just items stored in order with index positions

# Index:  0    1    2    3    4
# Value: [10,  20,  30,  40,  50]

# Every array problem follows one of these patterns
# Loop through and check something
# Use two pointers
# Use a hash map
# Sort first then solve 
# Sliding window

# Pattern 1 - Loop and Check

# Input:  [5, 3, 8, 1, 9, 2], target = 8
# Output: True

# Step 1 - Understand: Go through every number, check if it equals target.
# Step 2 - Manual solve:
# Step 3 - Code

def contains(numbers, target):
    for num in numbers:
        if num == target:
            return True
    return False

print(contains([5, 3, 8, 1, 9, 2], 8))      # True
print(contains([5, 3, 8, 1, 9, 2], 7))      # False

# Big O: O(n) - One loop.

# Problem 2: Find the second largest number
# Input:  [5, 3, 8, 1, 9, 2]
# Output: 8

# Step 1 - Understand: Find largest, then find the largest among the rest
# Step 2 - Manual code
# Step 3 - logic
# Track two variables: largest and second_largest
# Loop through every number:
#   If number > largest:
#     second_largest = largest  (old largest becomes second)
#     largest = number          (new largest found)
#   Elif number > second_largest and number != largest:
#     second_largest = number   (new second found)

# Step 4 - Code
def second_largest(numbers):
    largest = float('-inf')     # negative infinity
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest    # Old largest becimes second
            largest = num       # Update largest
        elif num > second and num != largest:
            second = num        # Update second
    
    return second

print(second_largest([5, 3, 8, 1, 9, 2]))   # 8
print(second_largest([1, 2, 3, 4, 5]))      # 4

# Why float('-inf') It's negative infinity - smaller than ANY number. So the fitst comparision always works correctly.

# Problem 3: Rotate an array
# Input:  [1, 2, 3, 4, 5], rotate by 2
# Output: [4, 5, 1, 2, 3]

# Step 1 - Understand: Move last k elements to the front
# Step 2 - Manual solve:

# Original: [1, 2, 3, 4, 5]
# Last 2:   [4, 5]
# Rest:     [1, 2, 3]
# Combined: [4, 5, 1, 2, 3]

# Step 3 - Code

def rotate(numbers, k):
    k = k % len(numbers)       # Handle k larger than list size
    return numbers[-k:] + numbers[:-k]

print(rotate([1, 2, 3, 4, 5], 2))   # [4, 5, 1, 2, 3]
print(rotate([1, 2, 3, 4, 5], 7))   # [4, 5, 1, 2, 3]   (7 % 5 = 2)

# Pattern 2 - Two Pointer Technique

# This is one of the most powerful patterns in DSA.

# The idea: Use two variables pointing to different positions in the array and move them toward each other.

#[1, 2, 3, 4, 5, 6]
#  |                |
# left            right

# Problem 4: Check if array is a palindrome

# Input:  [1, 2, 3, 2, 1]
# Output: True

# Input:  [1, 2, 3, 4, 5]
# Output: False

# Step 1 - Understand: A palindrome reads same forwards and backwards
# Step 2 - Manual solve:
# Step 3 - Code

def is_palindrome(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] != numbers[right]:
            return False    # mismatch found
        left += 1           # move left pointer right
        right -= 1          # move right pointer left

    return True             # all matched!

print(is_palindrome([1, 2, 3, 2, 1]))   # True
print(is_palindrome([1, 2, 3, 4, 5]))   # False
print(is_palindrome([1, 2, 2, 1]))      # True

# Problem 5: Two Sum - find two numbers that add to target

# Input:  [2, 7, 11, 15], target = 9
# Output: [0, 1]  (because 2 + 7 = 9)

# Step 1 - Understand: Find two numbers in the list that add up to target. Return their indices.
# Step 2 - Brute force(O(n^2))

# Check every pair
def two_sum_brute(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return []

print(two_sum_brute([2, 7, 11, 15], 9))     # [0, 1]

# Step 3 - Better solution using HashMap (O(n))

# Logic:
# For each number, check if (target - number) exists already.

# Example: target = 9
#   See 2 → need 9-2=7 → is 7 in our map? No → store {2:0}
#   See 7 → need 9-7=2 → is 2 in our map? YES! → return [map[2], current index]

def two_sum(numbers, target):
    seen = {}    # number: index

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))    # [0, 1]
print(two_sum([3, 2, 4], 6))         # [1, 2]