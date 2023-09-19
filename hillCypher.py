# -*- coding: utf-8 -*-
"""
Created on Tue Sep  17 22:18:56 2023

@author: zhang siwei

"""
import random as rd
import numpy as np

alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", "'", "!", "?", ".","*")

#Creates a random key, while making sure the key can be inversed
def randomKey():
	
	while True:
		numbers = 0
		numbers = list()
		
		for number in range (0, 9):
			number = rd.randint(1, 9)
			numbers.append(number)
		key = createKey(numbers)
		
		if not verifyKey(key):
			break

	printKey = list()
	for row in key:
		for number in row:
			printKey.append(str(number))
	
	print("\nYour new key is:")
	print("".join(printKey))
	
	return key

#Verifies if the key for the cypher can be reversed
def verifyKey(key):
	return ((np.linalg.det(key) <= 0.5) and (np.linalg.det(key) >= -0.5)) or (np.linalg.det(key) % 5 == 0) or (np.linalg.det(key) % 3 == 0) or (np.linalg.det(key) % 2 == 0)

#Creates a 3x3 matrix with a list of 9 numbers
def createKey(numbers):
	key = np.array([[numbers[0], numbers[1], numbers[2]], [numbers[3], numbers[4], numbers[5]], [numbers[6], numbers[7], numbers[8]]])
	return key

#Lets the user use it's own key to encode the message while making sure the key can be reversed
def chooseKey():
	chosenKey = input("What key do you want to use? Please present a key with 9 numbers, without spaces:\n")	
	
	while not chosenKey.isdigit() or len(chosenKey) != 9:
		chosenKey = input("Your key has to be 9 numbers without any spaces. Choose another key:\n")
	
	numbers = list()
	for number in chosenKey:
		numbers.append(int(number))
	
	key = createKey(numbers)
	
	while verifyKey(key):
		chosenKey = input("Your key is not valid. Please choose another one:\n")
		numbers = list()
		for number in chosenKey:
			numbers.append(int(number))
		key = createKey(numbers)
		
		print("\nYour key is:")
		print(key)
		
	return key

#Takes the message to encrypt and transforms it into a list of numbers
def messageNumbers(message):
	message = message.lower()
	messageNumber = list()		#List with the message characters transformed into numbers as objects
	
	for char in message:
		if char in alphabet:		#transforms each characters into a number accordingly to it's position in the alphabet list
			index = alphabet.index(char)
			messageNumber.append(index)
		else:			#assign the * character to a character which isn't part of the alphabet
			messageNumber.append(len(alphabet) - 1)
	if (len(messageNumber) % 3 != 0):		#makes sure the message's lentgh is a multiple of 3, so the matrix can have rows of 3 elements
		nbrAjout = 3 - len(messageNumber) % 3
		for x in range (0, nbrAjout): 	#if not, add spaces until it can be divised by 3
			x = 26
			messageNumber.append(x)
	return messageNumber

#puts a list into a matrix with 3 columns and n rows
def matrix(matrix):
	nbrRange = len(matrix) // 3		#determines the number of rows for the matrix containing the list
	M = np.array([matrix[0], matrix[1], matrix[2]])	#Creates the first row(minimum number of row)
	if nbrRange > 1:		#if it needs more rows, create them and add them to the matrix
		for x in range (1, nbrRange):
			arrays = np.array([matrix[0 + 3*x], matrix[1 + 3*x], matrix[2 + 3*x]])
			M = np.vstack([M, arrays])
	return(M)

#takes the encoded message and converts it back into a string of characters
def messageEncoded(encodedNumber, alphabet):
	encodedNumber = encodedNumber.tolist()
	encodedMessage = list()
	try:
		for row in encodedNumber:
			for number in row:
				encodedMessage.append(str(number))
	except:
		for number in encodedNumber:
			encodedMessage.append(str(number))
	print("\nYour encoded message is:")
	print(" ".join(encodedMessage))
	
#asks the user for the code to be decoded	
def code():
	code = input("What's the code to be decoded? Write it down below:\n")
	code = code.split()
	
	while len(code) % 3 != 0:		#makes sure the code is valid(it has to be a multiple of 3 to be put back as a matrix)
		code = input("Your code has to be numbers, with a total of numbers which is a multiple of 3. Otherwise, there is a mistake. Try again:\n")
		code = code.split()
		
	codeList = list()
	for number in code:		#puts all the string numbers making the code in a list of integers
		number = int(number)
		codeList.append(number)
	
	return codeList

def messageText(messageNumber, alphabet):
	message = list()
	try:
		for number in messageNumber:
			number = int(round(number))
			number = number % 32 - 1
			message.append(alphabet[number])
	except:
		for row in messageNumber:
			for number in row:
				number = int(round(number))
				number = number % 32
				message.append(alphabet[number])
	return message