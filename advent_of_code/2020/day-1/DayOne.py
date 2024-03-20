class AdventOfCodeDayOne:
    def __init__(self):
        self.list = []
        with open("one") as One:
            for line in One:
                line = line.replace("\n", "")
                self.list.append(int(line))
        print(self.get2020With2Num())
        print(self.get2020with3Num())

    def get2020With2Num(self):
        for i in self.list:
            for j in self.list:
                if i + j == 2020:
                    return i*j

    def get2020with3Num(self):
        for i in self.list:
            for j in self.list:
                for k in self.list:
                    if i + j + k == 2020:
                        return i * j * k
a = AdventOfCodeDayOne()