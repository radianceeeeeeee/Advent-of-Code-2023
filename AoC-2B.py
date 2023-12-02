f = open("AoC-2.in", "r")

sum = 0
for x in f.readlines():
    input = x.rstrip("\n").split(" ")
    id = int(input[1][:-1])

    maxCubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for i in range(2, len(input), 2):
        count = int(input[i].rstrip(",;"))
        color = input[i + 1].rstrip(",;")

        maxCubes[color] = max(maxCubes[color], count)

    sum += maxCubes["red"] * maxCubes["green"] * maxCubes["blue"]

print(sum)