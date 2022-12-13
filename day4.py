
f = open("day4_input.txt", "r")
input = f.readlines()

def main():
    count = 0
    for i in input:
        i = i.replace(",", " ")
        i = i.split()
        one = i[0].split("-")
        two = i[1].split("-")
        low1 = one[0]
        low2 = two[0]
        high1 = one[1]
        high2 = two[1]
        if (low1 >= low2 and high1 <= high2) or (low2 >= low1 and high2 <= high1):
            print("low1: " + low1 + " low2: " + low2 + " high1: " + high1 + " high2: " + high2)
            count += 1

    return count

if __name__ == "__main__":
    print(main())