# What is linked list - it is a chain of nodes
# Each node consist 
# data - the value stored
# next - pointer to the next node

# Linked list

# Node class

class Node:
    def __init__(self, data):
        self.data = data    # value stored
        self.next = None    # pointer to next node

# Creating nodes manually 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Connecting them manually 

node1.next = node2
node2.next = node3

# Now we have: 1 - 2 - 3 - None
print(node1.data)               # 1
print(node1.next.data)          # 2
print(node1.next.next.data)     # 3
print(node1.next.next.next)     # None

# Linked list class

class LinkedList:
    def __init__(self):
        self.head = None    # empty list starts with no head
        self.size = 0       # track number of nodes

        # INSERT at end

    def append(self, data):
        new_node = Node(data)

        # if list is empty - new node becomes head
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        # traverse to last node
        current = self.head
        while current.next is not None:
            current = current.next

        # attach new node at end 
        current.next = new_node
        self.size += 1

    # INSERT at beginning

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # new node becomes new head
        self.size += 1

    # DISPLAY the list

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        result = []

        while current is not None:
            result.append(str(current.data))
            current = current.next
        
        print(" -> ".join(result) + " -> None")

    # SEARCH for a value

    def search(self, target):
        current = self.head
        index = 0
        
        while current is not None:
            if current.data == target:
                return f"Found {target} at index {index}"
            current = current.next
            index += 1

        return f"{target} not found"
    
    # DELETE a value

    def delete(self, target):
        # Empty list
        if self.head is None:
            print("List is empty")
            return
        
        # deleting head node
        if self.head.data == target:
            self.head = self.head.next
            self.size -= 1
            print(f"Deleted {target}")
            return
        
        # find node before the target
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next    # skip target node
                self.size -= 1
                print(f"Deleted {target}")
                return
            current = current.next
        
        print(f"{target} not found")

    # LENGTH of list

    def length(self):
        return self.size
    

# TESTING


ll = LinkedList()

# Append items
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()    # 1 -> 2 -> 3 -> 4 -> 5 -> None

# Prepend item
ll.prepend(0)
ll.display()    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

# Search
print(ll.search(3))    # Found 3 at index 3
print(ll.search(10))   # 10 not found

# Delete
ll.delete(3)
ll.display()    # 0 -> 1 -> 2 -> 4 -> 5 -> None

ll.delete(0)
ll.display()    # 1 -> 2 -> 4 -> 5 -> None

# Length
print(f"Length: {ll.length()}")   # 4


# Question
# Given the head of a singly linked list, reverse the linked list and return the new head.

# Input:
# 1 -> 2 -> 3 -> 4 -> 5

# Output:
# 5 -> 4 -> 3 -> 2 -> 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next   # Store next node
        current.next = prev        # Reverse the link
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    return prev


# Helper function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
printList(head)

# Reverse the linked list
reversed_head = reverseLinkedList(head)

print("Reversed Linked List:")
printList(reversed_head)