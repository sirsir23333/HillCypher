import time
import hillCypher as hc

wait = .5

#MAIN PROGRAM

#Lets the user decides if he wants to use his own key to encode or if he wants to or have a key randomly
#assigned for him
choiceKey = input("Have you already chosen a key(a) or do you want a random key?(b):\n")

while choiceKey != "a" and choiceKey != "b":
	choiceKey = input('Please type "a" or "b" as your answer:\n')

time.sleep(wait)

if choiceKey == "b":
	K = hc.randomKey()
else:
	K = hc.chooseKey()

time.sleep(wait)

#Transform the user's message into a matrix with numbers associated to each characters 
message = input("What message do you want to encode? Write it below:\n")
messageNumber = hc.messageNumbers(message)
M = hc.matrix(messageNumber)

#encodes the message M with the key K (matrix multiplication)
encodedNumber = M.dot(K)

time.sleep(wait)

#gives back a message with characters and not numbers
hc.messageEncoded(encodedNumber, hc.alphabet)

time.sleep(wait)

input("\nPress enter to exit the encoder.\nDon't forget you'll need the key to decode the message")