# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices's
def isCyclic(n, graph):
    # Code here
    visited = []
    for i in range(0,n):
        visited.append(0)
    def iscycle(node,visited,parent):
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                if iscycle(i,visited,node):
                    return 1
            elif i != parent:
                return 1
        return 0
    for i in list(graph):
        if visited[i] == 0:
            if iscycle(i,visited,-1):
                return 1
    return 0
