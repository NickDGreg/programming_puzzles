from math import ceil
from trees import Node

def printTree(node):
    if node:
        printTree(node.left)
        print(node)
        printTree(node.right)

def createBinarySearchTree(values):
    """ Values is ordered array of distinct integers"""
    midIdx = ceil(len(values)/2) - 1
    newNode = Node(values[midIdx])
    if midIdx > 0:
        newNode.left = createBinarySearchTree(values[:midIdx])
    if midIdx < len(values)-1:
        newNode.right = createBinarySearchTree(values[midIdx+1:])
    return newNode
