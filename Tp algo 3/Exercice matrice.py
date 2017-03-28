#Exercice Tp Matrice
# coding: utf-8 

from random import*
 
class Matrice:
	"""Une matrice est un tableau a deux dimensions contenant des nombres reels"""
	
	def __init__(self,l,c):   #Exercice 1
		self.l=l
		self.c=c
		self.L=[]
		for i in xrange(0,self.l):
			self.L.append([])
			for j in xrange(0,self.c):
				self.L[i].append(0)
						
	def get(self):      #Exercice 2
		for i in xrange(0,self.l):
			for j in xrange(0,self.c):
				x=input("Entrez une valeur:")
				self.L[i][j]=x
	
	def printer(self):   #Exercice 3
		for i in xrange(0,self.l):
			for j in xrange(0,self.c):
				print self.L[i][j],
				
				print''
				
				
				
	def dimension():     #Exercice 4
		return l,c
		
	def randomize(self): #Exercice 5
		for i in xrange(self,l):
			for j in xrange(self,c):
				self.l[i],[j]=random.uniform(-1,1)
				
	def add(self,b):   #Exercice 6
		l, c=self.dimension()
		l2, c2=b.dimension()
		if l!=l2 and c!=c2:
			print "Erreur"
			
			return
		d=Matrice(l,c)
		for j in range(c):
			for i in range(l):
					d.self.l[i][j]=self.l[i][j]+b.l[i][j]
			print "Addition des deux matrices"
							
		return
				
	
		
		
#Entré des lignes et colones		
a=Matrice(1,1)
b=Matrice(1,1)
d=Matrice(1,1)

#Donner les valeurs
a.get()
b.get()


#Afficher les valeurs
a.printer()
b.printer()
d.printer()


b.add(d)
	
				
	
