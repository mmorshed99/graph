#Task. Given an directed graph with possibly negative edge weights and with n vertices and m edges, 
#check whether it contains a cycle of negative weight.
#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    curr_cost = []
    for i in range (0,len(adj)):
       curr_cost.append(1001)

    for i in range(1,len(adj)):
       for j in range(0,len(adj)):
          for k in range(0,len(adj[j])):
             if curr_cost[adj[j][k]] > curr_cost[j] + cost[j][k]:
               curr_cost[adj[j][k]] = curr_cost[j] + cost[j][k] 
     
    for j in range(0,len(adj)):
          for k in range(0,len(adj[j])):
             if curr_cost[adj[j][k]] > curr_cost[j] + cost[j][k]:
               return 1
    
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
