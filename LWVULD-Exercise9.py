import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# The prime factors of 600851475143 are 71, 839,  1471 and 6857.

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def biggestPrimeFactors2(n): 
    div = 1
    while n != 1:
        div += 1
        if isPrime(div):
            while n%div == 0:
                n = n/div
    return div

def biggestPrimeFactors3(n): #Még gyorsabb, mint a 2-es, mert a 2-t, mint egyetlen páros prímet külön kezeli, így utána csak a páratlanokat vizsgálja.
    if n <= 1: #Így kezeli azt is, ha 1-et, 0-át vagy negatív egészszámot adunk a függvénynek.
        return None
    while n%2 == 0:
        n = n/2
    if n == 1:
        return 2
    div = 3
    while n != 1:
        if isPrime(div):
            while n%div == 0:
                n = n/div
        div += 2
    return div-2

#main:
# print(biggestPrimeFactors2(13195))
# print(biggestPrimeFactors2(600851475143))

# print(biggestPrimeFactors3(13195))
print(biggestPrimeFactors3(600851475143))
