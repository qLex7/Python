# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Diviseurs
#Date : 7/11/16
#Version : 1
from math import*
n=input("Ecrivez un nombre supérieur à zéro:")
while n<0:
	print"Je vous ai demandé un nombre supérieur à zéro!"
	n=input("Ecrivez un nombre supérieur à zéro:")
print "Voici les diviseurs de",n
divis=0
for i in range(1,n+1):
		div=n%i
		if div==0:
			print i
			divis=divis+1
print n,"possède donc",divis,"diviseur"
