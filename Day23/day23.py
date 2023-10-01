#filename='day23/input.txt'
filename='day23/day23.txt'
with open(filename) as f:
    lines = [x for x in f.read().split('\n')]


board = []
for line in lines:
    board.append(list(line))
    
def padding(grid, length):
    for _ in range(length):
        grid.append(['.' for _ in grid[0]])
        grid.insert(0, ['.' for _ in grid[0]])

    for idx, line in enumerate(grid):
        for _ in range(length):
            grid[idx].append('.')
            grid[idx].insert(0, '.')
    return grid

board = padding(board, 3)
print(board)


for y, line in enumerate(board):
    for x, val in enumerate(line):
        if val=='#':
            N=(x, y-1)
            NE=(x+1, y-1)
            NW=(x-1, y-1)
            print(x,y)
    
    
