#Possibility of finishing all courses given pre-requisitesBookmark Suggest Edit
#There are a total of N courses you have to take, labeled from 1 to N. Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2]. 
#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses. return 1/0 if it is possible/not possible.
#The list of prerequisite pair are given in two integer arrays B and C where B[i] is a prerequisite for C[i].
#
# Example: If N = 3 and the prerequisite pairs are [1,2] and [2,3], then you can finish courses in the following order: 1, 2 and 3. But if N = 2 and the prerequisite pairs are [1,2] and [2,1], then it is not possible for you to finish all the courses. 
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        def iscycle(adja,visited,stack,node):
            visited[node] = 1
            stack[node] = 1
            for i in adja[node]:
                if visited[i] != 1:
                    visited[i] = 1
                    stack[node] = 1
                    if iscycle(adja,visited,stack,i):
                        return 1
                elif stack[i] == 1:
                    return 1
            stack[node] = 0
            return 0
        adja = []
        visited = []
        stack = []
        for i in range(A+1):
            adja.append([])
            visited.append(0)
            stack.append(0)
        for i in range(0,len(B)):
            adja[B[i]].append(C[i])
        for i in range(1,len(adja)):
            if visited[i] == 0:
                if iscycle(adja,visited,stack,i):
                    return 0
        return 1
