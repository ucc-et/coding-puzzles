
def primeFactor(n):
    lastPrimeFactor = 2 if n % 2 == 0 else 1

    while n % 2==0:
        n = n / 2

    currentFactor, maxFactor = 3, n**0.5

    while n > 1 and currentFactor <= maxFactor:
        if n % currentFactor == 0:
            n = n / currentFactor
            lastPrimeFactor = currentFactor
            while n % currentFactor==0:
                n = n / currentFactor
            maxFactor = n
        currentFactor += 2

    return lastPrimeFactor if n == 1 else n

primeFactor(600851475143)