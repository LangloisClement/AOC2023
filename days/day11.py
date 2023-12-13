from re import finditer
from pkg_resources import resource_stream


def expandUnivers(universe: list[str]):
    lineToAdd = []
    colToAdd = []
    for i in range(len(universe)):
        if not "#" in universe[i]:
            lineToAdd.append(i)
    for i in range(len(universe[0])):
        flag = True
        for line in universe:
            if line[i] == "#":
                flag = False
                break
        if flag:
            colToAdd.append(i)
    count = 0
    for nb in colToAdd:
        for i in range(len(universe)):
            universe[i] = universe[i][:nb+count]+"."+universe[i][nb+count:]
        count += 1
    count = 0
    for nb in lineToAdd:
        universe.insert(nb+count, universe[nb+count])
        count += 1


def part1():
    print("day 11")
    universe = []
    with resource_stream('input', 'D11.txt') as textInput:
        universe = [line.decode().strip() for line in textInput.readlines()]
    # find index to expand
    expandUnivers(universe)
    lenUni = len(universe[0])
    coordGalaxies = []
    for i in range(len(universe)):
        coordGalaxies += [(x.start(), i) for x in finditer("#", universe[i])]
    res = 0
    for i in range(len(coordGalaxies)-1):
        for coord in coordGalaxies[i+1:]:
            if coordGalaxies[i][0] < coord[0]:
                absX = coord[0]-coordGalaxies[i][0]
            else:
                absX = coordGalaxies[i][0]-coord[0]
            absY = abs(coordGalaxies[i][1]-coord[1])
            dist = absX+absY
            # print(f"dist {coordGalaxies[i]} -- {coord} = {absX}+{absY}={dist}")
            res += dist
    return res


def expandOldUnivers(universe: list[str]):
    lineToAdd = []
    colToAdd = []
    for i in range(len(universe)):
        if not "#" in universe[i]:
            lineToAdd.append(i)
    for i in range(len(universe[0])):
        flag = True
        for line in universe:
            if line[i] == "#":
                flag = False
                break
        if flag:
            colToAdd.append(i)
    return (colToAdd, lineToAdd)


def part2():
    print("day 11")
    universe = []
    FACTEUR = 1000000
    with resource_stream('input', 'D11.txt') as textInput:
        universe = [line.decode().strip() for line in textInput.readlines()]
    # find index to expand
    expanded = expandOldUnivers(universe)
    coordGalaxies = []
    for i in range(len(universe)):
        coordGalaxies += [(x.start(), i) for x in finditer("#", universe[i])]
    res = 0
    for i in range(len(coordGalaxies)-1):
        for coord in coordGalaxies[i+1:]:
            # coord[0]=colone
            # coord[1]=ligne
            dist = 0
            if coordGalaxies[i][0] < coord[0]:
                coloneTraversed = [c for c in range(
                    coordGalaxies[i][0], coord[0])]
            else:
                coloneTraversed = [c for c in range(
                    coord[0], coordGalaxies[i][0])]
            ligneTraversed = [l for l in range(coordGalaxies[i][1], coord[1])]
            for colone in coloneTraversed:
                if colone in expanded[0]:
                    dist += FACTEUR
                else:
                    dist += 1
            for ligne in ligneTraversed:
                if ligne in expanded[1]:
                    dist += FACTEUR
                else:
                    dist += 1
            # print(f"dist {coordGalaxies[i]} -- {coord} = {absX}+{absY}={dist}")
            res += dist
    return res
