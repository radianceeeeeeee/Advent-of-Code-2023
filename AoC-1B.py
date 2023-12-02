import re

f = open("AoC-1.in", "r")

spelledOut = {"one": "1", 
              "two": "2", 
              "three": "3", 
              "four": "4", 
              "five": "5", 
              "six": "6", 
              "seven": "7", 
              "eight": "8", 
              "nine": "9"}

def strToInt(str1, str2):
    if str1 in spelledOut.keys():
        str1 = spelledOut[str1]

    if str2 in spelledOut.keys():
        str2 = spelledOut[str2]

    return int(str1 + str2)    

sum = 0
for x in f.readlines():
    firstNum = re.findall("[1-9]|one|two|three|four|five|six|seven|eight|nine", x)[0]

    for i in range(len(x) + 1): 
        findLastNumbers = re.findall("[1-9]|one|two|three|four|five|six|seven|eight|nine", x[len(x) - i:]) # find backwards
        if len(findLastNumbers) == 1: # if a match is found, return as second number
            secondNum = findLastNumbers[0]
            break
        
    calibration = strToInt(firstNum, secondNum)
    sum += calibration

print(sum)
