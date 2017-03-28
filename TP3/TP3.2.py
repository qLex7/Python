#TP3 Exercice 2
prix=42
x=input("Rentrer un prix :")

while x!=prix :
	if x<prix :
		print "superieur"
	elif x>prix :
		print "inferieur"
	x=input("Retenter votre chance:")
print "bravo"
