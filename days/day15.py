from functools import reduce
from pkg_resources import resource_stream


def part1():
    print("day 15")
    hashStrings = []
    with resource_stream('input', 'D15.txt') as textInput:
        hashStrings = textInput.readline().decode().strip().split(",")
    res = []
    for hashString in hashStrings:
        tmp = 0
        for c in hashString:
            tmp += ord(c)
            tmp *= 17
            tmp %= 256
        res.append(tmp)
    return reduce(lambda a, b: a+b, res)
