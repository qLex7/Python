#Algorithme tp1
#Ex7 
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
	
	
l=[1,2,7,3,-1]
trier (l)
print (l)

