n = [x for x in range(100, 1000)]
m = [x for x in range(100, 1000)]
currentMaxPalindromeProduct = 0

def checkIfPalindrome(num):
    return str(num) == str(num)[::-1]

for i in n:
    for j in m:
        product = checkIfPalindrome(i*j) 
        if product and i*j > currentMaxPalindromeProduct:
            currentMaxPalindromeProduct = i*j
            

print(currentMaxPalindromeProduct)