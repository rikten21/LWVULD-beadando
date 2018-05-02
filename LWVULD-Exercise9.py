import math

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primeFactors(n):
    primefactors = []
    for i in range(2,n+1):
        if isPrime(i):
            if n%i == 0:
                primefactors.append(i)
    return primefactors

def biggestNumber(numberlist):
    max = -math.inf
    for i in numberlist:
        if i > max:
            max = i
    return max

#main:
#print(biggestNumber(primeFactors(600851475143)))
#print(biggestNumber(primeFactors(13195)))

def biggestPrimefactor(n):
    for i in range(n,0,-1):
        if n%i == 0:
            if isPrime(i):
                return i

#print(biggestPrimefactor(600851475143))
