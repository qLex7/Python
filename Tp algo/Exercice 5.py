#Algorithme tp1
#Ex5
def moyenne(l):
		som=0.0
		for i in xrange(0,len(l)):
				som+=l[i]
		return som/len(l)
l=[6,10,20,68,2]
print moyenne(l)
