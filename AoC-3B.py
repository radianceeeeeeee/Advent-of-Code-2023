import math

f = open("AoC-3.in", "r")

def isNumber(char):
    if 47 < ord(char) < 58:
        return True
    
    return False

def isAsterisk(char):
    return ord(char) == 42

grid = []

for x in f.readlines():
    # pad the leftmost and rightmost columns
    grid.append(["."] + list(x.rstrip("\n")) + ["."])

# pad the topmost and bottommost rows
extraRow = ["."] * len(grid[0])
grid = [extraRow] + grid + [extraRow]

partNumbers = [[]] # pad with extra list to be consistent with asteriskLocations being 1-based
asteriskLocations = []

for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if isAsterisk(grid[r][c]):
            asteriskLocations.append((r, c))


def sweep_number(r, c):
    n = 0

    # break immediately if square is not a number
    if not isNumber(grid[r][c]):
        return n
    
    # sweep to the left first to get the most significant digit
    while c > 0 and isNumber(grid[r][c]):
        c -= 1

    # then sweep to the right to get the other digits
    c += 1
    while len(grid[0]) > c and isNumber(grid[r][c]):
        n *= 10
        n += int(grid[r][c])
        c += 1

    return n


def sweep_neighbors(r, c):
    nums = set()

    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            nums.add(sweep_number(i, j))

    nums.remove(0)
    return nums

sum = 0

for r, c in asteriskLocations:
    s = sweep_neighbors(r, c)
    if len(s) == 2:
        sum += s.pop() * s.pop()

print(sum)