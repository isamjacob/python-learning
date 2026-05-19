
# STRINGS - DEEP DIVE

word = "Hello World"

# Basic operations
print(len(word))           # 11 — length
print(word.lower())        # hello world
print(word.upper())        # HELLO WORLD
print(word.strip())        # removes whitespace from both ends
print(word.split(" "))     # ['Hello', 'World']
print(word.replace("World", "Python"))  # Hello Python
print(word.count("l"))     # 3 — count occurrences
print(word.find("World"))  # 6 — index where it starts
print(word.startswith("Hello"))  # True
print(word.endswith("World"))    # True

# Slicing
print(word[0:5])    # Hello
print(word[6:])     # World
print(word[::-1])   # dlroW olleH — reversed

# Check type
print("abc123".isalnum())   # True — all alphanumeric
print("abc".isalpha())      # True — all letters
print("123".isdigit())      # True — all digits
print("  ".isspace())       # True — all spaces

# Problem 1 - reverse a string

# Input:  "hello"
# Output: "olleh"

# Method 1 — Pythonic 
def reverse_string(word):
    return word[::-1]

# Method 2 — Using Two pointer 
def reverse_string_tp(word):
    chars = list(word)    # strings immutable, convert to list
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)  # convert list back to string

print(reverse_string("hello"))      # olleh
print(reverse_string_tp("hello"))   # olleh

# Remember lists in python are immutable

# word = "hello"
# word[0] = "H"   # TypeError

chars = list("hello")
chars[0] = "H"  # works

# Problem 2 - Anagram

# Input:  "listen", "silent"
# Output: True

# Input:  "hello", "world"
# Output: False

# what is anagram - Same letters, different orders

def is_anagram(word1, word2):
    # Quick check - different lengths can't be anagrams
    if len(word1) != len(word2):
        return False
    
    counts = {}

    # Count letters in word1 - add
    for char in word1:
        counts[char] = counts.get(char, 0) + 1
    
    # Count letters in word2 - subtract
    for char in word2:
        counts[char] = counts.get(char, 0) - 1
    
    # If all counts are 0 - anagram
    for count in counts.values():
        if count != 0:
            return False
    
    return True

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("rat", "car"))        # True

# Problem 3 - First Non-Repeating Character

# Input:  "leetcode"
# Output: "l"

# Input:  "aabb"
# Output: None  (all repeat)

def first_non_repeating(word):
    counts = {}

    # Pass 1 - count frequency
    for char in word:       # Loop in ORIGINAL order
        if counts.get(char, 0) == 1:
            return char
    
    return None     # All characters repeat

print(first_non_repeating("leetcode"))  # l
print(first_non_repeating("aabb"))      # None
print(first_non_repeating("swiss"))     # w

# Problem 4 - Longest Common Prefix 

# Input:  ["flower", "flow", "flight"]
# Output: "fl"

# Input:  ["dog", "racecar", "car"]
# Output: ""  (no common prefix)

def longest_common_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]   # start with first word as prefix

    for word in words[1:]:
        # shrink prefix until it matches start of word
        while not word.startswith(prefix):
            prefix = prefix[: -1]   # remove last character
            if not prefix:
                return ""
    
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))  # fl
print(longest_common_prefix(["dog", "racecar", "car"]))     # ""
print(longest_common_prefix(["interview", "inter", "internal"]))  # inter

# Problem 5 - Longest Substring Without Repeating Characters

# Input:  "abcabcbb"
# Output: 3  ("abc")

# Input:  "bbbbb"
# Output: 1  ("b")

def longest_unique_substring(s):
    seen = set()
    left = 0 
    max_length = 0

    for right in range(len(s)):
        # if duplicate found - shrink window from left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # add current character to window
        seen.add(s[right])

        # update max length
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))     # 1
print(longest_unique_substring("pwwkew"))    # 3

# Exercise 1

# Count number of vowels in a string
# Input:  "Hello World"
# Output: 3  (e, o, o)
# Hint: check if each char is in "aeiou"

def count_vowles(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in vowels:
        if char in vowels:
            count += 1
    return count

print(count_vowles("Hello World"))  # 3

# Exercise 2

# Reverse the words in a sentence
# Input:  "Hello World Python"
# Output: "Python World Hello"
# Hint: split() then reverse then join()

def reverse_words(sentence):
    words = sentence.split(" ")    # split into list
    words.reverse()                # reverse the list
    return " ".join(words)         # join back to string

print(reverse_words("Hello World Python"))  # Python World Hello

# Python Easy way to write the same thing

# def reverse_words(sentence):
#     return " ".join(sentence.split(" ")[::-1])

# Exercise 3 - Check panagram

# A pangram contains every letter of alphabet at least once
# Input:  "The quick brown fox jumps over the lazy dog"
# Output: True
# Hint: use set() to find unique letters
#       check if all 26 letters present

def is_panagram(sentence):
    sentence = sentence.lower()
    unique_letters = set()

    for char in sentence:
        if char.isalpha():
            unique_letters.add(char)
    
    return len(unique_letters) == 26

print(is_panagram("The quick brown fox jumps over the lazy dog"))   # True
print(is_panagram("Hello World"))   # False

# Exercise 4 - Compress String

# Compress consecutive repeated characters
# Input:  "aabcccdddd"
# Output: "a2bc3d4"
# If count is 1 → just write the letter
# Hint: loop and count consecutive same characters

def compress_string(word):
    if not word:
        return ""
    
    result = ""
    count = 1

    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            count += 1
        else:
            result += word[i-1]
            if count > 1:
                result += str(count)
            count = 1
    
    # Handle last character
    result += word[-1]
    if count > 1:
        result += str(count)

    return result

print(compress_string("aabcccdddd"))   # a2bc3d4
print(compress_string("abc"))          # abc
print(compress_string("aabb"))         # a2b2