#Tp2-1

a=input("Entrer un nombe,")
b=input("Entrer un nombe,")
c=input("Entrer un nombe,")
d=input("Entrer un nombe,")
e=input("Entrer un nombe,")
f=input("Entrer un nombe,")
x=input("x=")

if a<b<c<d<e<f:
	print"Plage invalide"
	exit ()
else:
	print"Plage valide"
if a<=x and x<=b:
	print"Dans la fourchette"
elif c<x and x<d:
	print"Dans la fourchette"
elif e<=x and x<f:
	print"Dans la fourchette"
else:
	print"En dehors de la fourchette"
