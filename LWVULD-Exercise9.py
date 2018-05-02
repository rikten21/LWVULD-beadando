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
            if n%div == 0:
                n = n/div
    return div

#main:
# print(biggestPrimeFactors2(13195))
print(biggestPrimeFactors2(600851475143))