import re

lines = []
hash = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9 
}

outs = ["a", "b", "c","d", "j", "k", "l", "m", "p", "q", "y", "z"]

with open("input.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()
    file.close()

def task1():
    sum = 0

    for line in lines:
        filtered = re.sub("[^0-9]", "", line)
        if len(filtered) > 1:
            sum += int(filtered[0]+filtered[-1])
        elif len(filtered) == 1:
            sum += int(filtered[0]+filtered[0])
        else:
            sum += 0
    
    print(sum)

def task2():
    subs = []
    subsAll = []
    for line in lines:
        line = ''.join(char for char in line if char not in outs)
        current = ""
        for character in line:
            if character.isnumeric():
                subs.append(int(character))
            else:
                current += character
                if len(current) > 2:
                    for nums in list(hash.keys()):
                        if nums in current:
                            subs.append(hash.get(nums))
                            current = character
                            break
        subsAll.append(subs)
        subs = []

    sum = 0

    for line in subsAll:
        print(line)
        if len(line) > 1:
            sum2 += line[0] * 10 + line[-1]
        elif len(line) == 1:
            sum2 += line[0] * 10 + line[0]
        else:
            sum += 0
    print(sum)


