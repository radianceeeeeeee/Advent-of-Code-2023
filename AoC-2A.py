f = open("AoC-2.in", "r")

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum = 0
for x in f.readlines():
    input = x.rstrip("\n").split(" ")
    id = int(input[1][:-1])

    dontAdd = False

    for i in range(2, len(input), 2):
        count = int(input[i].rstrip(",;"))
        color = input[i + 1].rstrip(",;")

        if count > cubes[color]:
            dontAdd = True
            break

    if dontAdd: continue

    sum += id

print(sum)