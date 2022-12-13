input  = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

f = open("day12_input.txt", "r")
input = f.readlines()

class position:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.posx == other.posx and self.posy == other.posy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return ("" + str(self.posx) + " " + str(self.posy))

    def __repr__(self):
        return self.__str__()


visited = []
queue = []

def getStartPosition(grid):
    for y1 in range(len(grid)):
        for x1 in range(len(grid[y1])):
            if grid[y1][x1] == "S":
                return position(x1, y1)

def getPotentialNeighbours(grid, pos):
    x = pos.posx
    y = pos.posy
    neighbours = []
    if x < len(grid[0]) - 1:
        neighbours.append(position(x+1, y))
    if y != 0:
        neighbours.append(position(x, y-1))
    if x != 0:
        neighbours.append(position(x-1, y))
    if y < len(grid) - 1 :
        neighbours.append(position(x, y+1))
    
    for p in neighbours:
        if ord(grid[p.posy][p.posx]) > ord(grid[y][x]) + 1:
            neighbours.remove(p)

    return neighbours
        

def bfs(grid, pos, visited):
    #visited.append(pos)
    queue.append([pos])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = getPotentialNeighbours(grid, node)

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if grid[neighbour.posy][neighbour.posx] == "E":
                    #print("Shortest path = ", *new_path)
                    return
            visited.append(node)
        # neighbours = getPotentialNeighbours(grid, pos)
        # for neighbour in neighbours:
        #     if neighbour not in visited:
        #         visited.append(neighbour)
        #         queue.append(neighbour)


def main():
    pos = getStartPosition(input)
    bfs(input, pos, visited)

    pos1 = position(7, 4)
    #print(getPotentialNeighbours(input, pos1))
    #print(input[pos1.posy][pos1.posx])
    return visited


if __name__ == "__main__":
    print(len(main())-1)

print(getStartPosition(input))