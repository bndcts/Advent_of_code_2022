stack1 = ["Z", "N"]
stack2 = ["M", "C", "D"]
stack3 = ["P"]

stack_input = """
    [P]                 [C] [C]    
    [W]         [B]     [G] [V] [V]
    [V]         [T] [Z] [J] [T] [S]
    [D] [L]     [Q] [F] [Z] [W] [R]
    [C] [N] [R] [H] [L] [Q] [F] [G]
[F] [M] [Z] [H] [G] [W] [L] [R] [H]
[R] [H] [M] [C] [P] [C] [V] [N] [W]
[W] [T] [P] [J] [C] [G] [W] [P] [J] """

stacks = []
stack_input = stack_input.replace("[", " ")
stack_input = stack_input.replace("]", " ")
stack_input = stack_input.splitlines()
del stack_input[0]
#print(stack_input)

cr = []
for n, i in enumerate(stack_input):
    z = 1
    crates = []
    while z < len(i):
        crates.append(i[z])
        z += 4
    #print(crates)
    for m, x in enumerate(crates):
        if m < len(stacks):
            stacks[m].insert(0, x)
        else:
            stacks.append([x])

for i in stacks:
    for n, j in enumerate(i):
        if j == " ":
            del i[n:]

#print(stacks)
#stacks = [stack1, stack2, stack3]

input = open("day5_input.txt", "r")

arr = input.readlines()

#print(arr)

for n, i in enumerate(arr):
    arr[n] = i.split()
    ls = arr[n]
    cleaned = [ x for x in ls if x.isdigit()]
    arr[n] = cleaned

for i in arr:
    fr = int(i[1])-1
    to = int(i[2])-1
    num = int(i[0])
    move = stacks[fr][len(stacks[fr])-num:]
    del stacks[fr][len(stacks[fr])-num:]
    #move.reverse()
    stacks[to].extend(move)

res = ""
for i in stacks:
    res = res + i[len(i)-1]
print(res)
#print(stacks)