#Algorithme tp2
#Exo 5
from math import*

class Point:	#Exercice 1
	"""Classe definissant un point par:
	- x
	- y
	- z"""
	def __init__(self):
		self.x=0.0
		self.y=0.0
		self.z=0.0
			
	def Afficher (self):      #Exercice 2
		print"(",self.x,",",self.y,",",self.z,")"

	def Saisir (self):        #Exercice 3
		self.x=input("Valeur de x:")
		self.y=input("Valeur de y:")
		self.z=input("Valeur de z:")
		
	def inf_ou_egal(self,Q):   #Exercice 4
		Q.x=3
		Q.y=5
		Q.y=7
		if(self.x<Q.x):
			return True
		if(self.x>Q.x):
			return False
		if( self.y<Q.y):
			return True
		if(self.y>Q.y):
			return False
		if(self.z<Q.z):
			return True
		if(self.z>Q.z):
			return False
		return True
	
	def distance(self,Q):   #Exercice 5
		return sqrt((self.x-Q.x)**2+(self.y-Q.y)**2+(self.z-Q.z)**2)

#---------
		
class collection:    #Exercice 6
		"""Classe definissant une collection de points"""
		def __init__(self):
			self.points=list()
	
		def ajouter(self,p):  #Exercice 7
			self.points.append(p)
		
		def afficher(self):  #Exercice 8
			print"["
			for i in xrange(0,len(self.points)):
				self.points[i].Afficher()
			print"]"
		
		
		
		def appartient(self,c):   #Exercice 9
			d=self.points.distance(c)
			if (d<0.00001):return True
			else: return False
			
		def intersect(self, c):		#Exercice 10
			cp=collection()
			
			for p in self.points:
				if c.appartient(p):
				
					cp.add(p)
					
					
			return cp
		    			
		def moyenne(self):   #Exercice 11
			m=Point()
			
			x, y, z= 0, 0, 0
			
			for e in self.points:
				x += e.x
				y += e.y
				z += e.z
				
			taille=len(self.points)
			
			x/= taille
			y/= taille
			z/= taille
			
			m.x=x
			m.y=y
			m.z=z
			
			return m
			
			
		def ind_pg(self,n):     #Exercice 12
			ind=0
			for i in  xrange(n):
				if self.points[ind].inf_ou_egal(self.points[i]):
					ind=i
			return ind
			
		def trier(self):
			N=len(self.points)
			for i in xrange(0,N-1):
				ind=self.ind_pg(N-i)
				self.points[ind],self.points[N-i-1]=self.points[N-i-1],self.points[ind]
		
		
		
		
		
		
	
p=Point()
Q=Point()

p.Saisir()
Q.Saisir()

p.Afficher()
Q.Afficher()


print p.inf_ou_egal(Q)
print p.distance(Q)

nb=input("Combien de points voulez vous ?")
c=collection()

for i in range(nb):
	p=Point()
	p.Saisir()
	c.ajouter(p)
	print ""
	
c.afficher()

print""

c.moyenne().Afficher()

print""

c.trier()

c.afficher()






