# A Rock, B paper, C Scissor
# X Rock, Y paper, Z Scissor
A, B, C = 1, 2, 3
X, Y, C = A, B, C

def getValue(x, y):
    attack = 1 if x == "A" else 2 if x == "B" else 3
    counter = 1 if y == "X" else 2 if y == "Y" else 3
    return (attack, counter)

def getScore(x, y):
    if hasWon(x,y):
        return y + 6
    else:
        if x == y:
            return y + 3
        return y

def hasWon(x, y):
    if x == A and y == B:
        return True
    elif x == B and y == C:
        return True
    elif x == C and y == A:
        return True
    return False

def startStrategy():
    strategy = []
    points = 0
    with open("day2_input.txt") as file:
        lines = file.readlines()
        for line in lines:
            strategy.append(line.split())
    
    for move in strategy:
        value = getValue(move[0], move[1])
        points += getScore(value[0], value[1])
    print(points)

def chooseTactic(x, y):
    if y == X: # lose
        yMove = C if x == A else A if x == B else B
    elif y == Y: # draw
        yMove = x
    else: # win
        yMove = A if x == C else B if x == A else C
    
    return getScore(x, yMove)

def startCorrectStrategy():
    strategy = []
    points = 0
    with open("day2_input.txt") as file:
        lines = file.readlines()
        for line in lines:
            strategy.append(line.split())
    
    for move in strategy:
        val = getValue(move[0], move[1])
        points += chooseTactic(val[0], val[1])
    print(points)
startCorrectStrategy()
