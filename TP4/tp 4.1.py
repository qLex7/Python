# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Carré améliorer
#Date : 2/11/16
#Version : 1
l=input("Entrez une longueur:")
while l<0:
	print"Donner une valeur supérieur à 0"
	l=input("Entrez une longueur:")
h=input("Entrez une hauteur:")
while h<0:
	print"Donner une valeur supérieur à 0"
	h=input("Entrez une hauteur:")
print("Voici votre carré:")
for i in range(1,h+1):
	print"*"*l
