# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : triangle amélioré
# Date : 2/11/16
# Version : 5
h=input("entrez une hauteur:")
while h<0:
	print"Donner une valeur supérieur à 0" 
	h=input("entrer une hauteur:")
c=raw_input("entrer un caractère:")
print"Voici votre triangle:"
q=h-1
n=1
while q>=0:
		print " "*q,c*n
		q-=1
		n+=1
