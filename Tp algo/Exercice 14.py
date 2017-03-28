#Algorithme tp1
#Ex14

def fonction (l1,x,epsilon):
	for i in l1:
		if epsilon<(i-x)<epsilon:
			return True
	return False
	
l1=[0,2,4,6,8,10,12,14,16]
x=8
epsilon=4
print fonction(l1,x,epsilon)
