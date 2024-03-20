dir = [[], []]
i = 0
with open("twelve") as f:
    for line in f:
        for a in line:
            a = a.replace("\n", "")
            dir[i].append(a[0])
            dir[i].append(a[1:])
        i += 1
        dir.append([])
print(dir)