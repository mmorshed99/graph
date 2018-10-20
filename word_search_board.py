#Given a 2D board and a word, find if the word exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell. 
#The same letter cell may be used more than once.
#
#Example :
#
#Given board =
#
#[
#  ["ABCE"],
#  ["SFCS"],
#  ["ADEE"]
#]
#word = "ABCCED", -> returns 1,
#word = "SEE", -> returns 1,
#word = "ABCB", -> returns 1,
#word = "ABFSAB" -> returns 1
#word = "ABCD" -> returns 0
#
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        def find_pattern(curr_idx,curr_search_idx,B_split,list_2d):
            next_search_idx = [[curr_search_idx[0]-1,curr_search_idx[1]],[curr_search_idx[0]+1,curr_search_idx[1]],[curr_search_idx[0],curr_search_idx[1]-1],[curr_search_idx[0],curr_search_idx[1]+1]]
            for i in next_search_idx:
                if i[0] >= 0 and i[0]< len(list_2d) and i[1] >= 0 and i[1]< len(list_2d[i[0]]) and list_2d[i[0]][i[1]] == B_split[curr_idx]:
                    if curr_idx == len(B_split)-1:
                        return 1
                    elif find_pattern(curr_idx+1,[i[0],i[1]],B_split,list_2d):
                        return 1
            return 0
        list_2d = []
        B_split = list(B)
        for i in range(len(A)):
            temp = list(A[i])
            list_2d.append(temp)
        save_start = []
        for i in range(len(list_2d)):
            for j in range(len(list_2d[i])):
                if list_2d[i][j] == B_split[0]:
                    save_start.append([i,j])
                    if len(B_split) == 1:
                        return 1
        for i in range(len(save_start)):
            curr_search_idx = save_start[i]
            curr_idx = 0
            if find_pattern(curr_idx+1,curr_search_idx,B_split,list_2d):
                return 1
        return 0
    
    #############look at this #####
    class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == B[0]:
                    if len(B) == 1:
                        return 1
                    stack = []
                    stack.append([i,j])
                    curr = 0
                    while(len(stack) > 0 and curr < len(B)):
                        temp_stack = []
                        for k in range(len(stack)):
                            if A[stack[k][0]][stack[k][1]] == B[curr]:
                                print(stack[k][0])
                                print(stack[k][1])
                                if curr == len(B) -1 :
                                    return 1
                                x = stack[k][0]
                                y = stack[k][1]
                                if x == len(A) - 1:
                                    temp_stack.append([0,y])
                                else:
                                    temp_stack.append([x+1,y])
                                if x == 0:
                                    temp_stack.append([len(A)-1,y])
                                else:
                                    temp_stack.append([x-1,y])
                                if y == len(A[stack[k][0]]) - 1:
                                    temp_stack.append([x,0])
                                else:
                                    temp_stack.append([x,y+1])
                                if y == 0:
                                    temp_stack.append([x,len(A[stack[k][0]])-1])
                                else:
                                    temp_stack.append([x,y-1])
                        stack = temp_stack[:]
                        curr += 1
        return 0
                                

