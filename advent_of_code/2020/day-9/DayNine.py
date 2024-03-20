
numbers = []
with open("nine") as f:
    for num in f:
        num = num.replace("\n", "")
        numbers.append(int(num))

def findSum(index):
    goal = numbers[index]
    for i in range(index-25, index):
        for j in range(index-25, index):
            if numbers[i] != numbers[j] and numbers[i] + numbers[j] == goal:
                return True
    #print(goal)
    return False
def partOne():
    while True:
        for i in range(len(numbers)):
            if i < 25:
                pass
            else:
                a = findSum(i)
                if a == True:
                    pass
                elif a == False:
                    print(numbers[i])
                    return i

def partTwo(goal):

    idx = 0
    start = 0
    ende = 0
    while True:
        reichweite = numbers[start:ende]
        if sum(reichweite) == goal:
            return print(max(reichweite)+ min(reichweite))
        elif sum(reichweite) > goal:
            start += 1
        elif sum(reichweite) < goal:
            ende += 1

b = partOne()
a = numbers[b]
print(a)
print(partTwo(a))