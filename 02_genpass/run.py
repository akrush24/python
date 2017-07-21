#!/usr/bin/env python3
# password generator

from random import choice

chnum = "0 1 2 3 4 5 6 7 8 9"
chstr = "a b c d e f j h i j k l m n o p q r s t x y z"
chc = '~ ! @ # $ % ^ & * ( ) _ + ` - = { } [ ] : ; < > . / '

pas = ""
cmin = 4
cdef = 8
cmax = 100
clen = cdef

pass_ch = (chnum+chstr+chc+chstr.upper()).split()

while True:
	try:
		clen = int(input("Enter password length[MIN:"+str(cmin)+";MAX:"+str(cmax)+";DEF:"+str(cdef)+"]: "))
		if clen == "": clen = cdef
	except ValueError: pass
	if clen >= cmin and clen <= cmax: break

for ch in range(0,clen):
	pas = pas+choice(pass_ch)
print(pas)
