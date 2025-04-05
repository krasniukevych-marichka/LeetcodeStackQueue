class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = Node(x, self.head)

    def pop(self) -> int:
        if self.head is not None:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError

    def top(self) -> int:
        if self.head is not None:
            return self.head.item
        raise ValueError

    def empty(self) -> bool:
        return self.head is None
