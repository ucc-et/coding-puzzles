
class checkPassword:
    def __init__(self):
        self.lines = []
        self.minValue = 0
        self.maxValue = 0
        self.operand = ""
        self.containedOperand = 0
        self.validPassword = 0

        with open("two") as file_in:
            for line in file_in:
                line = line.replace("\n", "")
                self.lines.append(line)
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].split(": ")
        print(self.getValues())

    def getValues(self):
        for i in range(len(self.lines)):
            a = self.lines[i][0]
            if len(a) == 5:
                self.minValue = int(a[0])
                self.maxValue = int(a[2])
                self.operand = a[4]
                self.checkNewValidity(i)
            elif len(a) == 6:
                if a[1] == "-":
                    self.minValue = int(a[0])
                    self.maxValue = int(a[2] + a[3])
                    self.operand = a[5]
                    self.checkNewValidity(i)
                elif a[1] != "-" and a[2] == "":
                    self.minValue = int(a[0] + a[1])
                    self.maxValue = int(a[3])
                    self.operand = a[5]
                    self.checkNewValidity(i)
            elif len(a) == 7:
                self.minValue = int(a[0] + a[1])
                self.maxValue = int(a[3] + a[4])
                self.operand = a[6]
                self.checkNewValidity(i)

    def checkOldValidity(self, index):
        password = self.lines[index][1]
        for letter in password:
            if letter == self.operand:
                self.containedOperand = self.containedOperand + 1

        if self.containedOperand >= self.minValue and self.containedOperand <= self.maxValue:
            self.validPassword = self.validPassword + 1

        self.resetValues()

    def resetValues(self):
        self.minValue = 0
        self.maxValue = 0
        self.operand = ""
        self.containedOperand = 0

    def checkNewValidity(self, index):
        password = self.lines[index][1]
        if self.operand == password[self.minValue-1] and self.operand == password[self.maxValue-1]:
            return
        elif self.operand == password[self.minValue-1] or self.operand == password[self.maxValue-1]:
            self.validPassword = self.validPassword + 1
        else:
            return

challenge = checkPassword()