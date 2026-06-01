# Stack and Queue 
from collections import deque

# # Using list for queue — SLOW!
# items = [1, 2, 3]
# items.pop(0)    # O(n) — shifts ALL elements left 

# # Using deque — FAST!
# from collections import deque
# items = deque([1, 2, 3])
# items.popleft()  # O(1) — instant! 

# deque is a double-ended queue — optimized for adding/removing from both ends.

# Stack

class Stack:
    def __init__(self):
        self.items = []             # List to store items

    def push(self, item):
        self.items.append(item)     # Add to top

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop() # Removes from top
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]        # view top without removing
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Stack: {self.items} <- top")

# Testing

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()                 # [1, 2, 3] <- top

print(stack.peek())             # 3 - top item
print(stack.pop())              # 3 - removed
stack.display()                 # [1, 2] <- top
print(f"Size: {stack.size()}")  # 2

# Queue

class Queue:
    def __init__(self):
        self.items = deque()    # deque is faster than list for queue

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items.popleft()     # remove from front
    
    def front(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items[0]            # view front without removing
    
    def is_empty(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: front -> {list(self.items)} <- back")

# Testing

queue = Queue()

queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")
queue.display()             # front -> [Alice, Bob, Charlie]   <- back


print(queue.front())            # Alice
print(queue.dequeue())          # Alice - served first!
queue.display()                 # front -> [Bob, Charlie]
print(f"Size: {queue.size()}")  # 2

# Problem 1 - Valid Parentheses

def valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)      # opening -> push
        
        elif char in ')}]':
            if not stack:           # nothing to match
                return False
            if stack[-1] != pairs[char]:    # doesn't match
                return False
            stack.pop()                     # matched -> pop

    return len(stack) == 0                  # empty = all matched

print(valid_parentheses("()[]{}"))      # True
print(valid_parentheses("([)]"))        # False
print(valid_parentheses("{[]}"))        # True
print(valid_parentheses("((("))         # False

# Problem 2 - Reverse a string using Stack

def reverse_with_stack(word):
    stack = Stack()

    # push all characters
    for char in word:
        stack.push(char)

    # pop all characters — comes out reversed!
    result = ""
    while not stack.is_empty():
        result += stack.pop()

    return result

print(reverse_with_stack("hello"))   # olleh
print(reverse_with_stack("python"))  # nohtyp

# Problem 3 - Min Stack (get minimum in O(1)):

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []   # tracks minimums

    def push(self, val):
        self.stack.append(val)
        # push to min_stack if it's new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()   # remove from min too
        return val

    def get_min(self):
        return self.min_stack[-1]   # O(1)!

    def display(self):
        print(f"Stack: {self.stack}")
        print(f"Min:   {self.get_min()}")


# Testing
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
ms.push(4)
ms.display()        # Stack: [5,3,7,2,4], Min: 2

ms.pop()            # remove 4
ms.pop()            # remove 2
ms.display()        # Stack: [5,3,7], Min: 3

# Real Problems using Queue:

# Problem - Hot Potato(circular queue simulation):

def hot_potato(players, count):
    queue = Queue()

    # add all players
    for player in players:
        queue.enqueue(player)

    while queue.size() > 1:
        # pass potato 'count' times
        for _ in range(count):
            queue.enqueue(queue.dequeue())  # move front to back

        # person holding potato is eliminated
        eliminated = queue.dequeue()
        print(f"{eliminated} is eliminated!")
    
    return queue.dequeue()  # winner!

winner = hot_potato(["Alice", "Bob", "Charlie", "David", "Eve"], 3)
print(f"Winner: {winner}")

# Exercise 1 - Balanced brackets:

# Already solved above — valid_parentheses
# Now extend it:
# Return WHICH bracket is unmatched
# Input:  "([)]"
# Output: "Unmatched ) at index 2"

def valid_parentheses_extended(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for index, char in enumerate(s):
        if char in '({[':
            stack.append((char, index))

        elif char in ')}]':
            if not stack:
                return f"Unmatched {char} at index {index}"
            if stack[-1][0] != pairs[char]:
                return f"Unmatched {char} at index {index}"
            stack.pop()

    if stack:
        char, index = stack[-1]
        return f"Unmatched {char} at index {index}"

    return "Valid!"

# Testing
print(valid_parentheses_extended("()[]{}"))   # Valid!
print(valid_parentheses_extended("([)]"))     # Unmatched ) at index 2
print(valid_parentheses_extended("{[]}"))     # Valid!
print(valid_parentheses_extended("((("))      # Unmatched ( at index 0

# Exercise 2 - Queue using two Stacks:

# Implement a Queue using only two Stack objects
# No deque or list.pop(0) allowed!
# Hint:
# stack1 → for enqueue (push)
# stack2 → for dequeue (pop from stack1 into stack2, then pop stack2)

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()   # inbox — for enqueue
        self.stack2 = Stack()   # outbox — for dequeue

    def enqueue(self, item):
        self.stack1.push(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        if self.stack2.is_empty():
            return "Queue is empty!"

        return self.stack2.pop()

    def display(self):
        all_items = list(self.stack2.items) + \
                    list(reversed(self.stack1.items))
        print(f"Queue front → {all_items} ← back")


# Testing
print(" QUEUE USING TWO STACKS ")
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print(f"Dequeued: {q.dequeue()}")
print(f"Dequeued: {q.dequeue()}")
q.enqueue(4)
q.display()
print(f"Dequeued: {q.dequeue()}")
print(f"Dequeued: {q.dequeue()}")


# Exercise 3 - Next greater element:

# For each element find next greater element to its right
# Input:  [4, 5, 2, 10, 8]
# Output: [5, 10, 10, -1, -1]
# (4's next greater = 5, 5's next greater = 10...)
# (-1 means no greater element exists)
# Hint: use stack!

def next_greater(numbers):
    result = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            index = stack.pop()
            result[index] = numbers[i]
        stack.append(i)

    return result

# Testing
print(next_greater([4, 5, 2, 10, 8]))   # [5, 10, 10, -1, -1]
print(next_greater([1, 3, 2, 4]))        # [3, 4, 4, -1]
print(next_greater([5, 4, 3, 2, 1]))     # [-1, -1, -1, -1, -1]