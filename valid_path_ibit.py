def solve(self, A, B, C, D, E, F):
        def find_blockage(A,B,C,D,E,F):
            block_arr = []
            for i in range(A+1):
                block_arr.append([])
                for j in range(B+1):
                    block_arr[i].append(1)
            for i in range(C):
                ctr_x = E[i]
                ctr_y = F[i]
                range_x = []
                range_y = []
                for j in reversed(range (ctr_x-D,ctr_x)):
                    if j < 0:
                        break
                    range_x.append(j)
                    range_y.append(ctr_y)
                for j in reversed(range (ctr_y-D,ctr_y)):
                    if j < 0:
                        break
                    range_x.append(ctr_x)
                    range_y.append(j)
                for j in range(ctr_x,ctr_x+D):
                    if j > A:
                        break
                    range_x.append(j)
                    range_y.append(ctr_y)
                for j in range(ctr_y,ctr_y+D):
                    if j > B:
                        break
                    range_x.append(ctr_x)
                    range_y.append(j)
                curr_y = ctr_y
                for j in reversed(range (ctr_x-D,ctr_x)):
                    if j < 0 or curr_y - 1 < 0:
                        break
                    curr_y -= 1
                    range_x.append(j)
                    range_y.append(curr_y)
                curr_y = ctr_y
                for j in reversed(range (ctr_x-D,ctr_x)):
                    if j < 0 or curr_y + 1 > B:
                        break
                    curr_y += 1
                    range_x.append(j)
                    range_y.append(curr_y)
                curr_y = ctr_y
                for j in range (ctr_x,ctr_x+D):
                    if j > A or curr_y + 1 > B:
                        break
                    curr_y += 1
                    range_x.append(j)
                    range_y.append(curr_y)
                curr_y = ctr_y
                for j in range (ctr_x,ctr_x+D):
                    if j > A or curr_y - 1 < 0:
                        break
                    curr_y -= 1
                    range_x.append(j)
                    range_y.append(curr_y)
            for i in range(len(range_x)):
                block_arr[range_x[i]][range_y[i]] = 0
            return block_arr
        def find_next(x,y,block_arr,visited):
                temp = []
                temp_x = [x-1,x-1,x-1,x+1,x+1,x+1,x,x]
                temp_y = [y,y-1,y+1,y,y+1,y-1,y+1,y-1]
                for i in range(8):
                  if temp_x[i] >= 0 and temp_x[i] <= A and temp_y[i] >= 0 and temp_y[i]<= B: 
                    if block_arr[temp_x[i]][temp_y[i]] and not visited[temp_x[i]][temp_y[i]]:
                        temp.append([temp_x[i],temp_y[i]])
                return temp,visited
                
        curr_points = []
        visited = []
        for i in range(A+1):
            visited.append([])
            for j in range(B+1):
                visited[i].append(0)
        block_arr = find_blockage(A,B,C,D,E,F)
        if block_arr[0][0]:
            curr_points.append([0,0])
        while(len(curr_points) != 0):
                next_points = []
                for i in range(len(curr_points)):
                    visited[curr_points[i][0]][curr_points[i][1]] = 1
                    if curr_points[i][0] == A and curr_points[i][1] == B:
                        return "YES"
                    next_pt_from_curr_pt,visited = find_next(curr_points[i][0],curr_points[i][1],block_arr,visited)
                    for i in next_pt_from_curr_pt:
                        if len(i) != 0:
                           next_points.append(i)
                curr_points = []
                for j in next_points:
                    curr_points.append(j)
        return "NO"
