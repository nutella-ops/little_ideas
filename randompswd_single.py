import random
import string

pwdlim=input("pwd length: ")
n=0
char=""

while pwdlim > n:
	s=("{}".format(str(random.choice(string.printable))))
	char=char+s
	n+=1
	
print (char)
raise exit()
