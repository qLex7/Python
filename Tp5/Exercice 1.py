# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Triangle
#Date : 7/11/16
#Version : 1
h=input("Entrez la hauteur:")
while h<0:
	 h=input("Entrez la hauteur:")
for num in range(1,h+1):
	if num <=2:
		print num*"*"
	elif 2 <num<h:
		print"*"+(num-2)*"-"+"*"
	elif num==h:
		print h*"*"
