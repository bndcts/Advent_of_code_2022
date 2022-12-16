import re

input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

input = input.splitlines()
# print(int(re.findall(r'\d+', st[0])[0]))
# print(st[0].split()[9:])
# a = []
# for x in st[0].split()[9:]:
#     a.append(x.replace(',', ""))

# print(a)
queue = []
def parseInput(a):
    edges = {}
    flowRates = {}
    for s in a:
        s = s.split()
        v = s[1]
        fr = int(re.findall(r'\d+', s[4])[0])
        flowRates[v] = fr
        leads = []
        for x in s[9:]:
            leads.append(x.replace(',', ""))
        edges[v] = leads

    return flowRates, edges

def algo(edges, flowRates, v, timeleft, visited):

    queue.append([v])
    results = []
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = edges[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                timeleft -= 1

                queue.append(new_path)

                if timeleft == 0:

                    # print("Shortest path = ", *new_path)
                    return
            visited.append(node)
            timeleft -= 1
            
    return

def algoUtil(edges, flowrates, v, timeleft):

def main():
    flowRates, edges = parseInput(input)
    algo(edges, flowRates, list(edges.keys())[0], 30)

    return "s"

if __name__ == "__main__":
    print(main())








