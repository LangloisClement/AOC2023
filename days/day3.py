from functools import reduce
from re import finditer
from pkg_resources import resource_stream


def part1():
    print("Day 3")
    numbers = []
    symbols = []
    with resource_stream('input', 'D3.txt') as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
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


def part2():
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
