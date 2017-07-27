#!/usr/bin/env python3
########################
#   Guess the number   #
########################

from random import randint

min = 5

while True:
	try:
		max = int(input("Input max number (more than "+str(min)+"):"))
		if max > min:
			break
	except ValueError:
		print("ValueError: Please try again.")
		pass

while True: 
	num = randint(0, max)
	ynum = -1
	atts = []
	i = 0
	att = 0

	while num != ynum:
		ynumold = ynum

		while True:
			try:
				ynum = int(input("Enter number (0..."+str(max)+"):"))
			except ValueError:
				print("ValueError: Please try again.")
				pass
			if ynum != ynumold:
				break
			else:
				print("Enter new value")
		if ynum > num:
			print("More...")
			atts.append(ynum)
		elif ynum < num:
			print("Less...")
			atts.append(ynum)
		else:
			atts.append(ynum)
			print("\nCongratulations!\n\tYou WIN!\n\tMy number is "+str(num)+"\n")
			print("Attempts count:["+str(len(atts))+"]\n")
			for att in atts:
				i += 1
				print(str(i)+":"+str(att))
			print ("\n")

	game = input("Do you want play agen?\n[Y/N]:")
	if game != "Y":
		break

print("End Of Game...\n")


