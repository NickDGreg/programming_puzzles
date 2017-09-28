class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.start = None
        self.node = None

    def add(self, newNode):
        newNode = LLNode(newNode)
        if not self.start:
            self.start = newNode
        if self.node:
            self.node.next = newNode
        self.node = newNode
