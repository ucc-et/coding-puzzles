def openFile(path):
    with open(path) as file:
        lines = file.readlines()
        stack = parseStack(lines[:8])
        instructions = parseInstructions(lines[10:])
    return stack, instructions

def parseInstructions(instructions):
    parsedInstructions = []
    for instruction in instructions:
        a = instruction.split()
        parsedInstructions.append((a[1], a[3], a[5]))
    return parsedInstructions

def parseStack(stack):
    stackLines = []
    for line in stack:
        lines = ""
        for letter in line[:-1]:
            if letter == " ":
                if len(lines) == 0:
                    lines += "["
                elif lines[-1] == "-":
                    lines += "["
                elif lines[-1] == "[":
                    lines += "0"
                elif lines[-1] == "0":
                    lines += "]"
                else:
                    lines += "-"
            else:
                lines += letter
        stackLines.append(lines.split("-"))
    for idy, line in enumerate(stackLines):
        for idx, element in enumerate(line):
            stackLines[idy][idx] = element.replace("[", "").replace("]", "")
    
    currentStack = {}
    listNum = 0
    for i in range(len(stackLines[0])):
        listNum += 1
        for j in range(len(stackLines)-1, -1, -1):
            if not stackLines[j][i] == "0":
                if str(listNum) in currentStack.keys():
                    currentStack[str(listNum)].append(stackLines[j][i])
                else:
                    currentStack[str(listNum)] = [stackLines[j][i]]
    return currentStack

def move9000(amount, source, goal, dict):
    if amount == 0:
        return dict
    
    elem, dict[str(source)] = dict[str(source)][-1], dict[str(source)][:-1]
    dict[str(goal)].append(elem)
    
    move9000(amount-1, source, goal, dict)

def move9001(amount, source, goal, dict):
    elem, dict[str(source)] = dict[str(source)][amount *(-1):], dict[str(source)][:amount *(-1)]
    for crate in elem:
        dict[str(goal)].append(crate)
    
    return dict

def moveStacks():
    
    stack, instructions = openFile('day_5_input.txt')
    for instruction in instructions:
        move9001(int(instruction[0]), instruction[1], instruction[2], stack)
    
    sol = ""
    for key in stack.keys():
        sol+=stack[key][-1]
    print(sol)

moveStacks()
