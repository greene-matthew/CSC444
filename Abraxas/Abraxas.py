# Matthew Greene
# 102-49-075
# 3/26/2020

from sys import stdin
import re

ALPHABET = "7JZv. 964jMLh)5QtAS2PXWaFU8,/cpkY'O(Tqr?dsEmbRwINVKBez1=3+H0GyfxCiD\"lg:!uo"

dictionary = "dictionary.txt"
threshold = 0.3

d = open(dictionary, "r")
dictionary = d.read().rstrip("\n").split("\n")

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


# This is to return the number shift depending on the letters
def findShift(shiftedLetter, originalLetter, alphabet):
    return (alphabet.find(shiftedLetter) - alphabet.find(originalLetter)) % len(alphabet)


def decrypt(encryptedString, alphabet):
    decryptedString = ""
    for letter in encryptedString:
        if (letter not in alphabet):
            decryptedString += letter
        else:
            indexInShiftedAlphabet = alphabet.find(letter)
            try:
                decryptedString += ALPHABET[indexInShiftedAlphabet]
            except IndexError:
                continue
    return decryptedString


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


# This is the method to decrypt a string
def decryptString(word, alphabet):
        decryptedString = decrypt(encryptedText, alphabet)
        decryptedStringSplit = decryptedString.split(" ")

        if (checkIfValid(decryptedStringSplit)):
            print("WORD=" + str(word))
            print(decryptedString)
            return 1
        return 0

#This function checks if a word has duplicate letters
def checkForDuplicateLetters(word):
    letters = []
    for letter in word:
        if letter not in letters:
            letters.append(letter)
        else:
            return False
    return True

#This function makes the new alphabet with the word appended to the beginning of the alphabet
def setNewAlphabet(word):
    alphabet = ALPHABET
    lettersOfWord = []

    for letter in word:
        if letter not in lettersOfWord:
            lettersOfWord.append(letter)

    for letter in alphabet:
        if letter in lettersOfWord:
            alphabet = alphabet.replace(letter, "")

    alphabet = word + alphabet

    return alphabet

#This is where the function starts off it wil go through each word in the dictonary
#If it has duplicate letters it will skip that word in the dictanary
def newAlphabet():
    for word in dictionary:
        if(word[0] == 'd'):
            print(word)
            if checkForDuplicateLetters(word):
                alphabet = setNewAlphabet(word)
                if (decryptString(word, alphabet)):
                    break


#newAlphabet()

# print(checkForDuplicateLetters("hello"))

    for num in range(len(key)):
        if encryptedText[num] not in alphabet:
            print("THIS NOT IN TeXt: " + encryptedText[num])
            string += encryptedText[num]
        else:
            encryptedLetter = encryptedText[num]
            print(encryptedLetter)
            keyLetter = key[num]
            sum = alphabet.index(encryptedLetter) - alphabet.index(keyLetter)
            if (sum < 0):
                string += alphabet[sum + len(alphabet)]
            else:
                string += alphabet[sum]