from functools import reduce
from re import sub
from pkg_resources import resource_stream


def part1():
    listNumber = []
    with resource_stream('input', 'D1.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            numbers = sub(r"\D", "", line)
            lineNumber = "".join([numbers[0], numbers[-1]])
            listNumber.append(int(lineNumber))
    return reduce(lambda a, b: a+b, listNumber)


def part2():
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
