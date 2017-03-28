#Algorithme tp1
#Ex9
def recherche_indices(l,x):
	l_indices=[]
	for i in xrange(len(l)):
		if (l[i]==x):
			l_indices.append(i)
			
	return l_indices
	
l=[5,1,3,8,9,1,1]

l1=recherche_indices(l,1)
print l1
