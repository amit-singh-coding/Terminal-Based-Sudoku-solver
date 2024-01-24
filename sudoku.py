def is_possible(mat,r,c,ch):
    for i in range(0,9): #--->check for row
        if mat[r][i]==ch:
            return False
        if mat[i][c]==ch:#-->check for column
            return False
    #--->check for 3X3 box
    box_r=(r//3)*3
    box_c=(c//3)*3
    for i in range(box_r,box_r+3): 
        for j in range(box_c,box_c+3):
            if mat[i][j]==ch:
                return False
    return True            
def solve(mat,r,c):
    if r==9:
        return True
    if c==9:
        return solve(mat,r+1,0)
        
    if mat[r][c]!=0:
        return solve(mat,r,c+1)
    for ch in range(1,10):
        if is_possible(mat,r,c,ch):
            mat[r][c]=ch
            if solve(mat,r,c+1):
                return True
            else:    
                mat[r][c]=0
    return False        
                
mat=[[0, 4, 0, 0, 0, 0, 1, 7, 9],
    [0, 0, 2, 0, 0, 8, 0, 5, 4],
    [0, 0, 6, 0, 0, 5, 0, 0, 8],
    [0, 8, 0, 0, 7, 0, 9, 1, 0],
    [0, 5, 0, 0, 9, 0, 0, 3, 0],
    [0, 1, 9, 0, 6, 0, 0, 4, 0],
    [3, 0, 0, 4, 0, 0, 7, 0, 0],
    [5, 7, 0, 1, 0, 0, 2, 0, 0], 
    [9, 2, 8, 0, 0, 0, 0, 6, 0]]
if(solve(mat,0,0)):
    for rr in range(0,9):
        print(*mat[rr]);
else:
    print(-1);