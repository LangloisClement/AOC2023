from pkg_resources import resource_stream


def part1():
    print("day 21")
    garden = []
    with resource_stream('input', 'D21.txt') as textInput:
        garden = [line.decode().strip() for line in textInput.readlines()]
    ROW=len(garden)
    COL=len(garden[0])
    posibleTiles=set()
    for r in range(ROW):
        if len(posibleTiles)>0:
            break
        for c in range(COL):
            if garden[r][c]=="S":
                posibleTiles.add((r,c))
                break
    
    NB_STEP=64
    for i in range(NB_STEP):
        newTiles=set()
        for tile in posibleTiles:
            r,c=tile
            if 0<r and garden[r-1][c]!="#":
                newTiles.add((r-1,c))
            if r<ROW-1 and garden[r+1][c]!="#":
                newTiles.add((r+1,c))
            if 0<c and garden[r][c-1]!="#":
                newTiles.add((r,c-1))
            if c<COL-1 and garden[r][c+1]!="#":
                newTiles.add((r,c+1))
        posibleTiles=newTiles
    return len(posibleTiles)