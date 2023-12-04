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
    possibleGame=[]
    with resource_stream('input', 'D2.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
            lineSplit=line.split(":")
            gameID=int(lineSplit[0].strip("Game "))
            cubeSets=lineSplit[-1].split(";")
            flagValide=True
            for cubeSet in cubeSets:
                if not flagValide:
                    break
                cubes=cubeSet.strip().split(", ")
                for cube in cubes:
                    if not flagValide:
                        break
                    nb=int(*(re.findall("(\d+)",cube)))
                    match cube:
                        case str(a) if "red" in a:
                            if nb>12:
                                flagValide=False
                        case str(a) if "green" in a:
                            if nb>13:
                                flagValide=False
                        case str(a) if "blue" in a:
                            if nb>14:
                                flagValide=False
            if flagValide: possibleGame.append(gameID)
    return reduce(lambda a,b: a+b, possibleGame)

def day2_part2():
    print("day 2")
    gamePower=[]
    with resource_stream('input', 'D2.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
            lineSplit=line.split(":")
            cubeSets=lineSplit[-1].split(";")
            gameSet={"red":0,"green":0,"blue":0}
            for cubeSet in cubeSets:
                cubes=cubeSet.strip().split(", ")
                for cube in cubes:
                    nb=int(*(re.findall("(\d+)",cube)))
                    match cube:
                        case str(a) if "red" in a:
                            if nb>gameSet["red"]:
                                gameSet["red"]=nb
                        case str(a) if "green" in a:
                            if nb>gameSet["green"]:
                                gameSet["green"]=nb
                        case str(a) if "blue" in a:
                            if nb>gameSet["blue"]:
                                gameSet["blue"]=nb
            gamePower.append(reduce(lambda a,b:a*b,gameSet.values()))
    return reduce(lambda a,b: a+b, gamePower)


def day4_part1():
    print("Day 4")
    res=[]
    with resource_stream('input', 'D4.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
            numbers=line.split(":")[1].split("|")
            winningNumbers,givenNumbers=numbers[0].split(),numbers[1].split()
            power=-1
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    power+=1
            if power>=0:
                res.append(pow(2,power))
    return reduce(lambda a,b: a+b, res)

def day4_part2():
    print("Day 4")
    with resource_stream('input', 'D4.txt') as textInput:
        lines=textInput.readlines()
        cardnumbers=[1 for line in lines]
        for i in range(len(cardnumbers)):
            line = lines[i].decode().removesuffix("\n")
            numbers=line.split(":")[1].split("|")
            winningNumbers,givenNumbers=numbers[0].split(),numbers[1].split()
            nbValide=0
            for givenNumber in givenNumbers:
                if givenNumber in winningNumbers:
                    nbValide+=1
            for j in range(i+1,i+1+nbValide):
                if j>len(cardnumbers):
                    break
                cardnumbers[j]+=cardnumbers[i]
    return reduce(lambda a,b: a+b, cardnumbers)


print(day4_part2())
