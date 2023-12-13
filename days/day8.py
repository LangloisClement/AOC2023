from math import lcm
from re import findall
from pkg_resources import resource_stream


def part1():
    print("day 8")
    directions = ""
    nodes = {}
    with resource_stream('input', 'D8.txt') as textInput:
        lines = textInput.readlines()
        directions = lines[0].decode().strip()
        for i in range(2, len(lines)):
            l = lines[i].decode().strip().split(" = ")
            k = l[0]
            v = findall(r"\w+", l[1])
            nodes[k] = tuple(v)
    node = "AAA"
    nbstep = 0
    while node != "ZZZ":
        d = directions[nbstep % len(directions)]
        match d:
            case "L":
                node = nodes[node][0]
            case "R":
                node = nodes[node][1]
        nbstep += 1
    return nbstep


def listStrEndsWith(l: list[str], end: str):
    for s in l:
        if not s.endswith(end):
            return False
    return True


def part2():
    print("day 8")
    directions = ""
    nodes = {}
    with resource_stream('input', 'D8.txt') as textInput:
        lines = textInput.readlines()
        directions = lines[0].decode().strip()
        for i in range(2, len(lines)):
            l = lines[i].decode().strip().split(" = ")
            k = l[0]
            v = findall(r"\w+", l[1])
            nodes[k] = tuple(v)

    startNodes = [s for s in nodes.keys() if s.endswith("A")]
    cycleSize = []
    for node in startNodes:
        nbstep = 0
        while not node.endswith("Z"):
            d = 0 if directions[nbstep % len(directions)] == "L" else 1
            node = nodes[node][d]
            nbstep += 1
        cycleSize.append(nbstep)
    return lcm(*cycleSize)
