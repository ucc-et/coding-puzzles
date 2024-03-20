# line => rucksack --> half teh string per compartmens
#a -> z (1->26) || A -> Z (27 -> 52)

backpackContent = []

def readFile(path):
    
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            left = line[:len(line)//2]
            right = line[len(line)//2:]
            backpackContent.append([left, right])

def turnLetterToValue(x: str):
    return ord(x)-38 if not x.islower() else ord(x)-96
    

def getContent():
    backpackSum = 0
    for backpack in backpackContent:
        leftCompartment, rightCompartment = backpack[0], backpack[1]
        for letter in leftCompartment:
            if letter in rightCompartment:
                backpackSum += turnLetterToValue(letter)    
                break
    return backpackSum

def getBadgeValue():
    backpackSum = 0
    lineCount = 0
    while not lineCount >= len(backpackContent): 
        first, second, third = backpackContent[lineCount][0] + backpackContent[lineCount][1], backpackContent[lineCount+1][0] + backpackContent[lineCount+1][1], backpackContent[lineCount+2][0] + backpackContent[lineCount+2][1]
        if len(first) >= len(second) and len(first) >= len(third):
            biggestString = first
        elif len(second) >= len(first) and len(second) >= len(third):
            biggestString = second
        else:
            biggestString = third
        for character in biggestString:
            if character in second and character in third and character in first:
                backpackSum += turnLetterToValue(character)
                break
        lineCount += 3
    return  backpackSum


readFile('day_3_input.txt')
print(getBadgeValue())
