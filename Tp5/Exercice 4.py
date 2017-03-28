# -*- coding: utf-8 -*-
# Auteur : DEBORD Guillaume
# Rôle : Converge
#Date : 7/11/16
#Version : 1
n=input("Donnez n ?")
while n<1:
	print"Je vous dit un nombre supérieur à 1"
	n=input("Donnez un nombre supérieur à 1 s'il vous plait:")
sp=float(0)
sn=float(0)
s=float(0)
for i in range (1,n+1):
	if i%2.0==0.0:
		sn=sn-(1.0/i)
	else:
		sp=sp+(1.0/i)
s=sp+sn
print s
print"Au revoir !"
# la valeur XX de la série converge vers 0.64 lorsque l'on augmente la valeur de 10
