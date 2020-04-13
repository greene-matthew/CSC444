import re
import sys

dictionary = "dictionary.txt"
threshold = 0.75
#alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
alphabet = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"


d = open(dictionary, "r")
dictionary = d.read().rstrip("\n").split("\n")
d.close()

encryptedString = sys.stdin.read().rstrip('\n')
encryptedStringTest = encryptedString.split('\n')[:10]


lenOfEncyption= 0
for line in encryptedStringTest:
    for letter in line:
        if letter in alphabet:
            lenOfEncyption += 1




def getKey(word):
    key = ""
    while len(key) < lenOfEncyption:
        key += word
    if (len(key) != lenOfEncyption):
        key = key[:lenOfEncyption]

    return key


# This method checks the decrypted string agaisnt the dictionary. If 75% of the words in the string
# are in the dictonary we return the string
def checkIfValid(decryptedString):
    words = len(decryptedString)
    validWords = 0

    for x in decryptedString:
        x = re.sub(r'[^A-Za-z]', '', x)
        if x.lower() in dictionary:
            validWords += 1
    if ((validWords / words) >= threshold):

        return True
    else:
        return False


def decrypt(key, encryptedText):
    string = ""
    indexOfLetter = 0

    for line in encryptedText:
        for letter in line:
            if letter not in alphabet:
                string += letter
            else:
                try:
                    keyLetter = key[indexOfLetter]
                except:
                    continue
                indexOfLetter +=1
                sum = alphabet.index(letter) - alphabet.index(keyLetter)
                if (sum < 0):
                    string += alphabet[sum + len(alphabet)]
                else:
                    string += alphabet[sum]

    return string


for word in dictionary:
    key = getKey(word)
    decryptedString = decrypt(key, encryptedStringTest)
    decryptedStringSplit = decryptedString.split(" ")
    if (checkIfValid(decryptedStringSplit)):
        print("WORD=" + str(word))
        print(decrypt(key, encryptedString))


