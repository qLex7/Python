#Algorithme tp2
#Exo 4

class Point:
	"""Classe definissant un point par:
	- x
	- y
	- z"""
	def __init__(self):
		self.x=4.0
		self.y=1.0
		self.z=2.5
			
	def afficher (self):
		print"(",self.x,self.y,self.z,")"

	def saisir (self):
		self.x=input("Entrez un x:")
		self.y=input("Entrez un y:")
		self.z=input("Entrez un z:")
	def in_ou_egal(self,Q):
		q.x=3
		q.y=5
		q.y=7
		if(self.x<Q.x):
			return True
		if(self.x>Q.x):
			return False
		if(self.y<Q.y):
			return True
		if(self.y>Q.y):
			return False
		if(self.z<Q.z):
			return True
		if(self.z>Q.z):
			return False
		return True
	
P=Point()
P.afficher()
P.saisir()
P.afficher()


