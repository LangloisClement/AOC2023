from enum import Enum
from pkg_resources import resource_stream


Direction = Enum("Direction", ["UP", "RIGHT", "DOWN", "LEFT"])


def part1():
    print("day 16")
    wall = []
    with resource_stream('input', 'D16.txt') as textInput:
        wall = [line.decode().strip() for line in textInput.readlines()]

    return energized(0, 0, Direction.RIGHT, wall)


def energized(startRow: int, startCol: int, startDirection: Direction, wall: list[str]):
    ROW = len(wall)
    COL = len(wall[0])
    seen = set()
    activeBeams = [(startRow, startCol, startDirection)]
    while len(activeBeams) > 0:
        r, c, d = activeBeams[0]
        if not (0 <= r < ROW and 0 <= c < COL):
            # OUT OF BOUND CELL
            activeBeams.remove((r, c, d))
            continue
        if (r, c, d) in seen:
            # LOOP DETECTION
            activeBeams.remove((r, c, d))
            continue
        seen.add((r, c, d))
        nextR, nextC, nextD = 0, 0, None
        match wall[r][c]:
            case ".":
                match d:
                    case Direction.UP:
                        nextR = r-1
                        nextC = c
                    case Direction.DOWN:
                        nextR = r+1
                        nextC = c
                    case Direction.RIGHT:
                        nextR = r
                        nextC = c+1
                    case Direction.LEFT:
                        nextR = r
                        nextC = c-1
                nextD = d
            case "/":
                match d:
                    case Direction.UP:
                        nextD = Direction.RIGHT
                        nextR = r
                        nextC = c+1
                    case Direction.DOWN:
                        nextD = Direction.LEFT
                        nextR = r
                        nextC = c-1
                    case Direction.RIGHT:
                        nextD = Direction.UP
                        nextR = r-1
                        nextC = c
                    case Direction.LEFT:
                        nextD = Direction.DOWN
                        nextR = r+1
                        nextC = c
            case "\\":
                match d:
                    case Direction.UP:
                        nextD = Direction.LEFT
                        nextR = r
                        nextC = c-1
                    case Direction.DOWN:
                        nextD = Direction.RIGHT
                        nextR = r
                        nextC = c+1
                    case Direction.RIGHT:
                        nextD = Direction.DOWN
                        nextR = r+1
                        nextC = c
                    case Direction.LEFT:
                        nextD = Direction.UP
                        nextR = r-1
                        nextC = c
            case "-":
                match d:
                    case Direction.UP | Direction.DOWN:
                        activeBeams.append((r, c-1, Direction.LEFT))
                        nextD = Direction.RIGHT
                        nextR = r
                        nextC = c+1
                    case Direction.RIGHT | Direction.LEFT:
                        nextD = d
                        nextR = r
                        nextC = c+1 if d == Direction.RIGHT else c-1
            case "|":
                match d:
                    case Direction.UP | Direction.DOWN:
                        nextD = d
                        nextR = r+1 if d == Direction.DOWN else r-1
                        nextC = c
                    case Direction.RIGHT | Direction.LEFT:
                        activeBeams.append((r+1, c, Direction.DOWN))
                        nextD = Direction.UP
                        nextR = r-1
                        nextC = c
        activeBeams[0] = (nextR, nextC, nextD)
    cell = set()
    for cellDirection in seen:
        r, c, d = cellDirection
        cell.add((r, c))
    return len(cell)


def part2():
    print("day 16")
    wall = []
    with resource_stream('input', 'D16.txt') as textInput:
        wall = [line.decode().strip() for line in textInput.readlines()]
    possibleStart = []
    possibleStart += [(0, c, Direction.DOWN) for c in range(len(wall[0]))]
    possibleStart += [(len(wall)-1, c, Direction.UP)
                      for c in range(len(wall[0]))]
    possibleStart += [(r, 0, Direction.RIGHT) for r in range(len(wall))]
    possibleStart += [(r, len(wall[0])-1, Direction.LEFT)
                      for r in range(len(wall))]
    res = []
    for start in possibleStart:
        r, c, d = start
        res.append(energized(r, c, d, wall))
    return max(res)
