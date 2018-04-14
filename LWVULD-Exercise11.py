def numReverse(n):
    r = 0
    p = len(str(n))-1
    while n!=0:
        r += n%10 * 10**p
        n = n//10
        p -= 1
    return r

def isPalindromicNum(n):
    l = int(len(str(n))) #a szám hossza
    if l%2 == 0:
        h = int(l/2) #a szám hosszának a fele
        p = 0  # helyiérték számolása
        n1 = n//10**h
        n2 = numReverse(n%10**h)
        if n1 == n2:
            return True
    return False

def biggest3digitPalindrome():
    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            if isPalindromicNum(i*j):
                return i, j, i*j

print(biggest3digitPalindrome())

# print(isPalindromicNum(564465))
# print(isPalindromicNum(456456))
# print(isPalindromicNum(12345))
