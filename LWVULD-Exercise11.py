def isPalindromicNum(n): #egy adott szám palindrom-e
    n = str(n)
    nReversed = n[::-1] #szeleteléssel, visszafelé lépkedve fordítja meg a sztinget
    if n == nReversed:
        return True
    return False


def biggestPalindromeFromTwo3digitnums():
    for i in range(1000,100,-1): #a legnagyobb 3 jegyű
        for j in range(1000,100,-1): #a második legnagyobb 3 jegyű
            if isPalindromicNum(i*j): #amiknek a szorzata
                return i, j, i*j

#main
# print(biggestPalindromeFromTwo3digitnums())
i, j, pal = biggestPalindromeFromTwo3digitnums()
print("The biggest palindrome from the product of two 3-digit numbers is {} from {} x {}".format(pal,i,j))

##########################
#extra:
def biggestPalindromeFromTwo_n_digitnums(n): #n-jegyű két szám szorzatából kapott legnagyobb palindrom
    fh = 10 ** n
    ah = 10 ** (n-1)
    for i in range(fh, ah, -1):
        for j in range(fh, ah, -1):
            if isPalindromicNum(i*j):
                return i, j, i*j

# print(biggestPalindromeFromTwo_n_digitnums(3))
