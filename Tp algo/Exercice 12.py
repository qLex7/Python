#Algorithme tp1
#Ex12

from math import*

def calcul(a,b,c):
	disc=0
	x1=0
	x2=0
	disc=b**2-4*a*c
	
	if disc==0:
		x1=(-b/2*a)
		return x1
		
	elif disc>0:
		x1=(-b+sqrt(disc))/2*a
		x2=(-b-sqrt(disc))/2*a
		return x1,x2
	elif disc<0:
		return 0
		
a=input("Entrer une valeur pour a:")
b=input("Entrer une valeur pour b:")
c=input("Entrer une valeur pour c:")
print calcul(a,b,c)
	
