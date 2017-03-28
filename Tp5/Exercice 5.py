# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Converge
#Date : 7/11/16
#Version : 2
n=input("Entrez un nombre supérieur à 1:")
while n<1:
	print n, ("la valeur est inférieur à 1!")
	n=input("Entrez un nombre supérieur à 1:")
a=1.0
b=2.0
for num in range(1,n+1):
	a=a+(1/(b**num))
print"La valeur de la série est égale à:",a
print"Au revoir !"
