t, n, l = 10001, 2, [2]

while len(l)<t:
    n += 1
    for i in l:
        if n % i == 0:
           break
    else:
        l.append(n)

print(l[-1])