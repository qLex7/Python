# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : triangle amélioré
# Date : 2/11/16
# Version : 6
h=input("entrez une hauteur:")
while h<0:
	print"Donner une valeur supérieur à 0" 
	h=input("entrer une hauteur:")
c=raw_input("entrer un caractère:")
print"Voici votre triangle:"
q=h-1
n=0
for i in range(1,h+1):
		if i==1:
			print " "*q+c
			q-=1
		elif 1<i<h:
			print " "*q+c+" "*n+c
			q-=1
			n+=1
		elif i==h:
			print c*h
