def generatePrimeList(n):
    sieve = [True] * (n + 1)
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = False
    return primes

print(sum(generatePrimeList(2000000)))