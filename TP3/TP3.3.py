#TP3 Exercice 3
from random import randint
rep=1
while rep>0:
	prix=randint(1,100)
	x=input("Rentrer un prix :")
	while x!=prix :
		if x<prix :
			print "superieur"
		elif x>prix :
			print "inferieur"		
		x=input("Retenter votre chance:")
	print "bravo"
	rep=input("Voulez vous continuer? 0/1")
	if rep==0:
		rep=1
	else:
		print"merci d'avoir joue"
