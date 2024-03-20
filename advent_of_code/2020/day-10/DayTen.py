list = [0]

with open("ten") as f:
    for line in f:
        line = line.replace("\n", "")
        list.append(int(line))

list = sorted(list)
#1856

def findNext(goal):
    for i in range(len(list)):
        if list[i] == goal:
            return i

def one():
    one = 0
    three = 0
    i = 0
    while True:
        if i + 1 == len(list):
            break
        if list[i+1] - list[i] == 1:
            one += 1
            i += 1
        elif list[i + 1] - list[i] == 3:
            three += 1
            i += 1
    print(one*three)

pos = [1] + [0] * list[-1]
for i in list[1:]:
    pos[i] = pos[i-1] + pos[i-2] + pos[i-3]
print(pos[-1])


