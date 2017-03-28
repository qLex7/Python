# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : racine carré
# Date : 2/11/16
# Version : 1
from math import *

n=input("Donnez un nombre:")
while n<0:
	print("Votre nombre doit être positif")
	n=input("Donnez un nombre:")
c=0
s=0.0
x=1.0
for i in range(1,n+1):
	c=1.0/x**2
	x*=2
	s+=c
print s
#La valeur XX converge vers 1.33 lorsque l'on augmente la valeur de n
