# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : triangle amélioré
# Date : 2/11/16
# Version : 7
h=input("entrez une hauteur:")
while h%2==0:
	print"Donner une valeur supérieur à 0" 
	h=input("entrer une hauteur:")
c=raw_input("entrer un caractère:")
print"Voici votre triangle:"
espace=0
q=h-2
while q>=0:
	print" "*espace+c*q+" "*espace
	q-=2
	espace+=1
