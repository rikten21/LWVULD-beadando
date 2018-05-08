# The prime factors of 13195 are 5, 7, 13 and 29.
# The prime factors of 600851475143 are 71, 839,  1471 and 6857.

def biggestPrimeFactors(n):
    if n <= 1: #1 vagy annál kisebb egészekre nem értelmez a függvény
        return None
    while n%2 == 0: #leoszt 2-vel, amíg lehet
        n = n/2
    if n == 1: #ha 2-es hatvány volt a szám
        return 2
    div = 3 #ezzel osztunk végig a számon
    while n != 1:
        while n%div == 0:
            n = n/div
        div += 2 #elég a páratlan számokon végigmenni
    return div-2

#main:
print(biggestPrimeFactors(600851475143), "is the biggest prime factor of 600851475143.")
