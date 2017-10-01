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
    """ex 4.3 returns linked list for each depth layer of the tree
    upon creation listNodes is a list containing the root of the tree
    Builds a linked list of the previous layer contained in listNodes.
    Saves in linkedListNodes. While building that list, the previous 
    layer's children are stored in a list to then recursively call the function
    """
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

"""
over confusing implementation by me. It uses a linkedlist class which new nodes
can be easily added to. Those nodes are linked list nodes with a value and next.
But here, I am adding tree nodes which have a value and left,right for the children.
So 
LinkedList of Nodes whos values and next attributes are TreeNodes with a value (i.e. 5)
and left,right attributes which are TreeNodes
"""

def listOfDepthsANSWER(root):
    """ex 4.3 based on answer from book
    builds linked list of a layer, saves it, then loops through that
    layer's nodes adding the children to a new linked list"""
    result = []
    currentLL = LinkedList()
    if root:
        currentLL.add(root)
    while currentLL.node:
        result.append(currentLL)
        parentNode = currentLL.start
        currentLL = LinkedList()
        while parentNode:
            if parentNode.value.left:
                currentLL.add(parentNode.value.left)
            if parentNode.value.right:
                currentLL.add(parentNode.value.right)
            parentNode = parentNode.next
    return result
