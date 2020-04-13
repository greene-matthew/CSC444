#Matthew Greene
#102-49-075
#3/19/2020

from sys import stdin
import re
import base64

alphabet = "GHXJ+g5y6Asd3ZB4D12NT8mQEcarbSIo7zwjltOWu9eP/pFVL0KYqx=hRUCkviMf"

dictionary = "dictionary.txt"
threshold = 0.01

d = open(dictionary, "r")
dictionary = d.read().rstrip("\n").lower().split("\n")
d.close()

encryptedText = stdin.read()
encryptedText = list(encryptedText)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
sortedText = {}

## This is to sort the encrypted text by letter. I assume that vowels would apper the most in a text
for x in encryptedText:
    if x not in sortedText.keys():
        sortedText[x] = 1
    if x in sortedText.keys():
        sortedText[x] = sortedText[x] + 1
sortedLetters = sorted(sortedText.items(), key=lambda x: x[1], reverse=True)

#This is to return the number shift depending on the letters
def findShift(shiftedLetter, originalLetter):
    return (alphabet.find(shiftedLetter) - alphabet.find(originalLetter)) % len(alphabet)


def decrypt(shiftedLetter, originalLetter, encryptedString):
    shift = findShift(shiftedLetter, originalLetter)
    decryptedString = ""
    for letter in encryptedString:
        if (letter not in alphabet):
            decryptedString += letter
        else:
            decryptedString += alphabet[(alphabet.find(letter) - shift) % len(alphabet)]


    return decryptedString

#This method checks the decrypted string agaisnt the dictionary. If 75% of the words in the string
#are in the dictonary we return the string
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


# This is the method to decrypt a string
def decryptString():
    # we will first check the vowels and see if we can decrypt the string with the vowels


    # If we dont crack the string with the vowels we will then check every letter
    for letter in alphabet:

        decryptedString = decrypt(encryptedText[0], letter, encryptedText)
        decryptedStringSplit = decryptedString.split(" ")

        shift = findShift(encryptedText[0], letter)
        print("SHIFT=" + str(shift))
        print(decryptedString)




decryptString()


