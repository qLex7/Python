#Algorithme tp2
#Exo 5
from math import*

class Point:
	"""Classe definissant un point par:
	- x
	- y
	- z"""
	def __init__(self,x,y,z):
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
	
	def distance(self,A):
		return sqrt((self.x-A.x)**2+(self.y-A.y)**2+(self.z-A.z))
		print A.distance(B)
	
P=Point(4.0,1.0,2.5)
P.afficher()
P.saisir()
P.afficher()
d=P.distance(A)

