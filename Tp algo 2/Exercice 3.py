#Algorithme tp2
#Exo 3

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
		print"(",self.x,self.y,self.z,")",

	def saisir (self):
		self.x=input("Entrez un x:")
		self.y=input("Entrez un y:")
		self.z=input("Entrez un z:")
	
P=Point()
Q=Point()
P.saisir()
Q.saisir()
P.afficher()
