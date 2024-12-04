from helpers import abs, read_lines

lines = read_lines("input.txt")
letters = list("XMAS")

grid = []
for y, line in enumerate(lines):
    grid.append([])
    for x, c in enumerate(line.strip()):
        grid[y].append(c)

width = len(grid[0])
height = len(grid)

for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] not in letters:
            grid[y][x] = "."


def printGrid(grid):
    for line in grid:
        print(" ".join(line))


def checkX(x: int, y: int, direction: tuple[int,int]) -> bool:
    c = grid[y][x]
    if c != "X":
        return False

    dx = direction[0]
    dy = direction[1]

    # check for M
    i = 1
    while i < len(letters):
        my = y + i * dy
        mx = x + i * dx
        if my < 0 or my >= height:
            return False
        if mx < 0 or mx >= width:
            return False
        if grid[my][mx] != letters[i]:
            return False
        i += 1
    return True

def checkA(x,y):
    if grid[y][x] != "A":
        return False

    A = 0
    B = 1
    C = 0
    D = 1

    for A,B,C,D in [("M", "S", "M", "S"), ("M", "M", "S", "S"), ("S", "M", "S", "M"), ("S", "S", "M", "M")]:
        if x > 0 and y > 0 and grid[y-1][x-1] == A:
            if x < width-1 and y>0 and grid[y-1][x+1] == B:
                if x > 0 and y < height - 1 and grid[y+1][x-1] == C:
                    if x < width - 1 and y < height -1 and grid[y+1][x+1] == D:
                        # print("Found at ", x,y)
                        return True


    return False
directions = [
    (-1,0),
    (-1, 1),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1,-1),
    (1,0),
    (1,1)
]

def countGrid(grid):
    count = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] != "X":
                continue

            for direction in directions:
                if checkX(x,y,direction):
                    count +=1

    return count

def countGridPart2(grid):
    count = 0
    for y in range(height):
        for x in range(width):
            if checkA(x,y):
                count +=1

    return count

print ("part1", countGrid(grid) )
print ("part2", countGridPart2(grid) )