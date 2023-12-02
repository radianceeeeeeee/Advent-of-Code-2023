import re

f = open("AoC-1.in", "r")

sum = 0
for x in f.readlines():
    numbers = re.findall("[1-9]", x)
    calibration = int(numbers[0] + numbers[-1])
    sum += calibration

print(sum)