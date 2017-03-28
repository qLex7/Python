# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Trigonométrique
#Date : 7/11/16
#Version : 1
from math import*
n=input("Entrez un nombre supérieur à 1:")
while n<1:
	print "Désolé",n,"est négatif !"
	n=input("Entrez un nombre supérieur à 1:")
print"n		sin(n)		sin(n)*cos(n)"
print"-----------------------------------------------------"
for i in range (1,n+1):
	print i,"			",sin(i),"			",sin(i)*cos(i)
print"Au revoir"
