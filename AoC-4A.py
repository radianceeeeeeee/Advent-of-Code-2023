f = open("AoC-4.in", "r")

sum = 0
for x in f.readlines():
    # pad the leftmost and rightmost columns
    _, twoList = x.rstrip("\n").split(": ")
    winningStr, ownedStr = twoList.split(" | ")
    winningNumbers = [int(winningStr[i:i+2]) for i in range(0, len(winningStr), 3)]
    ownedNumbers = [int(ownedStr[i:i+2]) for i in range(0, len(ownedStr), 3)]

    matchedNumbers = 0

    for n in winningNumbers:
        if n in ownedNumbers:
            matchedNumbers += 1

    sum += 2 ** (matchedNumbers - 1) if matchedNumbers != 0 else 0


print(sum)
