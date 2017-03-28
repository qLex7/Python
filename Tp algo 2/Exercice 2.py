#Algorithme tp2
#Exo 2

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
	
P=Point()
P.afficher()

