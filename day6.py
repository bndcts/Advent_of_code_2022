f = open("day6_input.txt", "r")
input = f.read()
#input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def is_unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return len(unique_list) == len(list)

def main():
    for i in range(len(input)-12):
        l = []
        for j in range(i, i+14):
            l.append(input[j])
        if is_unique(l):
            return(i+14)


if __name__ == "__main__":
    print(main())
