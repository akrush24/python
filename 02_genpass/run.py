#!/usr/bin/env python3

from random import choice

chnum = "0 1 2 3 4 5 6 7 8 9"
chstr = "a b c d e f j h i j k l m n o p q r s t x y z"
chc = "? & # @ % ^"

pas = ""

pass_ch = (chstr+chstr+chc).split()
cmin = 4

while True:
	try:
		cmax = int(input("Enter password length[min "+str(cmin)+"]: "))
	except ValueError: pass
	if cmax >= cmin: break

for ch in range(cmin,cmax):
	pas = pas+choice(pass_ch)
print(pas)
