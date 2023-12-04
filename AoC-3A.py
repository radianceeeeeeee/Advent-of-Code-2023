import functools

f = open("AoC-3.in", "r")

def isNumber(char):
    if 47 < ord(char) < 58:
        return True
    
    return False


def isSymbol(char):
    if ord(char) == 46 or isNumber(char): # ord(46) is .
        return False
    
    return True
    

def sweep_row(top, mid, bot):
    numbers = []

    numberOngoing = False
    symbolFound = False
    currentNumber = ""

    for i in range(1, len(mid) - 1): # rows are padded with periods
        if isNumber(mid[i]):
            numberOngoing = True
            currentNumber += mid[i]

            # split into three if statements because it's too long
            if isSymbol(top[i - 1]) or isSymbol(top[i]) or isSymbol(top[i + 1]):
                symbolFound = True
            if isSymbol(mid[i - 1]) or isSymbol(mid[i + 1]):
                symbolFound = True
            if isSymbol(bot[i - 1]) or isSymbol(bot[i]) or isSymbol(bot[i + 1]):
                symbolFound = True

            if i == len(mid) - 2:   # second to the last column
                if symbolFound:
                    numbers.append(int(currentNumber))
                currentNumber = ""

        else:
            if numberOngoing:
                if symbolFound:
                    numbers.append(int(currentNumber))
                currentNumber = ""

            # reset 
            numberOngoing = False
            symbolFound = False

    return numbers

grid = []

sum = 0
for x in f.readlines():
    # pad the leftmost and rightmost columns
    grid.append(["."] + list(x.rstrip("\n")) + ["."])

# pad the topmost and bottommost rows
extraRow = ["."] * len(grid[0])
grid = [extraRow] + grid + [extraRow]

sum = 0
for r in range(1, len(grid) - 1):
    partNumbers = sweep_row(grid[r - 1], grid[r], grid[r + 1])
    sum = functools.reduce(lambda a, b : a + b, partNumbers, sum)

print(sum)