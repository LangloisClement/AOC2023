# Advent Of Code 2023

from pkg_resources import resource_stream
from functools import reduce
from re import sub, findall, finditer
from day5 import Day5
from day7 import Day7

print("hello world")


def day1_part1():
    listNumber = []
    with resource_stream('input', 'D1.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            numbers = sub(r"\D", "", line)
            lineNumber = "".join([numbers[0], numbers[-1]])
            listNumber.append(int(lineNumber))
    return reduce(lambda a, b: a+b, listNumber)


def day1_part2():
    listNumber = []
    transTable = {"one": "1", "two": "2", "three": "3", "four": "4",
                  "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    with resource_stream('input', 'D1.txt') as textInput:
        for line in textInput.readlines():
            numbers = []
            line = line.decode().strip()
            for i in range(len(line)):
                if line[i].isdigit():
                    numbers.append(line[i])
                for k, v in transTable.items():
                    if line.startswith(k, i):
                        numbers.append(v)
                        break
            lineNumber = "".join([numbers[0], numbers[-1]])
            listNumber.append(int(lineNumber))
    return reduce(lambda a, b: a+b, listNumber)


def day2_part1():
    print("day 2")
    possibleGame = []
    with resource_stream('input', 'D2.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            lineSplit = line.split(":")
            gameID = int(lineSplit[0].strip("Game "))
            cubeSets = lineSplit[-1].split(";")
            flagValide = True
            for cubeSet in cubeSets:
                if not flagValide:
                    break
                cubes = cubeSet.strip().split(", ")
                for cube in cubes:
                    if not flagValide:
                        break
                    nb = int(*(findall(r"(\d+)", cube)))
                    match cube:
                        case str(a) if "red" in a:
                            if nb > 12:
                                flagValide = False
                        case str(a) if "green" in a:
                            if nb > 13:
                                flagValide = False
                        case str(a) if "blue" in a:
                            if nb > 14:
                                flagValide = False
            if flagValide:
                possibleGame.append(gameID)
    return reduce(lambda a, b: a+b, possibleGame)


def day2_part2():
    print("day 2")
    gamePower = []
    with resource_stream('input', 'D2.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            lineSplit = line.split(":")
            cubeSets = lineSplit[-1].split(";")
            gameSet = {"red": 0, "green": 0, "blue": 0}
            for cubeSet in cubeSets:
                cubes = cubeSet.strip().split(", ")
                for cube in cubes:
                    nb = int(*(findall(r"(\d+)", cube)))
                    match cube:
                        case str(a) if "red" in a:
                            if nb > gameSet["red"]:
                                gameSet["red"] = nb
                        case str(a) if "green" in a:
                            if nb > gameSet["green"]:
                                gameSet["green"] = nb
                        case str(a) if "blue" in a:
                            if nb > gameSet["blue"]:
                                gameSet["blue"] = nb
            gamePower.append(reduce(lambda a, b: a*b, gameSet.values()))
    return reduce(lambda a, b: a+b, gamePower)


def day3_part1():
    print("Day 3")
    # matrice=[]
    numbers = []
    symbols = []
    with resource_stream('input', 'D3.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            # matrice.append(line)
            numbers.append([(m.start(), m.end(), int(m.group()))
                           for m in finditer(r"\d+", line)])
            symbols.append([(m.start(), m.group())
                           for m in finditer(r"[^\d.]", line)])
    res = []
    for i in range(len(symbols)):
        for symbol in symbols[i]:
            voisin = range(symbol[0]-1, symbol[0]+1+1)
            if i-1 >= 0:
                for number in numbers[i-1]:
                    nbrange = range(number[0], number[1])
                    intersect = [v for v in nbrange if v in voisin]
                    if len(intersect) != 0:
                        res.append(number[2])
            for number in numbers[i]:
                if number[1] == symbol[0] or number[0] == symbol[0]+1:
                    res.append(number[2])
            if i+1 < len(symbols):
                for number in numbers[i+1]:
                    nbrange = range(number[0], number[1])
                    intersect = [v for v in nbrange if v in voisin]
                    if len(intersect) != 0:
                        res.append(number[2])
    return reduce(lambda a, b: a+b, res)


def day3_part2():
    print("Day 3")
    numbers = []
    symbols = []
    with resource_stream('input', 'D3.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            # matrice.append(line)
            numbers.append([(m.start(), m.end(), int(m.group()))
                           for m in finditer(r"\d+", line)])
            symbols.append([(m.start(), m.group())
                           for m in finditer(r"\*", line)])
    res = []
    for i in range(len(symbols)):
        for symbol in symbols[i]:
            gears = []
            voisin = range(symbol[0]-1, symbol[0]+1+1)
            if i-1 >= 0:
                for number in numbers[i-1]:
                    nbrange = range(number[0], number[1])
                    intersect = [v for v in nbrange if v in voisin]
                    if len(intersect) != 0:
                        gears.append(number[2])
            for number in numbers[i]:
                if number[1] == symbol[0] or number[0] == symbol[0]+1:
                    gears.append(number[2])
            if i+1 < len(symbols):
                for number in numbers[i+1]:
                    nbrange = range(number[0], number[1])
                    intersect = [v for v in nbrange if v in voisin]
                    if len(intersect) != 0:
                        gears.append(number[2])
            res.append(gears)
    a = 0
    for gears in res:
        if len(gears) == 2:
            a += gears[0]*gears[1]
    return a


def day4_part1():
    print("Day 4")
    res = []
    with resource_stream('input', 'D4.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            numbers = line.split(":")[1].split("|")
            winningNumbers, givenNumbers = numbers[0].split(
            ), numbers[1].split()
            power = -1
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    power += 1
            if power >= 0:
                res.append(pow(2, power))
    return reduce(lambda a, b: a+b, res)


def day4_part2():
    print("Day 4")
    with resource_stream('input', 'D4.txt') as textInput:
        lines = textInput.readlines()
        cardnumbers = [1 for line in lines]
        for i in range(len(cardnumbers)):
            line = lines[i].decode().strip()
            numbers = line.split(":")[1].split("|")
            winningNumbers, givenNumbers = numbers[0].split(
            ), numbers[1].split()
            nbValide = 0
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    nbValide += 1
            for j in range(i+1, i+1+nbValide):
                if j > len(cardnumbers):
                    break
                cardnumbers[j] += cardnumbers[i]
    return reduce(lambda a, b: a+b, cardnumbers)


def day6_part1():
    print("day 6")
    times, distances = [], []
    with resource_stream('input', 'D6.txt') as textInput:
        lines = textInput.readlines()
        times = lines[0].decode().strip().split(":")[-1].split()
        distances = lines[1].decode().strip().split(":")[-1].split()
    nbSoluce = []
    for i in range(len(times)):
        # D=times[i]*x-x²
        nbsol = 0
        time = int(times[i])
        distance = int(distances[i])
        for x in range(time):
            if (x*time)-(x**2) > distance:
                nbsol += 1
        nbSoluce.append(nbsol)
    return reduce(lambda a, b: a*b, nbSoluce)


def day6_part2():
    print("day 6")
    with resource_stream('input', 'D6.txt') as textInput:
        lines = textInput.readlines()

        time = int(sub(r"\s", "",
                   lines[0].decode().strip().split(":")[-1]))
        distance = int(
            sub(r"\s", "", lines[1].decode().strip().split(":")[-1]))
    # D=times[i]*x-x²
    nbsol = 0
    for x in range(time):
        if (x*time)-(x**2) > distance:
            nbsol += 1
    return nbsol


def day8_part1():
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


def day8_part2():
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

    curentNodes = [s for s in nodes.keys() if s.endswith("A")]
    nbstep = 0
    while not listStrEndsWith(curentNodes, "Z"):
        d = 0 if directions[nbstep % len(directions)] == "L" else 1
        for i in range(len(curentNodes)):
            curentNodes[i] = nodes[curentNodes[i]][d]
        nbstep += 1
    return nbstep


def calcNextValue(listValues: list[int]):
    flagRec = False
    for value in listValues:
        if value != 0:
            flagRec = True
            break
    if not flagRec:
        return 0
    ecartValues = [listValues[i+1]-listValues[i]
                   for i in range(len(listValues)-1)]
    r = listValues[-1]+calcNextValue(ecartValues)
    return r


def day9_part1():
    print("day 9")
    histories = []
    nextValues = []
    with resource_stream('input', 'D9.txt') as textInput:
        histories = [[int(x) for x in line.decode().strip().split()]
                     for line in textInput.readlines()]
    for history in histories:
        nextValues.append(calcNextValue(history))
    return reduce(lambda a, b: a+b, nextValues)


def calcPreviousValue(listValues: list[int]):
    flagRec = False
    for value in listValues:
        if value != 0:
            flagRec = True
            break
    if not flagRec:
        return 0
    ecartValues = [listValues[i+1]-listValues[i]
                   for i in range(len(listValues)-1)]
    r = listValues[0]-calcPreviousValue(ecartValues)
    return r


def day9_part2():
    print("day 9")
    histories = []
    nextValues = []
    with resource_stream('input', 'D9.txt') as textInput:
        histories = [[int(x) for x in line.decode().strip().split()]
                     for line in textInput.readlines()]
    for history in histories:
        nextValues.append(calcPreviousValue(history))
    return reduce(lambda a, b: a+b, nextValues)


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


def day11_part1():
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


# day5Class = Day5("D5.txt")
# print(day5Class.part2())
# day7 = Day7("D7.txt")
# print(day7.part2())
# print(day9_part2())
print(day11_part1())
