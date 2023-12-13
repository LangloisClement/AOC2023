from functools import reduce
from re import findall
from pkg_resources import resource_stream


def part1():
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


def part2():
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
