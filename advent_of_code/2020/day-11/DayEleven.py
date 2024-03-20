
class Elf:
    def __init__(self):
        self.seats = [[]]
        self.madeChanges = 0
        self.occupied = 0

        self.i = 0
        with open("eleven") as f:
            for line in f:
                line = line.replace("\n", "")
                for a in line:
                    self.seats[self.i].append(a)
                self.seats.append([])
                self.i += 1

        # print(len(self.seats))
        # print(len(self.seats)-1)
        # a = len(self.seats)-1
        # print(self.seats[a])
        # print(len(self.seats[0]))
        print(self.seats[0])
        # print(len(self.seats[2]))

    def checkTLC(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row+1][col] == "L" and self.seats[row][col+1] == "L" and self.seats[row+1][col+1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1

    def checkL(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row-1][col] == "L":
                if self.seats[row][col+1] == "L":
                    if self.seats[row-1][col+1] == "L":
                        if self.seats[row+1][col+1] == "L":
                            if self.seats[row+1][col] == "L":
                                self.seats[row][col] = "#"
                                self.madeChanges += 1
        elif self.seats[row][col] == "#":
            if self.seats[row-1][col] == "#":
                self.occupied += 1
            if self.seats[row+1][col] == "#":
                self.occupied += 1
            if self.seats[row][col+1] == "#":
                self.occupied += 1
            if self.seats[row+1][col+1] == "#":
                self.occupied += 1
            if self.seats[row-1][col+1] == "#":
                self.occupied += 1
            if self.occupied >= 4:
                self.seats[row][col] = "L"
                self.madeChanges += 1
            self.occupied = 0

    def checkBLC(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row-1][col] == "L" and self.seats[row][col+1] == "L" and self.seats[row - 1][col + 1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1

    def checkTRC(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row + 1][col] == "L" and self.seats[row][col - 1] == "L" and self.seats[row + 1][col - 1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1

    def checkR(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row - 1][col] == "L" and self.seats[row][col - 1] == "L" and self.seats[row - 1][col - 1] == "L" and self.seats[row + 1][col - 1] == "L" and self.seats[row + 1][col] == "L":
                self.seats[row][col] == "#"
                self.madeChanges += 1
        elif self.seats[row][col] == "#":
            if self.seats[row - 1][col] == "#":
                self.occupied += 1
            if self.seats[row + 1][col] == "#":
                self.occupied += 1
            if self.seats[row][col - 1] == "#":
                self.occupied += 1
            if self.seats[row + 1][col - 1] == "#":
                self.occupied += 1
            if self.seats[row - 1][col - 1] == "#":
                self.occupied += 1
        if self.occupied >= 4:
            self.seats[row][col] = "L"
            self.madeChanges += 1
        self.occupied = 0

    def checkBRC(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row - 1][col] == "L" and self.seats[row][col - 1] == "L" and self.seats[row - 1][col - 1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1

    def checkM(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row+1][col] == "L" and self.seats[row][col+1] == "L" and self.seats[row][col-1] == "L" and self.seats[row+1][col+1] == "L" and self.seats[row+1][col-1] == "L" and self.seats[row-1][col+1] == "L" and self.seats[row-1][col-1] == "L" and self.seats[row-1][col] == "L":
                self.madeChanges += 1
                self.seats[row][col] == "#"
        if self.seats[row][col] == "#":
            if self.seats[row+1][col] == "#":
                self.occupied += 1
            if self.seats[row-1][col] == "#":
                self.occupied += 1
            if self.seats[row-1][col-1] == "#":
                self.occupied += 1
            if self.seats[row-1][col+1] == "#":
                self.occupied += 1
            if self.seats[row+1][col-1] == "#":
                self.occupied += 1
            if self.seats[row+1][col+1] == "#":
                self.occupied += 1
            if self.seats[row][col+1] == "#":
                self.occupied += 1
            if self.seats[row][col-1] == "#":
                self.occupied += 1
            if self.occupied >= 4:
                self.seats[row][col] = "L"
                self.madeChanges += 1
            self.occupied = 0

    def checkBM(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row][col-1] == "L" and self.seats[row][col+1] == "L" and self.seats[row-1][col] == "L" and self.seats[row-1][col-1] == "L" and self.seats[row-1][col+1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1
        elif self.seats[row][col] == "#":
            if self.seats[row][col-1] == "#":
                self.occupied += 1
            if self.seats[row][col+1] == "#":
                self.occupied += 1
            if self.seats[row-1][col] == "#":
                self.occupied += 1
            if self.seats[row-1][col-1] == "#":
                self.occupied += 1
            if self.seats[row-1][col+1] == "#":
                self.occupied += 1
            if self.occupied >= 4:
                self.seats[row][col] = "L"
                self.madeChanges += 1
            self.occupied = 0

    def checkTM(self, row, col):
        if self.seats[row][col] == "L":
            if self.seats[row][col - 1] == "L" and self.seats[row][col + 1] == "L" and self.seats[row + 1][col] == "L" and self.seats[row + 1][col - 1] == "L" and self.seats[row + 1][col + 1] == "L":
                self.seats[row][col] = "#"
                self.madeChanges += 1
        elif self.seats[row][col] == "#":
            if self.seats[row][col - 1] == "#":
                self.occupied += 1
            if self.seats[row][col + 1] == "#":
                self.occupied += 1
            if self.seats[row + 1][col] == "#":
                self.occupied += 1
            if self.seats[row + 1][col - 1] == "#":
                self.occupied += 1
            if self.seats[row + 1][col + 1] == "#":
                self.occupied += 1
            if self.occupied >= 4:
                self.seats[row][col] = "L"
                self.madeChanges += 1
            self.occupied = 0

    def checkSeatConfig(self):

        while True:
            print(self.seats)
            self.madeChanges = 0
            self.occupied = 0
            for i in range(len(self.seats)):
                row = i
                for j in range(len(self.seats[i])):
                    col = j
                    if col == 0:
                        if row == 0:
                            self.checkTLC(row, col)
                        elif row == 96:  #row == len(self.seats)-2:
                            self.checkBLC(row, col)
                        elif row > 0 and row < 96: #row != 0 and row != len(self.seats)-1:
                            self.checkL(row, col)
                    elif col == 96: #col == len(self.seats[i])-1:
                        if row == 0:
                            self.checkTRC(row, col)
                        elif row == 96:#row == len(self.seats)-1:
                            self.checkBRC(row, col)
                        elif row > 0 and row < 96:#row != 0 and row != len(self.seats)-1:
                            self.checkR(row, col)
                    elif col > 0 and col < 96:
                        if row == 0:
                            self.checkTM(row, col)
                        elif row == 96:#row == len(self.seats)-1:
                            self.checkBM(row, col)
                        elif row > 0 and row < 96: #row != 0 and row != len(self.seats)-1:
                            self.checkM(row, col)
                    else:
                        print("-----------------------------")
                        print("Fehlende Reihe: " + str(row))
                        print("Fehlende Spalte: " +str(col))
                        print("-----------------------------")
            #print(self.madeChanges)
            a = 0
            for i in range(len(self.seats)):
                for j in range(len(self.seats[i])):
                    if self.seats[i][j] == "#":
                        a += 1
            print(a)

            if self.madeChanges == 0:
                print(self.seats.count("#"))

                exit()
            else:
                pass

a = Elf()
a.checkSeatConfig()
