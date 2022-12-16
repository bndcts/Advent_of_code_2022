input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

input = input.splitlines()

f = open("day14_input.txt", "r")
input = f.readlines()

grid = [[]]
for x in range(550):
    grid.append([])
    for y in range(1200):
        grid[x].append(False)

def parseInput(s, partTwo):
    for i in s:
        i = i.replace("->", "")
        i = i.split()
        for j in range(len(i)-1):
            x = i[j].split(",")
            y = i[j+1].split(",")
            x1 = int(x[0])
            y1 = int(x[1])
            x2 = int(y[0])
            y2 = int(y[1])
            if x1 == x2:
                l = [y1, y2]
                for z in range(min(l), max(l)+1):
                    grid[z][x1] = True
            if y1 == y2:
                l = [x1, x2]
                for z in range(min(l), max(l)+1):
                    grid[y1][z] = True

    # for i in grid[0:10]:
    #     print(i[494:504])
    if partTwo:
        height = highestY()+1
        for i in range(len(grid[0])-1):
            grid[height][i] = True

    for i in grid[0:12]:
        print(i[494:504])

def highestY():
    height = 0
    for i in range(1, len(grid)):
        if True not in grid[i] and True in grid[i-1]:
            if i > height:
                height = i
    #print(height)
    return height

def sand():
    posX = 500
    posY = 0
    count = 0
    height = highestY()
    while posY < height+5:
        if not grid[posY+1][posX]:
            posY += 1
        elif not grid[posY+1][posX-1]:
            posY += 1
            posX -= 1
        elif not grid[posY+1][posX+1]:
            posY +=1
            posX +=1
        else:
            if posX == 500 and posY == 0:
                count += 1
                break
            grid[posY][posX] = True
            count += 1
            #print("x:" + str(posX) + "y: " + str(posY))
            posX = 500
            posY = 0
    return count

def main():
    parseInput(input, True)
    return sand()

if __name__ == "__main__":
    print(main())