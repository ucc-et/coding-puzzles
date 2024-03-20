mapper = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand",
    100: "hundred"

}

letterCount = 0
tests = [789, 234, 354, 485, 500, 897]

for i in range(1, 1000):
    prev = letterCount
    if len(str(i)) == 1:
        oneDigit = mapper.get(i)
        letterCount += len(oneDigit)
    elif len(str(i)) == 2:
        if(str(i)[0] == "1"):
            letterCount += len(mapper.get(i))
        else:
            tenth = mapper.get(i - int(str(i)[1]))
            oneDigit = mapper.get(int(str(i)[1]))
            letterCount += len(tenth) + len(oneDigit)
    elif len(str(i)) == 3:
        if(str(i)[1] == "1"):
            inter = int(str(i)[1:])
            hundreds = mapper.get((i - inter)/100)
            tens = mapper.get(int(str(i)[1:]))
            letterCount += len(hundreds) + len(mapper.get(100)) + len("and") + len(tens)
        else:
            if(i==698):
                print()
            a = i - int(str(i)[1:])
            hundreds = i - int(str(i)[1:])
            tens = 10 * int(str(i)[1])
            tens = mapper.get(tens)
            ones = mapper.get(int(str(i)[2]))
            hundreds = mapper.get(hundreds / 100)
            if tens == "" and ones == "":
                letterCount += len(hundreds) + len(mapper.get(100))
            else:
                letterCount += len(hundreds) + len(mapper.get(100))+ len("and") + len(tens) + len(ones)
    print(str(i) + ": " + str(letterCount - prev))
letterCount += len(mapper.get(1000))
print(letterCount)