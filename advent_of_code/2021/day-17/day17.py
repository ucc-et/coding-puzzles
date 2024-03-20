
from fractions import Fraction
from math import isqrt
x_min = 14
x_max = 50
y_min = -267
y_max = -225

def factors(n):
    """Naive, slow. Fine for our purposes. Positive factors only.
    """
    for d in range(1, abs(n)+1):
        if abs(n) % d == 0:
            yield d
def possible_vy_n(y):
    """Find all combinations of initial vertical velocity (vy)
    and number of steps (n) that hit the given y value.
    """
    for d in factors(y):
        if (y//d + 2*d - 1) % 2 == 0:
            yield (y//d + 2*d - 1) // 2, 2*d
        if d % 2 == 1:
            yield (y//d + d//2), d

def possible_vx(x, n):
    """Find all possible values for initial horizontal velocity (vx)
    that hit the given x value after n steps. (There will be either
    0 or 1 such values.)
	"""
    # First see if there is a vx that works with vx > n
    vx = Fraction(x, n) + Fraction(n-1, 2)
    if vx.denominator == 1 and vx.numerator > n:
        yield vx.numerator
    
    # If x is the r'th triangular number, and n ≥ r, we can have vx = r
    discriminant = 8*x + 1
    root = isqrt(discriminant)
    if discriminant == root**2 and root % 2 == 1:
        r = (root - 1) // 2
        if n >= r: yield r

# Part 1
print(max((
    (vy * (vy + 1)) // 2
    for x in range(x_min, x_max + 1)
    for y in range(y_min, y_max + 1)
    for (vy, n) in possible_vy_n(y)
    for _ in possible_vx(x, n)
)))

# Part 2
print(len({
    (vx, vy)
    for x in range(x_min, x_max + 1)
    for y in range(y_min, y_max + 1)
    for (vy, n) in possible_vy_n(y)
    for vx in possible_vx(x, n)
}))
