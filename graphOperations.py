from copy import deepcopy
def findPath(graph, start, target):
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
    path.insert(0, node.name)
    if node.parent == None:
        return path
    else:
        return getPath(node.parent, path)

class Project:
    def __init__(self, value):
        self.value = value
        self.dependencies = []
    def addDependency(self, parent):
        self.dependencies.append(parent)

def buildOrder(projects):
    keepSearching = True
    co = []
    pt = []
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
    for dep in dependencies:
        if projectNotAdded(dep, co):
            return False
    return True

def projectNotAdded(project, projectsAdded):
    for p in projectsAdded:
        if p.value == project.value:
            return False
    return True
