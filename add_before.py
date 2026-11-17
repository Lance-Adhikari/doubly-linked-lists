class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, key):
        new_node = Node(key)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect the old tail and new node in both directions.
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        return new_node

    def add_before(self, node, key):
        new_node = Node(key)

        # Preserve both neighbors before inserting the new node.
        new_node.next = node
        new_node.prev = node.prev

        # Inserting before the first node updates the head.
        if node.prev is None:
            self.head = new_node
        else:
            node.prev.next = new_node

        node.prev = new_node


dll = DoublyLinkedList()

first = dll.push_back(7)
second = dll.push_back(10)
third = dll.push_back(4)

# Insert 8 before node 10
dll.add_before(second, 8)

# Print the list
current = dll.head

while current is not None:
    print(current.key)
    current = current.next
