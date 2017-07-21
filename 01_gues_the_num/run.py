#!/usr/bin/env python3
#######################
#Guess the number
#######################

from random import randint

min = 100
while True:
	try:
		max = int(input("Input max number (more than "+str(min)+"):"))
		if max > 10:
			break
	except ValueError: pass

num = randint(0, max)

ynum = -1
att = []

while num != ynum:
	ynumold = ynum
	while True:
		try: ynum = int(input("You num (0..."+str(max)+"):"))
		except ValueError: pass
		if ynum != ynumold:
			break
	if ynum > num:
		print("More...")
		att.append(ynum)
	elif ynum < num:
		print("Less...")
		att.append(ynum)
	else :
		print("\nCongratulations!\n\tYou WIN!\n\tMy NUM is "+str(num)+"\n")
		print("Attempts count:["+str(len(att))+"]\n"+str(att)+"\n")

print("End Of Game...\n")
