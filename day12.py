input  = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

input = input.splitlines()
x = -1
y = -1

def getPosition(grid):
    for y1 in range(len(grid)):
        for x1 in range(len(y1)):
            if grid[y1][x1] == "S":
                x = x1
                y = y1
                return

def bfs(grid, posx, posy):
    return




