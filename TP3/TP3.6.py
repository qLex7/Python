#TP3.6 Exercice 6
l=input("entrez une largeur:")
h=input("entrez une hauteur:")
while l==1: 
	l=input("entrer une largeur:")
	print"Donnez des valeurs superieur a 1"
while h==1:
		h=input("entrer une hauteur:")
q=l-3
compteur=0
h=h-2
print "* "*l
while compteur!=h:
		compteur+=1
		print "* ","  "*q,"*"
print "* "*l

