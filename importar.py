def interfaz(titulo,*arbitrarios):
	rayita="-"
	print ""
	print titulo.center(40," ")
	print rayita.center(40,"-")
	for i in arbitrarios:
		print i.center(38," ")
	print rayita.center(40,"-")
	print ""

