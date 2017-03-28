#Algorithme tp1
#Ex10
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
			
			
def insere_trie(l,x):
	n=len(l)
	if (x<= l[0]):
		l.inster(0,x)
		return
	if (x>= l[n-1]):
		l.inster(n,x)
		return
	d=0
	f=n-1
	while (f-d)>1:
		m=(f+d)/2
		if(x<l[m]):
				f=m
		else:
				d=m
	l.insert(d+1,x)

l=[1,10,6,7,9,15]
x=3
insere_trie(l,x)
trier (l)
print l
