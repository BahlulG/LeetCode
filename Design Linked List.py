class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        elif index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            newNode = Node(val)
            for _ in range(index - 1):
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            temp.next = temp.next.next
        self.size -= 1