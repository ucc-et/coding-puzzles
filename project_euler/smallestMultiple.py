def smallestMultiple(t,n):
    return ((True if smallestMultiple(t, n-1) else False) if not ( t % n ) else False) if n > 0 else True

i = 20
while not smallestMultiple(i,20):
    i +=20

print(i)