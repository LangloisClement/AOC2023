from functools import reduce
from pkg_resources import resource_stream


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


def part1():
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


def part2():
    print("day 9")
    histories = []
    nextValues = []
    with resource_stream('input', 'D9.txt') as textInput:
        histories = [[int(x) for x in line.decode().strip().split()]
                     for line in textInput.readlines()]
    for history in histories:
        nextValues.append(calcPreviousValue(history))
    return reduce(lambda a, b: a+b, nextValues)
