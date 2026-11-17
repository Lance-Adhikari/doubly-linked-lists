class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


# Create three nodes
first = Node(7)
second = Node(10)
third = Node(4)

# Connect forward
first.next = second
second.next = third

# Connect backward
second.prev = first
third.prev = second

# Head and tail
head = first
tail = third

# Move forward
print(head.key)
print(head.next.key)
print(head.next.next.key)

# Move backward
print(tail.key)
print(tail.prev.key)
print(tail.prev.prev.key)
