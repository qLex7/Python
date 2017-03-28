#TP3.7 Exercice 7
x=input("Saisissez un nombre entier positif:")
x1=1
x2=1
compteur=0
while x<=0:
		x=input("Saisissez un nombre entier positif:")

print "Methode avec for :\n"

for i in range (1,x+1):
		x1*=i
print " La factorielle de ce nombre est",x1

print " Methode avec while:\n"

while compteur !=x:
		compteur +=1
		x2*=compteur
print " La factorielle de ce nombre est",x2
