# Advent Of Code 2023

from pkg_resources import resource_stream
from functools import reduce
from re import sub

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
    with resource_stream('input', 'D1test.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().removesuffix("\n")
            for k, v in transTable.items():
                line = sub(k, v, line)
            numbers = sub("\D", "", line)
            lineNumber = "".join([numbers[0], numbers[-1]])
            listNumber.append(int(lineNumber))
    return reduce(lambda a, b: a+b, listNumber)


print(day1_part1())
