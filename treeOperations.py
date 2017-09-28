from math import ceil
from trees import Node
from linkedLists import LLNode, LinkedList
def printTree(node):
    if node:
        printTree(node.left)
        print(node)
        printTree(node.right)

def printLinkedList(node):
    if node:
        print(node)
        return printLinkedList(node.next)

def createBinarySearchTree(values):
    """ Values is ordered array of distinct integers"""
    midIdx = ceil(len(values)/2) - 1
    newNode = Node(values[midIdx])
    if midIdx > 0:
        newNode.left = createBinarySearchTree(values[:midIdx])
    if midIdx < len(values)-1:
        newNode.right = createBinarySearchTree(values[midIdx+1:])
    return newNode

def listOfDepths(listNodes, linkedListNodes):
    startNode = LLNode(listNodes[0].value)
    current = startNode
    newlistNodes = []
    if listNodes[0].left:
        newlistNodes.append(listNodes[0].left)
    if listNodes[0].right:
        newlistNodes.append(listNodes[0].right)
    for n in listNodes[1:]:
        nextNode = LLNode(n.value)
        current.next = nextNode
        current = nextNode
        if n.left:
            newlistNodes.append(n.left)
        if n.right:
            newlistNodes.append(n.right)
    linkedListNodes.append(startNode)
    if newlistNodes:
        return listOfDepths(newlistNodes, linkedListNodes)
    else:
        return linkedListNodes

def listOfDepthsANSWER(root):
    result = []
    currentLL = LinkedList()
    if root:
        currentLL.add(root)
    while currentLL.node:
        result.append(currentLL)
        parentNode = currentLL.start
        print(currentLL.node.value)
        currentLL = LinkedList()
        while parentNode:
            if parentNode.value.left:
                currentLL.add(parentNode.value.left)
            if parentNode.value.right:
                currentLL.add(parentNode.value.right)
            parentNode = parentNode.next
    return result
