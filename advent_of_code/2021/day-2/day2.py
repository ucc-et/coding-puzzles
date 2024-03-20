
mainInput = []

with open('input.txt') as file:
    inputList = file.readlines()
    for line in range(len(inputList)):
        inputList[line] = inputList[line].replace('\n', '')

    mainInput = inputList

horizontal = 0
depth = 0

for i in range(len(mainInput)):
    directionCmd = mainInput[i]
    length = len(directionCmd)-2
    direction = directionCmd[0:length]
    amount = int(float(directionCmd[-1:]))
    if direction == 'forward':
        horizontal += int(amount)
    elif direction == 'down':
        depth += int(amount)
    elif direction == 'up':
        depth -= int(amount)

print('Part 1: ', horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for i in range(len(mainInput)):
    directionCmd = mainInput[i]
    length = len(directionCmd)-2
    direction = directionCmd[0:length]
    amount = int(float(directionCmd[-1:]))
    if direction == 'forward':
        horizontal += int(amount)
        depth += (aim * int(amount))
    elif direction == 'down':
        aim += int(amount)
    elif direction == 'up':
        aim -= int(amount)

print('Part 2: ', horizontal * depth)
