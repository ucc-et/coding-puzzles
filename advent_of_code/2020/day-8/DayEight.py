import copy as cp

list = []
tempList = []
with open("eight") as f:
    for line in f:
        line = line.replace("\n","")
        list.append(line)
        tempList.append(line)

def PartOne():
    alreadyRun = []
    acc = 0
    index = 0
    while True:
        if index in alreadyRun:
            print(acc)
            break
        operate = list[index]
        if operate[0:3] == "acc":
            if operate[4] == "+":
                num = int(operate[5:len(operate)])
                acc += num
            elif operate[4] == "-":
                num = int(operate[5:len(operate)])
                acc = acc - num
            alreadyRun.append(index)
            index += 1
        elif operate[0:3] == "jmp":
            alreadyRun.append(index)
            if operate[4] == "+":
                num = int(operate[5:len(operate)])
                index += num
            elif operate[4] == "-":
                num = int(operate[5:len(operate)])
                index = index - num
        elif operate[0:3] == "nop":
            index += 1

def fillTempList():
    tempList = []
    with open("eight") as f:
        for line in f:
            line = line.replace("\n", "")
            tempList.append(line)

nopNjmp = []
def Part2(index):
    copy = []
    copy = cp.deepcopy(list)

    if "jmp" in copy[index]:
        copy[index] = "nop " + copy[index][4:len(copy[index])]
    elif "nop" in copy[index]:
        copy[index] = "jmp " + copy[index][4:len(copy[index])]

    alreadyRun = []

    acc = 0
    accList = []
    i = 0
    while True:
        if i in alreadyRun:
            return False
        try:
            operate = copy[i]
        except IndexError:
            print(acc)
            print("Raus")
            return True
        if operate[0:3] == "acc":
            if operate[4] == "+":
                num = int(operate[5:len(operate)])
                acc += num
            elif operate[4] == "-":
                num = int(operate[5:len(operate)])
                acc = acc - num
            alreadyRun.append(i)
            accList.append(operate)
            i += 1
        elif operate[0:3] == "jmp":
            alreadyRun.append(i)
            if operate[4] == "+":
                num = int(operate[5:len(operate)])
                i += num
            elif operate[4] == "-":
                num = int(operate[5:len(operate)])
                i = i - num
        elif operate[0:3] == "nop":
            i += 1

def Part2Ctrl():
    for i in range(len(list)):
        if "jmp" in list[i] or "nop" in list[i]:
            nopNjmp.append(i)

    for i in range(len(nopNjmp)):
        if Part2(nopNjmp[i]):
            pass

def checkACC(l):
    a = 0
    for i in l:
        a = a + int(i[4:len(i)])
    print("test " + str(a))
Part2Ctrl()
PartOne()
