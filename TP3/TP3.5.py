#TP3.5 Exercice 5.1
import math
n=input("Donnez un nombre n:")
while n<=0:
	n=input("Autre nombre de 0")
print "Valeur		carre		cube	"
print "---------------------------------------"
for i in range (1,n+1):
	print i,"		",int(math.pow(i, 2)),"		",int(math.pow(i,3))
