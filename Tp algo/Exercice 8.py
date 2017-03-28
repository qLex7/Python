#Algorithme tp1
#Ex8
def ind_pg_pnp(l,n):
	if(n>len(l)):
			n=len(l)
	ind=0
	for i in range (0,n):
			if (l[ind]<l[i]):
				ind=i
	return ind
		
def trier(l):
		n=len(l)
		for i in xrange(0,n-1):
			ind=ind_pg_pnp(l,n-i)
			l[ind],l[n-i-1]=l[n-i-1],l[ind]
	
def mediane(l):
	a=0
	b=0
	trier(l)
	for i in xrange(0,len(l)):
		if len(l)%2!=0:
			a=(len(l))/2
			return l[a]
		else:
			a=len(l)/2
			b=len(l)/2-1
			return a+b/2
	
l=[1,2,7,3,-1]
trier (l)
print (l)
print mediane(l)
