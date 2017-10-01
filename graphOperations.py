from copy import deepcopy
def findPath(graph, start, target):
    """ex 4.1 uses BFS to get the path between two nodes in a graph"""
    nodes = graph.getNodes()
    if start.name is target.name: return start
    visited = [start]
    toSearch = [start]
    while toSearch:
        focus = toSearch.pop(0)
        for n in focus.adjacent:
            if n not in visited:
                n.parent = focus
                visited.append(n)
                toSearch.append(n)
            if n.name is target.name:
                return getPath(n, [])
    return None

def getPath(node, path=[]):
     """ex 4.1 recursively builds path taken to node"""
    path.insert(0, node.name)
    if node.parent == None:
        return path
    else:
        return getPath(node.parent, path)

class Project:
    """ex 4.7"""
    def __init__(self, value):
        self.value = value
        self.dependencies = []
    def addDependency(self, parent):
        self.dependencies.append(parent)

def buildOrder(projects):
    """ex 4.7 finds a possible build order of a set of projects 
    based on their dependencies. Uses BFS."""
    keepSearching = True
    co = [] #current build order
    pt = [] #paths tried
    while keepSearching:
        for p in projects:
            # print('dep filled: ' + str(dependenciesFilled(p.dependencies, co)))
            if projectNotAdded(p, co) and dependenciesFilled(p.dependencies, co):
                trypath = deepcopy(co)
                trypath.append(p)
                if trypath not in pt:
                    co = trypath
                    added = True
        if not added:
            if len(co) == len(projects):
                keepSearching = False
                return co
            if len(co) == 0:
                keepSearching = False
                return error
            if co:
                pt.append(co)
                del co[-1]
        added = False
    return False

def dependenciesFilled(dependencies, co):
    """ex 4.7"""
    for dep in dependencies:
        if projectNotAdded(dep, co):
            return False
    return True

def projectNotAdded(project, projectsAdded):
    """ex 4.7"""
    for p in projectsAdded:
        if p.value == project.value:
            return False
    return True
