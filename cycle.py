'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
def isCyclic(n, graph):
    # Code here
    visited = []
    mystack = []
    for i in range(0,n):
        visited.append(0)
    for i in range(0,n):
        mystack.append(0)
    def iscycle(node,visited,mystack):
        visited[node] = 1
        mystack[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                mystack[i] = 1
                if iscycle(i,visited,mystack):
                    return 1
            elif mystack[i] == 1:
                return 1
        mystack[node] = 0
        return 0
    for i in list(graph):
        if visited[i] == 0:
            #visited[i] = 1
            #mystack[i] = 1
            if iscycle(i,visited,mystack):
                return 1
    return 0
