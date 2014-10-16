# breaking caesar ciphered message

import string

# all the alphabet letters in a list
ALPHABET=list(string.ascii_lowercase)

# lower and upper case alphabet
ALPHABET_LU=list(string.letters)

def cipher_big_msg(message, shift):
	""" this function is more efficient if the message is very long
	as it will iterate only over the 26 letters. On the other hand, 
	it will return the message in upper case """
	
	# working only with lowercase
	message = message.lower()

	# shifting the alphabet 
	shifted_alphabet = ALPHABET[shift:] + ALPHABET[0:shift]

	# I replace the shifted alphabet with upper case so there isn't problem when replacing the letters
	# (to not replace a letter that has already been replaced)
	shifted_alphabet = [letter.upper() for letter in shifted_alphabet]

	# we look for each letter of the alphabet and replace them
	for i in range(0,26):
		message = message.replace(ALPHABET[i], shifted_alphabet[i])

	return message

def cipher(message, shift):
	""" goes over each letter of the message and replace the letter. 
	It keeps the letter case """

	# shifting the alphabet
	shifted_alphabet = ALPHABET_LU[shift:26] + ALPHABET_LU[0:shift] + ALPHABET_LU[26+shift:] + ALPHABET_LU[26:26+shift]

	# transform the string into a list to be able to modify it
	message = list(message)

	for i in range(0,len(message)):
		if message[i].isalpha():
			# get the letter index
			j = ALPHABET_LU.index(message[i])
			message[i] = shifted_alphabet[j]

	# converting list to string
	message = ''.join(message)

	return message


# not knowing the shift value, we display a snippet of the cipher text with all the combination
for i in range(1,26):
	print "The shift is " + str(i) + ", the result is: " + cipher("Bpm abclg", i)


print cipher("\"The study of mathematics, like the Nile, begins in minuteness but ends in magnificence.\" Charles Caleb Colton", 8)

print cipher("\"Bpm abclg wn uibpmuibqka, tqsm bpm Vqtm, jmoqva qv uqvcbmvmaa jcb mvla qv uiovqnqkmvkm.\" Kpiztma Kitmj Kwtbwv", 18)

