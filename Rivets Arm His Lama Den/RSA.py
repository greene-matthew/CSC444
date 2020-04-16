import sys
import math

def gcd(a,b):
    if(b == 0):
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return (a*b) / gcd(a,b)

def isPrime(n):
    if (n < 3):
        return True
    if (n % 2 == 0):
        return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if (n % i == 0):
            return False
    return True


def getEs(z):
    es = []
    n = 2
    power = 1
    while((n **power) < z):
       e = n ** power +1
       power +=1
       if (isPrime(e) and gcd(e, z) == 1):
           es.append(e)
    return es

def getD(e, z):
    d = 0
    while (d < z):
        de = d * e
        modz = de % z
        if (modz == 1):
            return d
        d += 1


def factor(n):
    for i in range(3, int(n ** 0.5 + 1),2):
        if(n % i == 0 and isPrime(i) and isPrime(n/i)):
            return [int(i),int(n/i)]

def printTabs():
    print("--")

n = int(sys.stdin.readline())
C = sys.stdin.readline().rstrip('\n').split(',')
PandQ = factor(n)
z = int(lcm(PandQ[0]-1, PandQ[1]-1))
eValues = getEs(z)

print("p={}, q={}".format(PandQ[0],PandQ[1]))
print("n={}".format(n))
print("z={}".format(z))
printTabs()


for e in eValues:
    print("Trying e=" + str(e))
    d = getD(e, z)
    print("d=" + str(d))
    print("Public key: ({}, {})".format(e,n))
    print("Private key: ({}, {})".format(d,n))

    M = ""
    try:
        for c in C:
            m = str(chr(int(c) ** d % n))
            if not (m.isascii()):
                print("ERROR: invalid plaintext.")
                printTabs()
                break
            M += m
    except:
        print("ERROR: invalid plaintext.")
        printTabs()

print(M)






