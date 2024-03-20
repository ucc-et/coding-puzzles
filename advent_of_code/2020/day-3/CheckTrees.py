class tree:
    def __init__(self):
        self.lines = [[]]
        self.index = 0
        self.trees = 0
        self.x = 0
        self.y = 0

        with open("inputDay3.txt") as self.file_in:
            for self.line in self.file_in:
                self.line = self.line.replace("\n", "")
                for self.i in range(len(self.line)):
                    self.lines[self.index].append(self.line[self.i])
                self.lines.append([])
                self.index += 1

        self.scanPath(3, 1)
        print(self.trees)
        #print(len(self.lines))

    def showMap(self):
        for i in range(len(self.lines)):
            print(str(i) + "  " + str(self.lines[i]))

    def scanPath(self, right, down):
        if self.lines[0][0] == "#":
            self.trees += 1
        while True:
            # 79, 216, 91, 96, 45
            a = self.TwoDownOneRight()
            if down == 2:
                if self.y == 324:
                    break
                else:
                    self.y += 2
            if right == 3:
                pass
            if a == False:
                break
            if a == "#":
                self.trees += 1
                #self.lines[self.y][self.x] += "|"
                #print(self.trees)
                #print(str(self.x) + " " + str(self.y))
    def checkX(self, base, mxO=None, mxTw= None, mxTh= None, mxFr= None, mxSi= None):
        if mxO == 30:
            
            self.x = 2
        elif mxTw == 29:
            self.x = 1
        elif mxTh == 28:
            self.x = 0
    def OneDownThreeRight(self):

        if self.y == len(self.lines)-1:
            return False
        else:
            self.y += 1
        if self.x == 30 or self.x == 29 or self.x == 28:
            if self.x == 30:
                self.x = 2
            elif self.x == 29:
                self.x = 1
            elif self.x == 28:
                self.x = 0
        else:
            self.x += 3
        try:
            return self.lines[self.y][self.x]
        except IndexError:
            print("Done")

    def OneDownOneRight(self):
        stay = False
        if self.y == len(self.lines)-1:
            return False
        else:
            self.y += 1
        if self.x == 30:
            stay = True

        if stay:
            stay = False
            self.x = 0
        else:
            self.x += 1
        try:
            return self.lines[self.y][self.x]
        except IndexError:
            print("Done")

    def OneDownFiveRight(self):
        stay = False
        if self.y == len(self.lines)-1:
            return False
        else:
            self.y += 1

        if self.x == 30 or self.x == 29 or self.x == 28 or self.x == 27 or self.x == 26:

            if self.x == 30:
                self.x = 4
            elif self.x == 29:
                self.x = 3
            elif self.x == 28:
                self.x = 2
            elif self.x == 27:
                self.x = 1
            elif self.x == 26:
                self.x = 0
        else:
            self.x += 5
        try:
            return self.lines[self.y][self.x]
        except IndexError:
            print("Done")

    def OneDownSevenRight(self):
        if self.y == len(self.lines)-1:
            return False
        else:
            self.y += 1

        if self.x == 30 or self.x == 29 or self.x == 28 or self.x == 27 or self.x == 26 or self.x == 25 or self.x == 24:
            if self.x == 30:
                self.x = 6
            elif self.x == 29:
                self.x = 5
            elif self.x == 28:
                self.x = 4
            elif self.x == 27:
                self.x = 3
            elif self.x == 26:
                self.x = 2
            elif self.x == 25:
                self.x = 1
            elif self.x == 24:
                self.x = 0
        else:
            self.x += 7
        try:
            return self.lines[self.y][self.x]
        except IndexError:
            print("Done")

    def TwoDownOneRight(self):

        if self.y == 324:
            return False
        else:
            self.y += 2

        if self.x == len(self.lines[0])-1:
            self.x = 0
        else:
            self.x += 1
        try:
            return self.lines[self.y][self.x]
        except IndexError:
            print("Done")
chal = tree()

#216, 79, 91, 96, 46