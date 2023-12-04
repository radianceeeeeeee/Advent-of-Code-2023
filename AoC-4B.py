from collections import defaultdict

f = open("AoC-4.in", "r")

scratchCards = 0

copies = defaultdict(int)

for x in f.readlines():
    # pad the leftmost and rightmost columns
    card, twoList = x.rstrip("\n").split(": ")
    cardNumber = int(card.split(" ")[-1])

    copies[cardNumber] += 1 # original copy
    
    winningStr, ownedStr = twoList.split(" | ")
    winningNumbers = [int(winningStr[i:i+2]) for i in range(0, len(winningStr), 3)]
    ownedNumbers = [int(ownedStr[i:i+2]) for i in range(0, len(ownedStr), 3)]

    matchedNumbers = 0

    for n in winningNumbers:
        if n in ownedNumbers:
            matchedNumbers += 1

    for n in range(cardNumber + 1, cardNumber + matchedNumbers + 1):
        copies[n] += 1 * copies[cardNumber]


scratchCards = 0

for c in copies:
    scratchCards += copies[c]

print(scratchCards)