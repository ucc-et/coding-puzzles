answer = [[]]
questions = []
index = 0
word = ""
groupsQuestions = 0
askedQ = ""

with open("input") as file:
    for line in file:
        if line == "\n":
            answer.append([])
            index += 1
        for letter in line:
            word += letter
        word = word.replace("\n", "")
        answer[index].append(word)
        word = ""
b = [[i for i in item if i != ''] for item in answer]
groupAnswers = [item for item in b if item != []]
answer = groupAnswers

def fillString(list):
    wholegroup = ""
    for i in list:
        wholegroup += i
    return wholegroup

print(answer)
whole = ""
newques = 0
checked = []
for j in answer:
    whole = fillString(j)
    newques = 0
    checked = []
    for letter in j[0]:
        if letter not in checked and letter != "":
            a = whole.count(letter)
            if a == len(j):
                newques += 1
            whole = whole.replace(letter, "")
            checked.append(letter)
    groupsQuestions += newques

print(groupsQuestions)




