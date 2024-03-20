class checkPassport:
    def __init__(self):
        self.l = [[]]
        self.index = 0
        self.valids = 0
        self.validPW = 0

        with open("input") as file_in:
            for line in file_in:
                if line == "\n":
                    self.l.append([])
                    self.index += 1
                if " " in line:
                    word = ""

                    for letter in line:
                        if letter == " ":
                            word = word.replace("\n", "")
                            self.l[self.index].append(word)
                            word = ""
                        else:
                            word += letter
                    word = word.replace("\n", "")
                    self.l[self.index].append(word)
                else:
                    line = line.replace("\n", "")
                    self.l[self.index].append(line)

        self.eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        self.forbiddenLetter = ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.checkPass()
        print(self.l)

    def checkPass(self):
        for i in range(len(self.l)):
            for j in range(len(self.l[i])):
                a = self.l[i][j]
                if "hgt" in a:
                    if self.checkHeight(a):
                        self.valids += 1
                if "iyr" in a:
                    if self.checkIssueYear(a):
                        self.valids += 1
                if "hcl" in a:
                    if self.checkHair(a):
                        self.valids += 1
                        print(a)
                if "ecl" in a:
                    if self.checkEye(a):
                        self.valids += 1
                        print(a)
                if "byr" in a:
                    if self.checkBirthYear(a):
                        self.valids += 1
                        print(a)
                if "eyr" in a:
                    if self.checkExpirationYear(a):
                        self.valids += 1
                        print(a)
                if "pid" in a:
                    if self.checkPassID(a):
                        self.valids += 1
                        print(a)
            if self.valids == 7:
                self.validPW += 1
            self.valids = 0

    def checkHeight(self, text):
        a = text[4:len(text) - 2]

        if text[-2:] == "cm":
            if int(a) >= 150 and int(a) <= 193:
                return True
        elif text[-2:] == "in":
            if int(a) >= 59 and int(a) <= 76:
                return True

    def checkBirthYear(self, text):

        if len(text[4:len(text)]) == 4:
            if int(text[4:len(text)]) >= 1920 and int(text[4:len(text)]) <= 2002:
                return True

    def checkIssueYear(self, text):

        if len(text[4:len(text)]) == 4:
            if int(text[4:len(text)]) >= 2010 and int(text[4:len(text)]) <= 2020:
                return True

    def checkExpirationYear(self, text):
        if len(text[4:len(text)]) == 4:
            if int(text[4:len(text)]) >= 2020 and int(text[4:len(text)]) <= 2030:
                return True

    def checkHair(self, text):
        x = text[5:len(text)]

        if text[4] == "#" and len(x) == 6:
            con = 0
            for i in self.forbiddenLetter:
                if i not in x:
                    con += 1
            if len(text) == 11 and con == 20:
                return True

    def checkEye(self, text):
        if text[4:len(text)] in self.eyeColors:
            return True

    def checkPassID(self, text):

        if len(text[4:len(text)]) == 9:
            return True

a = checkPassport()



