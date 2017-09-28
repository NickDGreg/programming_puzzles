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
        
