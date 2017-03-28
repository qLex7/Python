#Algorithme tp1
#Ex11


def fusion(l1,l2):
	l3=[ ]
	i=0
	j=0
	while i<len(l1) and j<len(l2):
		if (l1[i]<l2[j]):
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if (i==len(l1)):
		for e in xrange(j,len(l2)):
			l3.append(l2[e])
	else:
		for x in xrange(i,len(l1)):
			l.append(l1[x])
	return l3
	
l1=[0,2,4,6]
l2=[1,3,5,7]
l3=fusion(l1,l2)
print l3
	
	
