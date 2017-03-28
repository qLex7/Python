# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : triangle 
# Date : 2/11/16
# Version : 4
h=input("entrez une hauteur:")
while h<0:
	print"Donner une valeur supérieur à 0" 
	h=input("entrer une hauteur:")
c=raw_input("entrer un caractère:")
print"Voici votre triangle:"
for i in range(1,h+1):
	print c*i

