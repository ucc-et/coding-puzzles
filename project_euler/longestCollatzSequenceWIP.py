#WIP
def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n+1

chainOrder = []
maxChain = 0
startNum = 13
startingNumberForMaxChain = startNum
current = 0

while startNum <= 1000000:
    chainOrder = []
    current = startNum
    chainOrder.append(startNum)
    while current != 1:
        current = collatz(current)
        chainOrder.append(current)
    if maxChain <= len(chainOrder):
        maxChain = len(chainOrder)
        startingNumberForMaxChain = startNum
    startNum += 1
    current = startNum
    
print(startingNumberForMaxChain)
print(maxChain)