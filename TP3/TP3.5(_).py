#TP3.5 Exercice 5.2
import math
n=input("Donnez un nombre n:")
while n<=0:
	n=input("Autre nombre de 0")
i=1
print "Valeur		carre		cube	"
print "---------------------------------------"
while i!=n+1:
	print i,"		",int(math.pow(i, 2)),"		",int(math.pow(i,3))
	i=i+1
