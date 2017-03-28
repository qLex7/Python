#Algorithme tp1
#Ex3

def cherche_pnp(l,x,n):
	if (len(l)<n): n=len(l)
	for i in xrange(0,n):
		if (x==l[i]):return True
	return False


def doublon(l):
	n=0
	m=len(l)
	for i in xrange(0,m):
		if cherche_pnp(l,l[n],n)==True:
			l.remove(l[n])
		else: n=n+1

l=[2,3,5,10,20,40,7,1,3,2,7,5,7,10,15]
doublon(l)
print l
