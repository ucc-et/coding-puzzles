basePower = 2**1000
powerAsString = str(basePower)
sum = 0

for letter in powerAsString:
    num = int(letter)
    sum += int(num)

print(sum)
