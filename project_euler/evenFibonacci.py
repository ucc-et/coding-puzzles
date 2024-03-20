evenFibonacciSet = []

previousSummand = 1
currentSummand = 1
currentFibo = 0

while currentFibo <= 4000000:
    currentFibo = previousSummand + currentSummand
    previousSummand = currentSummand
    currentSummand = currentFibo
    if currentFibo % 2 == 0:
        evenFibonacciSet.append(currentFibo)

print(sum(evenFibonacciSet))
    