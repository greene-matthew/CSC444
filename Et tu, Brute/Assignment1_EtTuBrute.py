# Et tu, Brute?
# Marcus A. Castille Jr.
# CSC - 444
# Spring 2020

import sys
import re
import base64

# the alphabet
# ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"
# ALPHABET = "7JZv. 964jMLh)5QtAS2PXWaFU8,/cpkY'O(Tqr?dsEmbRwINVKBez1=3+H0GyfxCiD\"lg:!uo"
ALPHABET = "GHXJ+g5y6Asd3ZB4D12NT8mQEcarbSIo7zwjltOWu9eP/pFVL0KYqx=hRUCkviMf"

# This dictionary allows us to keep track of a character's original index in the alphabet by only iterating over it once
ALPHABET_dict = {}

for idx, character in enumerate(ALPHABET):
    ALPHABET_dict[character] = idx

DICTIONARY_FILE = "dictionary.txt"

THRESHOLD = 0.25


# This function takes in an encoded message and a number to shift the alphabet by in order to generate a decoded message
# based off of that shift
def rot(encoded_message, shift):
    decoded_lines_of_text = []

    for line in encoded_message:
        # Here we turn the string representing a line of text into an array so that it can manipulated
        line_of_text = list(line)
        for j, character in enumerate(line_of_text):
            # If the current character is not in the alphabet we do not attempt a shift and leave it as is
            try:
                # Here we perform the shift on the current character
                character_index = ALPHABET_dict[character]
                shifted_character_index = character_index + shift

                if shifted_character_index > len(ALPHABET) - 1:
                    line_of_text[j] = ALPHABET[shifted_character_index - len(ALPHABET)]
                else:
                    line_of_text[j] = ALPHABET[shifted_character_index]
            except KeyError:
                line_of_text[j] = character

        decoded_lines_of_text.append(line_of_text)

    decoded_message = ''

    # Here we construct the decoded string to return by appended each line of text
    for idx, line in enumerate(decoded_lines_of_text):
        decoded_message += ''.join(line)
        if idx != len(decoded_lines_of_text) - 1:
            decoded_message += '\n'

    return decoded_message


file = open(DICTIONARY_FILE, "r")
dictionary = file.read().rstrip('\n').lower().split('\n')

# This dictionary allows us to quickly determine if a word is in the dictionary without having to iterate over the
# list of valid words
dictionary_mapping = {}

for word in dictionary:
    if word != '':
        dictionary_mapping[word] = True

# Here we read in the cipher text from stdin and grab the first 10 lines
cipher_text = sys.stdin.read().rstrip('\n')
cipher_text_restricted = cipher_text.split('\n')[:10]

# Shifts are tried from 1 to the length of the alphabet to determine the correct shift that generates the decoded
# message
for i in range(1, len(ALPHABET)):
    print('Shift: ' + str(len(ALPHABET) - i))
    decoded_text = rot(cipher_text_restricted, i)

    print(decoded_text)
    print('\n\n')
    try:
        list_of_decoded_words = decoded_text.split(' ')
    except Exception:
        continue
    count = 0
    # Here we iterate over every decoded word to determine if it is in the dictionary and determine if the decoded text
    # is within the threshold
    for word in list_of_decoded_words:
        # All punctuation is removed from words, except for single quotes, to be matched against the given dictionary
        word = (re.sub('[!?(",.]', '', word))

        # We match against the dictionary's dictionary (ironic) and increment the count accordingly
        try:
            if dictionary_mapping[word.lower().replace('\n', '')]:
                count += 1
        except KeyError:
            continue

    # The percentage of words that were found in the dictionary are matched against the threshold to determine if the
    # decoded message is the correct one
    if count > (len(list_of_decoded_words) * THRESHOLD):
        decoded_text = rot(cipher_text.split('\n'), i)
        print("SHIFT={}:\n{}".format(len(ALPHABET) - i, decoded_text))
        exit(1)

print("No matching plaintext found")
