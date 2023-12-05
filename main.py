# Advent Of Code 2023

from pkg_resources import resource_stream
from functools import reduce
from re import sub
import re

print("hello world")


def day1_part1():
    listNumber = []
    with resource_stream('input', 'D1.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
            numbers = sub("\D", "", line)
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
            line = line.decode().removesuffix("\n")
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
            line = line.decode().removesuffix("\n")
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
                    nb = int(*(re.findall("(\d+)", cube)))
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
            line = line.decode().removesuffix("\n")
            lineSplit = line.split(":")
            cubeSets = lineSplit[-1].split(";")
            gameSet = {"red": 0, "green": 0, "blue": 0}
            for cubeSet in cubeSets:
                cubes = cubeSet.strip().split(", ")
                for cube in cubes:
                    nb = int(*(re.findall("(\d+)", cube)))
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
    res = []
    with resource_stream('input', 'D3.txt') as textInput:
        matrice = [line.decode()[:-1] for line in textInput.readlines()]
        res = []
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if not matrice[i][j].isnumeric() and matrice[i][j] != ".":
                    print(matrice[i][j])
                    if i-1 >= 0:
                        if j-1 >= 0:
                            print(f"upperleft is {matrice[i-1][j-1]}")
                        print(f"upper is {matrice[i-1][j]}")
                        if j+1 <= len(matrice[i]):
                            print(f"upperright is {matrice[i-1][j+1]}")
                    if j-1 >= 0:
                        print(f"left is {matrice[i][j-1]}")
                    if j+1 <= len(matrice[i]):
                        print(f"right is {matrice[i][j+1]}")
                    if i+1 <= len(matrice):
                        if j-1 >= 0:
                            print(f"bottomleft is {matrice[i+1][j-1]}")
                        print(f"bottom is {matrice[i+1][j]}")
                        if j+1 <= len(matrice[i]):
                            print(f"bottomright is {matrice[i+1][j+1]}")

            print("------------------------------------------------")
    return reduce(lambda a, b: a+b, res)


def day4_part1():
    print("Day 4")
    res = []
    with resource_stream('input', 'D4.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
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
            line = lines[i].decode().removesuffix("\n")
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


def day5_xToY_dict(lines: list[str], i: int):
    xToY = {}
    while i < len(lines) and lines[i] != "":
        dest, source, ran = lines[i].split()
        dest, source, ran = int(dest), int(source), int(ran)
        xToY.update([(source+k, dest+k) for k in range(ran)])
        i += 1
    return xToY, i

def day5_xToY_tuples_list(lines: list[str], i: int):
    xToY = []
    while i < len(lines) and lines[i] != "":
        dest, source, ran = lines[i].split()
        dest, source, ran = int(dest), int(source), int(ran)
        xToY.append((dest,source,ran))
        i += 1
    return xToY, i

def day5_findNumber(n: int, tupleList: list(tuple())):
    for t in tupleList:
        if n >= t[1] and n<=t[1]+t[2]:
            diff=n-t[1]
            return diff+t[0]
    return n    

def day5_part1BRUT_FORCE():
    print("Day 5")
    with resource_stream('input', 'D5.txt') as textInput:
        lines = [l.decode().strip() for l in textInput.readlines()]
        seedNumbers = lines[0].split(":")[1].split()
        i = 3
        print("compiling seed to soil")
        seedToSoil, i = day5_xToY_dict(lines, i)
        print("compiling soil to fert")
        soilToFert, i = day5_xToY_dict(lines, i+2)
        print("compiling fert to water")
        fertToWater, i = day5_xToY_dict(lines, i+2)
        print("compiling water to light")
        waterToLight, i = day5_xToY_dict(lines, i+2)
        print("compiling light to temp")
        lightToTemp, i = day5_xToY_dict(lines, i+2)
        print("compiling temp to humi")
        tempToHumidity, i = day5_xToY_dict(lines, i+2)
        print("compiling humi to loc")
        humidityToLoc, i = day5_xToY_dict(lines, i+2)

        seedToSoil.setdefault
        locList = []
        for seed in seedNumbers:
            seed=int(seed)
            soil = seedToSoil.setdefault(seed, seed)
            fert = soilToFert.setdefault(soil, soil)
            water = fertToWater.setdefault(fert, fert)
            light = waterToLight.setdefault(water, water)
            temp = lightToTemp.setdefault(light, light)
            hum = tempToHumidity.setdefault(temp, temp)
            loc = humidityToLoc.setdefault(hum, hum)
            locList.append(loc)

        return locList.sort()[0]

def day5_part1():
    print("Day 5")
    with resource_stream('input', 'D5.txt') as textInput:
        lines = [l.decode().strip() for l in textInput.readlines()]
        seedNumbers = lines[0].split(":")[1].split()
        i = 3
        print("compiling seed to soil")
        seedToSoil, i = day5_xToY_tuples_list(lines, i)
        print("compiling soil to fert")
        soilToFert, i = day5_xToY_tuples_list(lines, i+2)
        print("compiling fert to water")
        fertToWater, i = day5_xToY_tuples_list(lines, i+2)
        print("compiling water to light")
        waterToLight, i = day5_xToY_tuples_list(lines, i+2)
        print("compiling light to temp")
        lightToTemp, i = day5_xToY_tuples_list(lines, i+2)
        print("compiling temp to humi")
        tempToHumidity, i = day5_xToY_tuples_list(lines, i+2)
        print("compiling humi to loc")
        humidityToLoc, i = day5_xToY_tuples_list(lines, i+2)
        locList = []
        for seed in seedNumbers:
            seed=int(seed)
            soil = day5_findNumber(seed,seedToSoil)
            fert = day5_findNumber(soil,soilToFert)
            water = day5_findNumber(fert,fertToWater)
            light = day5_findNumber(water,waterToLight)
            temp = day5_findNumber(light,lightToTemp)
            hum = day5_findNumber(temp,tempToHumidity)
            loc = day5_findNumber(hum,humidityToLoc)
            locList.append(loc)

        locList.sort()
        return locList[0]
    

print(day5_part1())
