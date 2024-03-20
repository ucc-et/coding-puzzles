
def specialPythagoreanTriplet():
    for c in range(400, 500): # put 1000 in range
        for b in range(300, c): # put c in range
            for a in range(b):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    print(a, b, c)
                    return a*b*c

print(specialPythagoreanTriplet())