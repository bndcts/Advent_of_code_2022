input="""30373
25512
65332
33549
35390"""
input = input.splitlines()
f = open("in.txt", "r")
input = f.readlines()

rot90 = lambda A: [*map(list, zip(*A[::-1]))]

grid = [[*map(int, x.strip())] for x in open('in.txt')]
part1 = [[0 for _ in x] for x in grid]
part2 = [[1 for _ in x] for x in grid]

for _ in range(4):
    for x,y in [(x,y) for x in range(99) for y in range(99)]:
        lower = [t < grid[x][y] for t in grid[x][y+1:]]

        part1[x][y] |= all(lower)
        part2[x][y] *= len(lower) if all(lower) else lower.index(0)+1

    grid, part1, part2 = map(rot90, [grid, part1, part2])

print(sum(map(sum, part1)), max(map(max, part2)))

summ = 2*len(input) + len(input[0])*2 - 4

for i in range(1,len(input)):
    for j in range(1, len(input[i])):
        val = input[i][j]
        visible = True
        for left in range(j):
            if input[i][left] >= val:
                visible = False
        right = len(input[i])-1
        while right > j:
            if input[i][right] >= val:
                visible = False
            right -= 1
        for up in range(i):
            if input[up][j] >= val:
                visible = False
        down = len(input)-1
        while down > i:
            if input[down][j] >= val:
                visible = False
            down -= 1
        if visible:
            summ += 1

print(summ)
