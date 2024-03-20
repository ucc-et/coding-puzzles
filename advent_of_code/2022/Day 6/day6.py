def openFile(path):
    with open(path) as file:
        line = file.readline()
    return line

def findStart4(path):
    line = openFile(path)
    charactersCounted = 4
    for i in range(len(line)-3):
        #print(line[i]+line[i+1]+line[i+2]+line[i+3])
        if line[i] != line[i+1] and line[i] != line[i+2] and line[i] != line[i+3]:
            if line[i+1] != line[i+2] and line[i+1] != line[i+3]:
                if line[i+2] != line[i+3]:
                    charactersCounted += i
                    break
    print(charactersCounted)

def parseStringToList(string):
    returnList = []
    for character in string:
        returnList.append(character)
    return returnList

def findStart14(path):
    line = openFile(path)
    charactersCounted = 14
    characters = []
    for i in range(len(line)-13):
        #print(line[i]+line[i+1]+line[i+2]+line[i+3])
        characters = parseStringToList(line[i:i+14])
        if len(characters) == len(set(characters)):
            print(characters)
            charactersCounted += i
            break
    print(charactersCounted)

findStart14("day_6_input.txt")
