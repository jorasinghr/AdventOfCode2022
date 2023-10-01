filename='day12/input.txt'
#filename='day12/day12.txt'
with open(filename) as f:
    lines = [x for x in f.read().split('\n')]

#import sys
#sys.setrecursionlimit(100000)

#print(list(lines[0])) 
matrix=[]

for y, line in enumerate(lines):
    temp_list=list(line)
    new_list=[]
    for val in temp_list:
        new_list.append(ord(val)-96)
    matrix.append(new_list)
    for x, chr in enumerate(line):
        if chr=='S':
            startx=x
            starty=y
        if chr=='E':
            endx=x
            endy=y
print(startx, starty, endx, endy)
#print(matrix)


 
# Recursive function to get all routes in a rectangular grid
# that start at cell (i, j) and ends at the last cell (M-1, N-1).
shortlist=[]
def printPaths(mat, i=0, j=0, M=2, N=3, route=[]):
 
    # base case
    if not mat or not len(mat):
        return
 
    # `M × N` matrix
    #(M, N) = (len(mat), len(mat[0]))
    (Y, X) = (len(mat), len(mat[0]))
    
    # include current cell in route
    route.append(mat[i][j])
    
    # if the last cell is reached
    if i == M and j == N:
        print(route)
        shortlist.append(len(route))
    else:
        # move down
        if i + 1 < Y and (matrix[i+1][j] == matrix[i][j]+1 or matrix[i+1][j] ==  matrix[i][j]):
            printPaths(mat, i + 1, j, M, N, route)
        
        # move up
        if 0 <= i - 1 < Y and (matrix[i-1][j] == matrix[i][j]+1 or matrix[i-1][j] ==  matrix[i][j]):
            printPaths(mat, i - 1, j, M, N, route)
        
        # move right
        if j + 1 < X and (matrix[i][j+1] == matrix[i][j]+1 or matrix[i][j+1] ==  matrix[i][j]):
            printPaths(mat, i, j + 1, M, N, route)
        
        # move left
        if 0 <= j - 1 < X and (matrix[i][j-1] == matrix[i][j]+1 or matrix[i][j-1] ==  matrix[i][j]):
            printPaths(mat, i, j - 1, M, N, route)
 
 
    # backtrack: remove the current cell from the route
    route.pop()
 
 

 

printPaths(matrix, startx, starty, endx, endy)
print(shortlist)