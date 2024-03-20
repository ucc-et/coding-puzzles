
sumOfSquares, sum = 0

for i in range(101):
    sumOfSquares += i**2
    sum += i

print(abs(sumOfSquares-sum**2))