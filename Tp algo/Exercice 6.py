#Algorithme tp1
#Ex6

def moyenne(l):
		som=0.0
		for i in xrange(0,len(l)):
			som+=l[i]
		return som/len(l)
		
def variance(l):
	m=moyenne(l)
	return(sum([(x-m)**2 for x in l])/len(l))

l=[1,2,3,4,5]
print variance(l)
