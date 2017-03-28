# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Carré améliorer
# Date : 2/11/16
# Version : 3
l=input("entrez une largeur:")
while l<0:
	print"Donner une valeur supérieur à 0" 
	l=input("entrer une largeur:")
h=input("entrer une hauteur:")
while h<0:
	print"Donner une valeur supérieur à 0"
	h=input("entrer une hauteur:")
c=raw_input("entrer un caractère:")
print ("Voici votre carré creux:")
q=l-3
compteur=0
h=h-2
espace=c+" "
print espace*l
while compteur!=h:
		compteur+=1
		print espace,"  "*q,espace
print espace*l

