#-------------------------------------------vars---------------------------------------------------#
import random 
option=0
carga=0
opSub=0
opSub1=0
listados=0
mayorCien=0
lista=[]
#----------------------------------------functions-------------------------------------------------#
def interfaz(titulo,*arbitrarios):
    rayita="-"
    print " "
    print titulo.center(40," ")
    print rayita.center(40,"-")
    for i in arbitrarios:
        print i.center(38," ")
    print rayita.center(40,"-")
    print " "

def cargar():
	lalista=raw_input("Ingrese los numeros: ")
        lalista=lalista.split(",")
        contador=0
        for i in lalista:
            if i.isdigit()==False or i.isalpha()==True:
                contador=contador+1
        if contador>=1:
            print "Por favor ingrese solo numeros."
            return []
        else:
            carga=1
            return map(int,lalista)

def comprobInt(texto): 
    string=raw_input(texto)
    error=0
    for i in string: 
        if i.isdigit()==False or i.isalpha()==True:
            error=error+1
    if error>=1:
        print "Por favor ingrese solo numeros."
        return 0
    else:
        return int(string)
        

def listar(listas):
    for i in range(len(lista)):
            print lista[i]
    

def posiciones(listaa,a,b):
        if opSub==a: 
            print listaa
            start=int(raw_input("Ingrese el inicio: "))
            end=int(raw_input("Ingrese el final: "))
            print listaa[start:end]

        if opSub==b:
            numero=int(raw_input("Ingrese el numero que desea buscar: "))
            if numero in listaa:
                print ""
                print "La posicion del numero %d es %d" %(numero,listaa.index(numero))

            else:
                print "El numero ingresado no se encuentra en la lista."

def realistar(listaa):
	listar(lista)


def mayor(listaa):
	mayor=0
	for i in listaa:
		if i>mayor:
			mayor=i
	return mayor

def plurSing(bandera,parametro1,parametro2): 
    if bandera>1 and bandera<99:
        print "Entre",parametro1,"y",parametro2,"hay",bandera,"numeros."
    if bandera==1:
        print "Entre",parametro1,"y",parametro2,"solo hay",bandera,"numero."
    if bandera==0:        
        print "Entre",parametro1,"y",parametro2,"no hay ningun numero."
    

def rangos(lista,mayorCien):
	treinta=0
	sesenta=0
	noventa=0
	cien=0
	for i in lista:
		if i>=1 and i<=30:
			treinta=treinta+1
		if i>=31 and i<=60:
			sesenta=sesenta+1
		if i>=61 and i <=90:
			noventa=noventa+1
		if i>=91 and i<=100:
			cien=cien+1
                if i>=101:
                    mayorCien=mayorCien+1

        if opSub1==1:
            plurSing(treinta,1,30)
        if opSub1==2:
            plurSing(sesenta,31,60)
        if opSub1==3:
            plurSing(noventa,61,90)
        if opSub1==4:
            plurSing(cien,91,100)
        if opSub1==5:
             if mayorCien>=1:
                 print "Hay",mayorCien,"numeros mayores a cien."
             if mayorCien==1:
                 print "Solo hay",mayorCien,"numero mayor a cien."
             if mayorCien==0:
                print "No hay ningun numero mayor a cien."

         


def modificar(lista,new,ubicacion):
        lista[ubicacion]=new
    


def randm(listaa):
	rand=random.choice(listaa)
        return rand

def sumatoria(listaa):
	suma=0
	for i in listaa:
		suma=suma+i
	return suma

#--------------------------------------script's body-----------------------------------------------#
while option<11:
    
	interfaz("MENU","1.Cargar","2.Listar","   3.Recargar","   4.Realistar","     5.Posiciones","         6.Busqueda mayor","            7.Modificar un valor","8.Rangos","9.Random","    10.Promedio.", "11.Salir")
        
	#option=int(raw_input("Ingrese una opcion en pantalla: "))
        option=comprobInt("Ingrese una opcion en pantalla: ")


       
        if option<=11:       
            if option==1:
                if carga==1:
                        valores=raw_input("Ingrese mas valores para agregar: ").split(",")	
                        contadorX=0
                        for i in valores:
                           if i.isdigit()==False:
                                contadorX=contadorX+1

                        if contadorX>=1:
                            print "Por favor ingrese solo numeros."
                       
                        else:
                            valor=map(int,valores)
                            lista=lista+valores
                else:
                    lista=cargar()
                    if len(lista)>=1:  
                        carga=1    

            if len(lista)>=1:

                if option==2:          
                    if listados==0:
                            listar(lista)
                            listados=1
                    else:
                            print "Ya utilizo esta accion, por favor use ralistar."
                if option==3:
                    lista=cargar()

                if option==4:
                    listar(lista)
        
                if option==5:
                    opSub=0
                    while opSub<3:
                        interfaz("Posiciones","1.Posicion por distancia", "2.Posicion por busqueda", "3.Salir")
                        opSub=comprob("Ingrese una opcion: ")
                        posiciones(lista,1,2)

                if option==6:
                        maxim=mayor(lista)
                        print "El mayor numero es %d"%(maxim)
        
                if option==7:
                        print lista
                        posicion=int(raw_input("Ingrese la ubicacion: "))
                        valor=int(raw_input("Ingrese el nuevo numero: "))
                        modificar(lista,valor,posicion)
                        print lista

                if option==8:
                    opSub1=0
                    while opSub1<6:
                        interfaz("Rangos","1.Rango entre 1 y 30","2.Rango entre 30 y 60","3.Rango entre 60 y 90","4.Rango entre 90 y 100","5.Mayores a cien","6.Salir" )
                        opSub1=comprob("Ingrese una opcion en pantalla: ")
                        rangos(lista,mayorCien)
                
                if option==9:
                        random=randm(lista)
                        print random

                if option==10:
                        total=sumatoria(lista)
                        promedio=total/len(lista)
                        print "La sumatoria de los numeros ingresados es ", total
                        print "El proemdio de los numeros ingresados es ", promedio
            
                    
            if option>=2 and option<=10 and len(lista)==0:
                print "No se puede ingresar a estas opciones sin antes cargar los datos."
        else:
            print "Ingreso un numero no valido, reinicie el programa."
