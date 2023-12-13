from functools import reduce
from re import sub
from pkg_resources import resource_stream


def part1():
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


def part2():
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
