from pkg_resources import resource_stream


def part1():
    print("day 13")
    paterns = []
    with resource_stream('input', 'D13.txt') as textInput:
        patern = []
        for line in textInput.readlines():
            line = line.decode().strip()
            if not line:
                paterns.append(patern)
                patern = []
            else:
                patern.append(line)
        paterns.append(patern)
    res = 0
    for patern in paterns:
        LINE_NB = len(patern)
        COL_NB = len(patern[0])
        #col sym
        for c in range(COL_NB-1):
            diffNb = 0
            for dc in range(COL_NB):
                left = c-dc
                right = c+1+dc
                if 0 <= left < right < COL_NB:
                    for l in range(LINE_NB):
                        if patern[l][left] != patern[l][right]:
                            diffNb += 1
            if diffNb == 0:
                res += c+1
        #line sym
        for l in range(LINE_NB-1):
            diffNb = 0
            for dr in range(LINE_NB):
                up = l-dr
                down = l+1+dr
                if 0 <= up < down < LINE_NB:
                    for c in range(COL_NB):
                        if patern[up][c] != patern[down][c]:
                            diffNb += 1
            if diffNb == 0:
                res += 100*(l+1)
    return res

def part2():
    print("day 13")
    paterns = []
    with resource_stream('input', 'D13.txt') as textInput:
        patern = []
        for line in textInput.readlines():
            line = line.decode().strip()
            if not line:
                paterns.append(patern)
                patern = []
            else:
                patern.append(line)
        paterns.append(patern)
    res = 0
    for patern in paterns:
        LINE_NB = len(patern)
        COL_NB = len(patern[0])
        #col sym
        for c in range(COL_NB-1):
            diffNb = 0
            for dc in range(COL_NB):
                left = c-dc
                right = c+1+dc
                if 0 <= left < right < COL_NB:
                    for l in range(LINE_NB):
                        if patern[l][left] != patern[l][right]:
                            diffNb += 1
            if diffNb == 1:
                res += c+1
        #line sym
        for l in range(LINE_NB-1):
            diffNb = 0
            for dr in range(LINE_NB):
                up = l-dr
                down = l+1+dr
                if 0 <= up < down < LINE_NB:
                    for c in range(COL_NB):
                        if patern[up][c] != patern[down][c]:
                            diffNb += 1
            if diffNb == 1:
                res += 100*(l+1)
    return res
