#Algorithme tp1
#Ex13

def inter(l1,l2):
	l3=[]
	i=0
	j=0
	n=len(l1)
	while i<n:
		if l1[i]==l2[j]:
			l3.append(l1[i])
			i+=1
			j+=1
		else:
			i+=1
			j+=1
	return l3
	
l1=[0,2,6,9,12]
l2=[0,2,7,9,15]
print inter(l1,l2)
