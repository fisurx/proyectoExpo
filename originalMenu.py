def interfaz(titulo,op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11):
	#la opcion 3 teiene que ir con dos espacios al principio
	opciones=[op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11]
	rayita="-"
	print ""
	print titulo.center(40," ")
	print rayita.center(40,"-")
	for i in opciones:
		print i.center(38," ")
	print rayita.center(40,"-")
	print ""

