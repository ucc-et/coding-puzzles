from math import floor
import time

startTime = time.time()

def triangularSet(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a

def getDivisorCount(n):
    divisorCount = 0
    for i in range(1, floor(n**0.5)+1):
        divisorCount += 0 if n % i != 0 else 2 if i**2 != n else 1 
    return divisorCount

i = 1
tri = 1
while getDivisorCount(tri) <= 500:
    tri = triangularSet(i)
    i += 1
print(tri)
#print(i) 12376

print(time.time()-startTime)
