class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def pop(self) -> int:
        if self.head is not None:
            value = self.head.item
            self.head = self.head.next
            return value
        raise ValueError

    def peek(self) -> int:
        if self.head is not None:
            return self.head.item
        raise ValueError

    def empty(self) -> bool:
        return self.head is None
