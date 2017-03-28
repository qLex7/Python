#Algorithme tp1
#Ex4

def indice(l):
	ind=0
	m=l[0]
	for i in xrange(0,len(l)):
		if l[i]>m:
				m=l[i]
				ind=i
	return ind

l=[2,5,6,7,2,10,25,10,40]
print indice(l)

