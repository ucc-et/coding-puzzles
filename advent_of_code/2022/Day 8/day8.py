visibleTrees = 0
scenics = {}

def openFile(path="day8_input.txt"):
    trees = []
    with open(path) as file:
        for line in file.readlines():
            trees.append([*line.strip()])
    return trees

def isVisible(trees, x, y):
    #check if Edge
    if (y == 0 or y == len(trees)-1) or (x == 0 or x == len(trees[0])-1):
        return True
    #visibleFromTop
    
    isVisible = {"top": True, "right": True, "down": True, "left": True}
    for a in range(y):
        if int(trees[a][x]) >= int(trees[y][x]):
            isVisible["top"] = False
            break
    #visibleFromRight
    for a in range(len(trees[y])-1, x, -1):
        if int(trees[y][a]) >= int(trees[y][x]):
            isVisible["right"] = False
            break
    #visibleFromLeft
    for a in range(x):
            if int(trees[y][a]) >= int(trees[y][x]):
                isVisible["left"] = False
                break
    #visibleFromDown
    for a in range(len(trees)-1, y, -1):
        if int(trees[a][x]) >= int(trees[y][x]):
            isVisible["down"] = False
            break
    return isVisible["down"] or isVisible["right"] or isVisible["left"] or isVisible["top"]

def countVisibles():
    global visibleTrees
    trees = openFile()
    for y, treeLine in enumerate(trees):
        for x, tree in enumerate(treeLine):
            visibleTrees += 1 if isVisible(trees, x, y) else 0
    return visibleTrees

def calculateScenic(trees, x, y):
    visibleLeft = visibleTop = visibleRight = visibleDown = 0
    #toLeft
    offSet = 1

    notBlocked = True
    while notBlocked:
        if x-offSet < 0:
            notBlocked = False
            offSet -= 1
        elif trees[y][x-offSet] >= trees[y][x]:
            notBlocked = False
        else:
            offSet += 1
    visibleLeft = offSet
    offSet, notBlocked = 1, True

    #toTop
    notBlocked = True
    while notBlocked:
        if y-offSet < 0:
            notBlocked = False
            offSet -= 1
        elif trees[y-offSet][x] >= trees[y][x]:
            notBlocked = False
        else:
            offSet += 1
    visibleTop = offSet
    offSet, notBlocked = 1, True

    #toRight
    while notBlocked:
        if x+offSet > len(trees[y])-1:
            notBlocked = False
            offSet -= 1
        elif trees[y][x+offSet] >= trees[y][x]:
            notBlocked = False
        else:
            offSet += 1
    visibleRight = offSet
    offSet, notBlocked = 1, True

    #toBottom
    while notBlocked:
        if y+offSet >= len(trees):
            notBlocked = False
            offSet -= 1
        elif trees[y+offSet][x] >= trees[y][x]:
            notBlocked = False
        else:
            offSet += 1
    visibleDown = offSet

    return visibleDown * visibleRight * visibleLeft * visibleTop

def findBestTreeScenic():
    global scenics
    values = []
    trees = openFile()
    for y, treeLine in enumerate(trees):
        for x, tree in enumerate(treeLine):
            if x != 0 and x != len(treeLine)-1 and y != 0 and y != len(trees):
                val = calculateScenic(trees, x, y)
                scenics[(y, x)] = val
                values.append(val)
    return values[0]
    
findBestTreeScenic()
