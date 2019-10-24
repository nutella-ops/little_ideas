import random
import string

while(1):
	pwdlim=input("pwd length: ")
	n=0
	char=""

	while pwdlim > n:
		s=random.choice(string.printable)
		char=char+s
		n+=1
	print (char)
	print("")
