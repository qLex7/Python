#Algorithme tp1
#Ex1
#saisie une liste:
def chercher(l,x):
	for e in xrange (0,len(l)):
		if (e==x):return True
	return False

l=[2,3,5,10,20,40,7,1]
print chercher(l,7)
print chercher(l,60)

