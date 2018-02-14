# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        dic = {}
        curr_list = [node]
        new_node = UndirectedGraphNode(node.label)
        dic[node] = new_node
        visited = {}
        visited[node] = 1
        while(len(curr_list) != 0):
            next_list = []
            for i in range(len(curr_list)):
                for j in range(len(curr_list[i].neighbors)):
                    try:
                     if visited[curr_list[i].neighbors[j]] == 1:
                        x = 1 
                    except:
                      next_list.append(curr_list[i].neighbors[j])
                      visited[curr_list[i].neighbors[j]] = 1
                    try:
                        dic[curr_list[i]].neighbors.append(dic[curr_list[i].neighbors[j]])
                    except:
                        my_node = str(curr_list[i].neighbors[j]) + "new"
                        my_node = UndirectedGraphNode(curr_list[i].neighbors[j].label)
                        dic[curr_list[i].neighbors[j]] = my_node
                        dic[curr_list[i]].neighbors.append(dic[curr_list[i].neighbors[j]])
            curr_list = []
            curr_list = next_list[:]
        return dic[node]
