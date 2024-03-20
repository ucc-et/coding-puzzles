

# zeroes=[0,0,0,0,0,0,0,0,0,0,0,0]
# ones=[0,0,0,0,0,0,0,0,0,0,0,0]

# for binary in mainInput:
#     for i in range(len(binary)):
#         if binary[i] == "1":
#             ones[i] += 1
#         else:
#             zeroes[i] += 1

# gamma = ""
# epsilon = ""

# for i in range(len(ones)):
#     if zeroes[i] > ones[i]:
#         gamma += "0"
#         epsilon += "1"
#     else:
#         gamma += "1"
#         epsilon += "0"

# gammaInt = int(gamma, 2)
# epsilonInt = int(epsilon, 2)

# print("Part 1: ", gammaInt * epsilonInt)

# find oxygen generator rating
# most common value in the current bit pos. and keep only numbers with that bit in that position. if 0 and 1 are equal, take 1 as most common. 

# find co2 scrubber 
# least common genau wie das andere nur 0 nehmen falls 1 und 0 gleich sind.


mainInput = []

with open('input.txt') as file:
    inputList = file.readlines()
    for line in range(len(inputList)):
        inputList[line] = inputList[line].replace('\n', '')
    mainInput = inputList

class PartTwo():
    def __init__(self, mainInput):
        self.zero = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.one = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.oxygen = ""
        self.CO2 = ""
        self.oxygenSol = ""
        self.CO2Solution = ""
        self.mainInput = mainInput

        self.findCommons()
        self.findOxygenCount()
        self.findCO2Count()
        
        a = int(self.oxygenSol,2)
        b = int(self.CO2Solution, 2)
        print("Part 2: ", a * b)

    def findCommons(self):
        for binary in self.mainInput:
            for i in range(len(binary)):
                if binary[i] == "1":
                    self.one[i] += 1
                else:
                    self.zero[i] += 1
    
    def findOxygenCount(self):
        list = self.mainInput
        for index in range( len(self.zero)):
            if self.zero[index] > self.one[index]:
                self.oxygen += "0"
                list = self.deleteOne(list, index)
                if len(list) == 1:
                    break
            elif self.zero[index] <= self.one[index]:
                self.oxygen += "1"
                list = self.deleteZero(list, index)
                if len(list) == 1:
                    break

        self.oxygenSol = list[0]
   
    def findCO2Count(self):
        list = self.mainInput
        for index in range( len(self.zero)):
            if self.zero[index] > self.one[index]:
                self.CO2 += "1"
                list = self.deleteZero(list, index)
                if len(list) == 1:
                    break
            elif self.zero[index] <= self.one[index]:
                self.CO2 += "0"
                list = self.deleteOne(list, index)
                if len(list) == 1:
                    break
        self.CO2Solution = list[0]
       
    def deleteZero(self, list, index):
        newList = []
        for i in range(len(list)):
            if list[i][index] == "1":
                newList.append(list[i])
        return newList
   
    def deleteOne(self, list, index):
        newList = []
        for i in range(len(list)):
            if list[i][index] == "0":
                newList.append(list[i])
        return newList

a = PartTwo(mainInput)
#4432698
