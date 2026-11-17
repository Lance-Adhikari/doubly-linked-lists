class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


# Create nodes
a = Node(7)
b = Node(8)
c = Node(10)
d = Node(4)

# Connect the nodes
a.next = b
b.prev = a

b.next = c
c.prev = b

c.next = d
d.prev = c

# Remove node c (value 10)
c.prev.next = c.next
c.next.prev = c.prev

# Disconnect c
c.prev = None
c.next = None

# Print remaining nodes
current = a

while current is not None:
    print(current.key)
    current = current.next
