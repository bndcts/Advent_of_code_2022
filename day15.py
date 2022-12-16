import re
input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

input = input.splitlines()
f = open("day15_input.txt", "r")
input = f.readlines()

def parseInput(s, num):
    xValues = []
    yValues = []
    values = []
    for i in s:
        dig = re.findall(r'-?\d+', i)
        for j in range(len(dig)):
            dig[j] = int(dig[j])
        values.append(dig)
        xValues.append(dig[0])
        xValues.append(dig[2])
        yValues.append(dig[1])
        yValues.append(dig[3])
    maxX, minX, maxY, minY = max(xValues), min(xValues), max(yValues), min(yValues)
    minX = -2077481

    if minY < 0:
        for i in values:
            i[1] + abs(minY)
            i[3] + abs(minY)
        maxY += abs(minY)
        minY += abs(minY)

    if minX < 0:
        for i in values:
            i[0] + abs(minX)
            i[2] + abs(minX)
        maxX += abs(minX)
        minX += abs(minX)

    row = []

    for i in range(maxX):
        row.append(False)

    ofInterest = values
    #for i in values:
        # if (i[1] <= num <= i[3]) or (i[1] >= num >= i[3]):
        #     ofInterest.append(i)

    for i in ofInterest:
        radius = abs(i[0] - i[2]) + abs(i[1]-i[3])
        i.append(radius)

    for i in ofInterest:
        dif = abs(i[1] - num)
        if not dif > i[4]:
            row[i[0]] = True

            restRadius = abs(dif-i[4])

            for j in range(restRadius+1):
                left = i[0] - j
                right = i[0] + j
                if left >= minX:
                    row[left] = True
                if right <= maxX:
                    row[right] = True


    return sum(row)


def main():
    return parseInput(input, 2000000)

if __name__ == "__main__":
    print(main())