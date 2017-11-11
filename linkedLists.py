class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        node = self.head
        listvalues = ""
        while node:
            listvalues += str(node.value)
            node = node.next
        return listvalues

    def add(self, data):
        newNode = LLNode(data)
        if not self.head:
            self.head = newNode
        if self.tail:
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            self.head.next = newNode
            self.tail = self.head.next
    
    
        
     
