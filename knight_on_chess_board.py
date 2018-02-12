# Problem Statement
#https://www.interviewbit.com/problems/knight-on-chess-board/
#
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        def find_next(x,y,visited):    
          temp = []
          temp_x = [x-2,x-1,x+1,x+2,x-2,x-1,x+1,x+2]
          temp_y = [y-1,y-2,y-2,y-1,y+1,y+2,y+2,y+1]
          for i in range(8):
            if temp_x[i] >= 0 and temp_x[i] <= A-1 and temp_y[i] >= 0 and temp_y[i]<= B-1: 
              if not visited[temp_x[i]][temp_y[i]]:
                temp.append([temp_x[i],temp_y[i]])
                visited[temp_x[i]][temp_y[i]] = 1
          return temp,visited
        curr_points = []
        visited = []
        for i in range(A):
            visited.append([])
            for j in range(B):
                visited[i].append(0)
        curr_points.append([C-1,D-1])
        total = -1
        while(len(curr_points) != 0):
            total += 1
            next_points = []
            for i in range(len(curr_points)):
                visited[curr_points[i][0]][curr_points[i][1]] = 1
                if curr_points[i][0] == E-1 and curr_points[i][1] == F-1:
                    return total
                next_pt_from_curr_pt,visited = find_next(curr_points[i][0],curr_points[i][1],visited)
                for i in next_pt_from_curr_pt:
                    if len(i) != 0:
                        next_points.append(i)
            curr_points = []
            for j in next_points:
                curr_points.append(j)
        return -1
