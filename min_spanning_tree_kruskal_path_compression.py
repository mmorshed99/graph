'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# your task is to complete this function
# Function should return sum of weights of  the edges of the Minimum Spanning Tree
# graph is of form adjancy matrix
# e is the number of edges and n is the no of nodes
def spanningTree(graph, n, e):
    # Code here
    def find_parent(parent,x):
        if parent[x] == x:
            return x, parent
        parent[x],parent = find_parent(parent,parent[x])
        return parent[x],parent

    def union_by_rank(parent,rank,x_parent,y_parent):
        #x_parent,parent = find_parent(parent,x)
        #y_parent,parent = find_parent(parent,y)
        if rank[x_parent] < rank[y_parent]:
            parent[x_parent] = y_parent
            #rank[x_parent] += 1
        elif rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1
        return rank, parent
    def merge_sort(A):
        if len(A) == 1:
            return A
        if len(A) == 2:
            if A[0][0] > A[1][0]:
                A[0],A[1] = A[1],A[0]
            return A
        A_left = merge_sort(A[0:len(A)//2])
        A_right = merge_sort(A[len(A)//2 : len(A)])
        left_idx = 0
        right_idx= 0
        temp = []
        while(True):
            if A_left[left_idx][0] < A_right[right_idx][0]:
                temp.append(A_left[left_idx])
                left_idx += 1
                if left_idx == len(A_left):
                    for i in range(right_idx,len(A_right)):
                        temp.append(A_right[i])
                    break
            else: #A_right[right_idx][0] < A_left[left_idx][0]:
                temp.append(A_right[right_idx])
                right_idx += 1
                if right_idx == len(A_right):
                    for i in range(left_idx,len(A_left)):
                        temp.append(A_left[i])
                    break
        return temp
    def post_process_input(graph):
        temp = []
        for i in range(0,n):
            #if i+1 == len(graph[i]):
            #    continue
            for j in range(i+1,len(graph[i])):
             if graph[i][j] != 0:
                temp.append([graph[i][j],i,j])
        return temp
    my_graph = post_process_input(graph)
    my_graph_sorted = merge_sort(my_graph)
    parent = []
    rank   = []
    current_num = 0
    for i in range(n):
        parent.append(i)
        rank.append(0)
    i = 0
    total_val = 0
    while(current_num < n-1 and i <len(my_graph_sorted)):
        a = my_graph_sorted[i][1]
        b = my_graph_sorted[i][2]
        a_parent,parent = find_parent(parent,a)
        b_parent,parent = find_parent(parent,b)
        if a_parent == b_parent:
            i += 1
            #current_num += 1
        else:
            total_val += my_graph_sorted[i][0]
            rank,parent = union_by_rank(parent,rank,a_parent,b_parent)
            i += 1
            current_num += 1
                
    return total_val
