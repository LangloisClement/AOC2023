from enum import Enum
from pkg_resources import resource_stream


Direction=Enum("Direction",["UP","RIGHT","DOWN","LEFT"])

def part1():
    print("day 10")
    maze = []
    with resource_stream('input', 'D10.txt') as textInput:
        maze = [line.decode().strip() for line in textInput.readlines()]
    ROW=len(maze)
    COL=len(maze[0])
    start=None
    d=None
    for r in range(ROW):
        if start:
            break
        for c in range(COL):
            if maze[r][c]=='S':
                start=[r,c]
                voisins=[maze[r-1][c],maze[r][c+1],maze[r+1][c],maze[r][c-1]]
                if voisins[0] in "F7|":
                    d=Direction.UP
                elif voisins[1] in "-7J":
                    d=Direction.RIGHT
                elif voisins[2] in "|LJ":
                    d=Direction.DOWN
                elif voisins[3] in "-FL":
                    d=Direction.LEFT
                else:
                    raise ValueError("No valide neighbor")
                break
    dist=0
    current=[start[0],start[1]]
    while True:
        match d:
            case Direction.UP:
                current[0]-=1
            case Direction.RIGHT:
                current[1]+=1
            case Direction.DOWN:
                current[0]+=1
            case Direction.LEFT:
                current[1]-=1
        dist+=1
        if current==start:
            break
        match maze[current[0]][current[1]]:
            case "F":
                d=Direction.RIGHT if d==Direction.UP else Direction.DOWN
            case "-":
                d=Direction.LEFT if d==Direction.LEFT else Direction.RIGHT
            case "7":
                d=Direction.LEFT if d==Direction.UP else Direction.DOWN
            case "|":
                d=Direction.DOWN if d==Direction.DOWN else Direction.UP
            case "J":
                d=Direction.LEFT if d==Direction.DOWN else Direction.UP
            case "L":
                d=Direction.RIGHT if d==Direction.DOWN else Direction.UP
            
        
    return dist//2
