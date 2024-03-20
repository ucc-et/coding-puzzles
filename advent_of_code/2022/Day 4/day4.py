pairs = []

def processFile(path):
    with open(path) as file:
        elves = file.readlines()
        for pair in elves:
            pairs.append(pair.strip().split(","))

def findContained():
    contained = 0
    for pair in pairs:
        elf1, elf2 = pair[0].split("-"), pair[1].split("-")
        if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
            contained += 1
    return contained

def checkIfOverlapped(x, y):
    a = (x[0] <= y[0] and x[1] >= y[1])
    b = (y[0] <= x[0] and y[1] >= x[1])
    c = (x[0] == y[0]  or x[0] == y[1] or x[1] == y[0] or x[1] == y[1])
    d = (x[0] <= y[0] and x[1] >= y[0])
    e = (y[0] <= x[0] and y[1] >= x[0])
    return a or b or c or d or e

def findOverlapped():
    overlap = 0
    for pair in pairs:
        elf1, elf2 = pair[0].split("-"), pair[1].split("-")
        elf1[0], elf1[1], elf2[0], elf2[1] = int(elf1[0]), int(elf1[1]), int(elf2[0]), int(elf2[1])
        if (checkIfOverlapped(elf1, elf2)):
            overlap += 1
    return overlap

processFile("day_4_input.txt")
print(findOverlapped())
