# Rijndael
# Sample template to show how to implement AES in Python
from __future__ import division
from sys import stdin
from hashlib import sha256
import re
from Crypto import Random
from Crypto.Cipher import AES


# the AES block size to use
BLOCK_SIZE = 16
# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"
# the key to use in the cipher

dictionary = "dictionary1-3.txt"
#dictionary = "dictionary4.txt"
#dictionary = "dictionary5.txt"
threshold = 0.75

d = open(dictionary, "r")
dictionary = d.read().rstrip("\n").split("\n")
d.close()


# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# get the 16-byte IV from the ciphertext
	# by default, we put the IV at the beginning of the ciphertext
	iv = ciphertext[:16]

	# decrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# the ciphertext is after the IV (so, skip 16 bytes)
	plaintext = cipher.decrypt(ciphertext[16:])

	# remove potential padding at the end of the plaintext
	# figure this one out...

	# return plaintext.rstrip("#")
	return plaintext.replace("#", "")


# encrypts a plaintext with a key
def encrypt(plaintext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# generate a random 16-byte IV
	iv = Random.new().read(BLOCK_SIZE)

	# encrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# if necessary, pad the plaintext so that it is a multiple of BLOCK SIZE in length
	plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
	# add the IV to the beginning of the ciphertext
	# IV is at [:16]; ciphertext is at [16:]
	ciphertext = iv + cipher.encrypt(plaintext)

	return ciphertext


def checkIfValid(decryptedString,key):
	words = len(decryptedString)
	validWords = 0

	for x in decryptedString:
		x = re.sub(r'[^A-Za-z]', '', x)
		if x.lower() in dictionary:
			validWords += 1

	if ((validWords / words) >= threshold):
#	if("%PDF-" in decryptedString[0]):
		return True
	else:
		return False


# MAIN
plaintext = stdin.read().rstrip("\n")
ciphertext = plaintext

for word in dictionary:
	#if(word[0] == "J" or word[0] == "j"):
		#print(word)
		decryptedString = decrypt(ciphertext, word)
		if (checkIfValid(decryptedString.split(" "),word)):
			print("KEY=" + str(word))
			print(decryptedString)

