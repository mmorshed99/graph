/*Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j iff either j = i + 1 or j = 3i. The task is to find the minimum number of edges in a path in G from vertex 1 to vertex n.

Input:  
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

Each test case contains a value of n. 

Output:  
Print the number of edges in the shortest path from 1 to n.

Constraints:
1<=T<=30
1<=n <=1000

Example:
Input:
2
9
4

Output:
2
2
*/
#code
import sys
def find_next(dist,unvisited):
    min = sys.maxsize
    node = -1
    for i in range(len(unvisited)):
      if unvisited[i] == True:
        if dist[i] < min:
            min = dist[i]
            node = i
    return node
def shortest_path(nodes):
    adja = []
    dist = []
    unvisited = []
    total = nodes
    for i in range(nodes+1):
        dist.append(sys.maxsize)
        unvisited.append(True)
        temp = []
        if i+1 <= nodes:
            temp.append(i+1)
        if 3 * i <= nodes:
            temp.append(3*i)
        adja.append(temp)
    unvisited[0] = False
    dist[1] = 0
    while(total>0):
      curr_node = find_next(dist,unvisited)
      unvisited[curr_node] = False
      total -= 1
      for i in range(len(adja[curr_node])):
          if dist[adja[curr_node][i]] > dist[curr_node] + 1:
             dist[adja[curr_node][i]] = dist[curr_node] + 1
    return dist[nodes]
t = int(input())
for i in range(t):
    nodes = int(input())
    print(shortest_path(nodes))
