#!/usr/bin/env python3
#######################
#Guess the number
#######################

from random import randint

min = 5
while True:
	try:
		max = int(input("Input max number (more than "+str(min)+"):"))
		if max > min:
			break
	except ValueError: pass

num = randint(0, max)

ynum = -1
atts = []

while num != ynum:
	ynumold = ynum
	while True:
		try: ynum = int(input("You num (0..."+str(max)+"):"))
		except ValueError: pass
		if ynum != ynumold:
			break
	if ynum > num:
		print("More...")
		atts.append(ynum)
	elif ynum < num:
		print("Less...")
		atts.append(ynum)
	else :
		print("\nCongratulations!\n\tYou WIN!\n\tMy NUM is "+str(num)+"\n")
		print("Attempts count:["+str(len(atts))+"]\n")
		i = 0
		for att in atts:
			i += 1
			print(str(i)+":"+str(att))
		print ("\n")

print("End Of Game...\n")
