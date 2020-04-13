# Et tu, Brute?
# Marcus A. Castille Jr.
# CSC - 444
# Spring 2020

import sys
import re
import copy

# the alphabet
# ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
ALPHABET = "7JZv. 964jMLh)5QtAS2PXWaFU8,/cpkY'O(Tqr?dsEmbRwINVKBez1=3+H0GyfxCiD\"lg:!uo"

# This dictionary allows us to keep track of a character's original index in the alphabet by only iterating over it once
ALPHABET_dict = {}
for idx, character in enumerate(ALPHABET):
    ALPHABET_dict[character] = idx


def decrypt(cipher_text, keyword):
    cipher_alphabet = list(ALPHABET)

    for idx, character in enumerate(keyword):
        cipher_alphabet.remove(character)
        cipher_alphabet.insert(idx, character)

    cipher_alphabet_dict = {}

    for idx, character in enumerate(cipher_alphabet):
        cipher_alphabet_dict[character] = ALPHABET[idx]

    decoded_lines_of_text = []
    for line in cipher_text:
        # Here we turn the string representing a line of text into an array so that it can manipulated
        line_of_text = list(line)
        for j, character in enumerate(line_of_text):
            # If the current character is not in the alphabet we do not attempt a shift and leave it as is
            try:
                # Here we perform the shift on the current character
                line_of_text[j] = cipher_alphabet_dict[character]
            except KeyError:
                line_of_text[j] = character

        decoded_lines_of_text.append(line_of_text)

    # Here we construct the decoded string to return by appended each line of text
    decoded_message = ''
    for idx, line in enumerate(decoded_lines_of_text):
        decoded_message += ''.join(line)
        if idx != len(decoded_lines_of_text) - 1:
            decoded_message += '\n'

    return decoded_message


for idx, character in enumerate(ALPHABET):
    ALPHABET_dict[character] = idx

DICTIONARY_FILE = "dictionary.txt"

THRESHOLD = 0.7

# Here we read in the cipher text from stdin and grab the first 10 lines
cipher_text = sys.stdin.read().rstrip('\n')
cipher_text_restricted = cipher_text.split('\n')[:10]

file = open(DICTIONARY_FILE, "r")
dictionary = file.read().rstrip('\n').split('\n')

valid_key_words = []
dictionary_mapping = {}
for keyword in dictionary:
    if len(set(keyword)) == len(keyword):
        valid_key_words.append(keyword)
    if keyword != '':
        dictionary_mapping[keyword.lower()] = True

counts = []
for keyword in valid_key_words:
    count = 0

    plain_text = decrypt(cipher_text_restricted, keyword)
    list_of_decoded_words = plain_text.split(' ')

    for word in list_of_decoded_words:
        # All punctuation is removed from words, except for single quotes, to be matched against the given dictionary
        word = (re.sub('[!?(",.]', '', word))

        # We match against the dictionary's dictionary (ironic) and increment the count accordingly
        try:
            if dictionary_mapping[word.lower().replace('\n', '')]:
                count += 1
        except KeyError:
            continue

    counts.append(count)
    # The percentage of words that were found in the dictionary are matched against the threshold to determine if the
    # decoded message is the correct one
    if count > (len(list_of_decoded_words) * THRESHOLD):
        decoded_text = decrypt(cipher_text.split('\n'), keyword)
        print('Key={}:\n{}'.format(keyword, decoded_text))
        exit(1)
