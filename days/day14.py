from pkg_resources import resource_stream
from re import findall


def part1():
    print("day 14")
    platform = []
    with resource_stream('input', 'D14.txt') as textInput:
        platform = [line.decode().strip() for line in textInput.readlines()]

    tiltNorth(platform)
    res = 0
    for row in range(len(platform)):
        nbRounRock = len(findall("O", platform[row]))
        res += nbRounRock*(len(platform)-row)
    return res


def tiltNorth(platform):
    colToChange = [i for i in range(len(platform[0]))]
    while len(colToChange) != 0:
        for col in colToChange:
            change = False
            for row in range(1, len(platform)):
                if platform[row][col] == "O" and platform[row-1][col] == ".":
                    platform[row] = ".".join(
                        [platform[row][:col], platform[row][col+1:]])
                    platform[row-1] = "O".join(
                        [platform[row-1][:col], platform[row-1][col+1:]])
                    change = True
            if not change:
                colToChange.remove(col)


def tiltSouth(platform):
    colToChange = [i for i in range(len(platform[0]))]
    while len(colToChange)!=0:
        for col in colToChange:
            change = False
            for row in range(len(platform)-2, -1, -1):
                if platform[row][col] == "O" and platform[row+1][col] == ".":
                    platform[row] = ".".join(
                        [platform[row][:col], platform[row][col+1:]])
                    platform[row+1] = "O".join(
                        [platform[row+1][:col], platform[row+1][col+1:]])
                    change = True
            if not change:
                colToChange.remove(col)


def tiltWest(platform):
    rowToChange = [i for i in range(len(platform))]
    while len(rowToChange)!=0:
        for row in rowToChange:
            change = False
            for col in range(1, len(platform[0])):
                if platform[row][col] == "O" and platform[row][col-1] == ".":
                    change = True
                    platform[row] = platform[row][:col-1] + \
                        "O."+platform[row][col+1:]
            if not change:
                rowToChange.remove(row)


def tiltEst(platform):
    rowToChange = [i for i in range(len(platform))]
    while len(rowToChange)!=0:
        change = False
        for row in rowToChange:
            for col in range(len(platform[0])-2, -1, -1):
                if platform[row][col] == "O" and platform[row][col+1] == ".":
                    change = True
                    platform[row] = platform[row][:col] + \
                        ".O"+platform[row][col+2:]
            if not change:
                rowToChange.remove(row)


def part2():
    print("day 14")
    platform = []
    with resource_stream('input', 'test.txt') as textInput:
        platform = [line.decode().strip() for line in textInput.readlines()]
    for i in range(1000000000):
        tiltNorth(platform)
        tiltWest(platform)
        tiltSouth(platform)
        tiltEst(platform)
    res = 0
    for row in range(len(platform)):
        nbRounRock = len(findall("O", platform[row]))
        res += nbRounRock*(len(platform)-row)
    return res
