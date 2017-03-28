#Algorithme tp1
#Ex2

def occ(l,x):
	cpt=0
	for i in xrange (0,len(l)):
		if (l[i]==x):
			cpt=cpt+1
	return cpt
	
l=[41,10,25,6,7,30,70,41]
n=occ (l,41)
print n

