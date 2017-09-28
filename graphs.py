class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    def getNodes(self):
        return self.nodes

class Node:
    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = adjacent
        self.parent = None

    def addNeighbours(self, neighbours):
        self.adjacent = neighbours
