#Algorithme tp1
#Ex16

def jour(a):
	n=a/100
	m=a%100
	return n,m
	
def semaine (j,m,a):
	d=0
	if m<11:
		y=a-1
		d=(((23*m)/9)+j+4+a+(y/4)-(y/100)+(y/400))%7
	elif m>=3:
		y=a
		d=(((23*m)/9)+j+4+a+(y/4)-(y/100)+(y/400)-2)%7
	return s[d]
	
	
s=["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
j=10
m=11
a=1996
print jour(a)
print semaine(j,m,a)
