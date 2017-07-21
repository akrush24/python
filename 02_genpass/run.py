#!/usr/bin/env python3

from random import randint
from random import getrandbits
from random import sample

chnum = "0 1 2 3 4 5 6 7 8 9"
chstr = "a b c d e f j"
chc = "?&#@%^"

pas = ""

for ch in sample((chstr+chstr+chc).split(),4):
	pas = pas+ch
print(pas)
