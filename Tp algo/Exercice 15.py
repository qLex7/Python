#Algorithme tp1
#Ex14

def pgcd(p,q):
	if p<q and q%p==0:
		return p
	elif q<p and p%q==0:
		return q
	else:
		return pgcd(p,p%q)
		
p=input("Donnez une valeur pour a:")
q=input("Donnez une valeur pour b:")
print "Le plus grand diviseur commun de ",p,"et",q,"est",pgcd(p,q)
