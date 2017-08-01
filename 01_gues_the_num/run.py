#!/usr/bin/env python3
########################
#   Guess the number   #
########################

from random import randint
name = ""

min = 100

def hello(name):
	print("Hello "+name+"!\n")

while name is "":
	name = input("Print you name: ")

hello(name)

while True:
	try:
		max = int(input("Input max number (more than "+str(min)+"):"))
		if max >= min:
			break
		elif max < min:
			print("You type number less than "+str(min))
	except ValueError:
		print("ValueError: Please try again.")
		pass

while True: 
	num = randint(0, max) #generation a random number
	you_num = -1
	atts = []
	i = 0
	att = 0

	while num != you_num:
		you_numold = you_num

		while True:
			try:
				you_num = int(input("Enter number (0..."+str(max)+"):"))
			except ValueError:
				print("ValueError: Please try again.")
				pass
			if you_num != you_numold:
				break
			else:
				print("Enter new value")
		if you_num > num:
			print("More...")
			atts.append(you_num)
		elif you_num < num:
			print("Less...")
			atts.append(you_num)
		else:
			atts.append(you_num)
			print("\nCongratulations!\n\tYou WIN!\n\tMy number is "+str(num)+"\n")
			print("Attempts count:["+str(len(atts))+"]\n")
			for att in atts:
				i += 1
				print(str(i)+":"+str(att))
			print ("\n")

	game = input("Do you want play agen?\nType [Y/N]:")
	if game != "Y":
		break

print("End Of Game...\n")
