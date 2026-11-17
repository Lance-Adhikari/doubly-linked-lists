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


# Practice
dll = DoublyLinkedList()

dll.push_back(7)
dll.push_back(10)
dll.push_back(4)
dll.push_back(20)

print(dll.head.key)
print(dll.tail.key)
print(dll.tail.prev.key)
