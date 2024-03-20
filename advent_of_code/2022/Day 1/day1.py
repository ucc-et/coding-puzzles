with open("d.txt") as f:
    cals = f.readlines()

elfs = []
sum = 0
for cal in cals:
    cal = cal.strip()
    if not cal == "":
        sum += int(cal.strip())
    else:
        elfs.append(int(sum))
        sum = 0

elfs.sort(reverse=True)
print(elfs[0] + elfs[1] + elfs[2])
