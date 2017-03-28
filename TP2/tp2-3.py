#Tp2-3

from math import *
print"Bonjour"
a=input("coefficient a=")
b=input("coefficient b=")
c=input("coefficient b=")
x=0
disc=0
if a==0:
	print"x=",-c/b
if a>0:
	disc= b**2-4*a*c
	if disc<0:
		print"Discriminant",disc
		print"Discrimininant negatif  Au revoir "
	elif disc>0:
		print"Discriminant",disc
		print"*** Les 2 racines"
		print"x1=",(-b+(sqrt(disc)))/(2*a)
		print"x2=",(-b-(sqrt(disc)))/(2*a)
		


	
