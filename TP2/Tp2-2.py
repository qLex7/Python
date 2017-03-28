# Tp2-2

m=input("montant")
if m<0:
	print"Vous n'avez pas de remise"
	exit()
if 100<m and m<500:
	print"Vous avez une remise de 5% \nPrix final",0.95*m,"euros"	
elif 500<=m and m<2500:
	print"Vous avez une remise de 15% \nPrix final",0.85*m,"euros"
elif 2500<=m:
	print"Vous avez une remise de 25% \nPrix final",0.75*m,"euros"
else:
	print "Vos achats sont trop bas pour beneficier d'une remise"

	
