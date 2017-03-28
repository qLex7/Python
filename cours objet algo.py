class date:
	def __init__(self):
		self.j=j
		self.m=m
		self.a=a

	def afficher(self):
		print self.j,"/",self.m,"/",self.a,

	def anterieure(self,d):
		if(self.a<d.a):return True
		elif (self.a>d.a):return False
		if(self.m<d.m):return True
		elif (self.m>d.m):return False
		if(self.j<d.j):return True
		elif (self.j>d.j):return False

	def saisir(self):
		s=raw_input("Entrez une date")
		r=s.rsplit("/")
		self.j=int(r[0])
		self.m=int(r[1])
		self.a=int(r[2])

class ingredient:
	def __init__(self,nom"rien",Q=0):
		self.nom=nom
		self.Q=Q

	def afficher(self):
		print self.nom,":",self.unite

	def saisir(self):
		self.nom=raw_input("Entrez un nom")
		self.Q=input("Entrez la quantité")
		self.unite=raw_input("Entrez l'unite:")


class pa:
	def __init__(self):
		self.nom="rien"
		self.marque="rien"
		self.ref="rien"
		self.dp=date()
		self.de=date()

		self.li=[]

	def saisir(self):
		self.nom=raw_input("Entrez un nom:")
		self.marque=raw_input("Entrez une marque:")
		self.ref=raw_input("Entrez une reference:")
		self.dp.saisir()
		self.de.saisir()

		nbi=input("Entrez le nbre d'ingredients:")
		for i in xrange(nbi):
			i=ingredient()
			i.saisir()
			self.li.append(i)

	def afficher(self):
		print "le nom:",self.nom
		print "la marque:",self.marque
		print "la reference",self.ref
		print "la date de production",self.dp.afficher()
		print "la date d expiration",self.de.afficher()

		for i in self.li:
			i.afficher()
			print 

class magasin:
	def __init__(self):
		self.PA=[]

	def add(self, pa):
		self.PA.append(pa)

	def vendre(self, ref):
		nbp=len(self.PA)
		for i xrange(nbp):
			if self.PA([i].ref==ref):
				del(self.PA[i])
				break

	def delete(self, d1):
		nbp=len(self.PA)
		for i xrange(nbp):
			if da.anterieure(self.PA[i].de)):
				del(self.PA[i])
				break
		


d1=date(12,12,2016)
d1.afficher()
print''
d2=date()
d2.afficher()

if(d1.anterieure(d2)==True):
	print"d1<d2"
else:
	print"d1>d2"

I=ingredient("eau",150,"cl")
I.afficher()

d3=date()
d3.saisir()
d3.afficher()

A=pa()
A.saisir()
A.afficher()






