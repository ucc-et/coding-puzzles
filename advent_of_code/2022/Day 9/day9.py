import math

class Knot:
    x = y = 0
    def __init__(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
        
head = Knot(0)
objects = [Knot(1),Knot(2),Knot(3),Knot(4),Knot(5),Knot(6),Knot(7),Knot(8),Knot(9)]
visited = [(0, 0)]

def moveDown(n):
    if n == 0:
        return
    head.y -= 1
    for i in range(len(objects)):
        if i == 0:
            if hasToMove(head, objects[i]):
                followHead(head, objects[i])
        else:
            if hasToMove(objects[i-1], objects[i]):
                followHead(objects[i-1], objects[i])
    moveDown(n-1)

def moveUp(n):
    if n == 0:
        return
    head.y += 1
    for i in range(len(objects)):
        if i == 0:
            if hasToMove(head, objects[i]):
                followHead(head, objects[i])
        else:
            if hasToMove(objects[i-1], objects[i]):
                followHead(objects[i-1], objects[i])
    moveUp(n-1)

def moveRight(n):
    if n == 0:
        return
    head.x += 1
    for i in range(len(objects)):
        if i == 0:
            if hasToMove(head, objects[i]):
                followHead(head, objects[i])
        else:
            if hasToMove(objects[i-1], objects[i]):
                followHead(objects[i-1], objects[i])
    moveRight(n-1)

def moveLeft(n):
    if n == 0:
        return
    head.x -= 1
    for i in range(len(objects)):
        if i == 0:
            if hasToMove(head, objects[i]):
                followHead(head, objects[i])
        else:
            if hasToMove(objects[i-1], objects[i]):
                followHead(objects[i-1], objects[i])
    moveLeft(n-1)  

directionParse = {
    "D": moveDown,
    "U": moveUp,
    "R": moveRight,
    "L": moveLeft
}

def openFile(path="day_9_input.txt"):
    moves = []
    with open(path) as f:
        for line in f.readlines():
            moves.append(line.strip().split())
    return moves

def followHead(headObject, tailObject):
    if headObject.x > tailObject.x and headObject.y > tailObject.y:
        tailObject.x += 1
        tailObject.y += 1
    elif headObject.x > tailObject.x and headObject.y < tailObject.y:
        tailObject.x += 1
        tailObject.y -= 1
    elif headObject.x < tailObject.x and headObject.y > tailObject.y:
        tailObject.x -= 1
        tailObject.y += 1
    elif headObject.x < tailObject.x and headObject.y < tailObject.y:
        tailObject.x -= 1
        tailObject.y -= 1
    else:
        if tailObject.x == headObject.x:
            tailObject.y += 1 if tailObject.y < headObject.y else -1
        else:
            tailObject.x += 1 if tailObject.x < headObject.x else -1
    if (not (tailObject.x, tailObject.y) in visited) and (tailObject.getId() == 9):
        visited.append((tailObject.x, tailObject.y))

def hasToMove(headObject, tailObject):
    if (abs(headObject.x-tailObject.x) <= 1) and (abs(headObject.y-tailObject.y) <= 1):
        return False
    return True

def startTrace():
    moves = openFile()
    for move in moves:
        directionParse[move[0]](int(move[1]))
    print(len(visited))

startTrace()
