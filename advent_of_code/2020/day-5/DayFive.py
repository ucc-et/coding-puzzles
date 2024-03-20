class SeatFinder:
    def __init__(self):
        self.seats = []
        self.freeSeats = []
        self.validSeats = []
        self.highestID = 0
        self.ids = []
        self.max = 127
        #self.max = 126
        self.min = 0
        #self.min = 1
        self.row = 0
        self.column = 0
        self.rowMax = 7
        self.rowMin = 0

        with open("five") as file_in:
            for line in file_in:
                line = line.replace("\n", "")
                self.seats.append(line)

        for i in range(len(self.seats)):
            self.scanText(i)
            self.reset()
        print(self.highestID)

        self.sort()
        print(self.ids)
        self.findMissing()
        print(self.validSeats)

    def scanText(self, index):
        for i in self.seats[index][:-3]:
            if i == "F":
                d = (self.max-self.min) / 2
                self.max = self.min + int(d)
                if i == self.seats[index][6:7]:
                    self.row = self.max

            elif i == "B":
                d = (self.max-self.min) / 2 + 1
                self.min = self.min + int(d)
                if i == self.seats[index][6:7]:
                    self.row = self.min

        for i in self.seats[index][7:]:
            if i == "L":
                d = (self.rowMax-self.rowMin) / 2
                self.rowMax = self.rowMin + int(d)
                if i == self.seats[index][-1:]:
                    self.column = self.rowMax
            elif i == "R":
                d = (self.rowMax-self.rowMin) / 2 + 1
                self.rowMin = self.rowMin + int(d)
                if i == self.seats[index][-1:]:
                    self.column = self.rowMin

        z = self.row * 8 + self.column
        self.ids.append(z)
        if self.highestID < z:
            self.highestID = z

    def reset(self):
        self.max = 127
        self.min = 0
        self.rowMax = 7
        self.rowMin = 0

        self.row = 0
        self.column = 0

    def sort(self):
        self.ids.sort()
        self.ids = list(dict.fromkeys(self.ids))

    def findMissing(self):
        for i in range(1024):
            if i not in self.ids:
                self.freeSeats.append(i)

        for i in self.freeSeats:
            if i+1 in self.ids and i-1 in self.ids:
                self.validSeats.append(i)

s = SeatFinder()
