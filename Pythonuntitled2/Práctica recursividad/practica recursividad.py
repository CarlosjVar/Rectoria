##################################################
#Creado por: Carlos Varela y Joseph Tenorio
#Fecha de creación: 09/06/2019
#Fecha de última modificación: 
#Versión: 3.7.3
###################################################

#Definicicón de funciones
def esParEnPosicion (pnum,cont,pos):
    """"
    Funcionamiento: Determina si el dígito en una determinada posición del numero
    dado es par
    Entradas: pnum (int),cont (int), pos(int)
    Salidas: True en caso de ser par, False en caso contrario
    """
    if cont==pos:
        dig=pnum%10
        if esPar(dig):
            return True
        else:
            return False
    else:
        return esParEnPosicion((pnum//10),(cont+1),pos)

def auxEsParEnPosicion (pnum,pos):
    """"
    Funcionamiento: Validar las entradas de la función esParEnPosicion
    Entradas: pnum (str/int) ,pos (int/str)
    Salidas: El resultado de esParEnPosicion(num,1,pos)
    """
    try:
        num=int(pnum)
        pos=int(pos)
        if pos>=1 and pos<=9:
            if pos<=len(str(num)):
                return esParEnPosicion(num,1,pos)
            else:
                return "La posición indicada excede la cantidad de dígitos del número"
        else:
            return "La posición a analizar debe ser un entero entre 1 y 9"
    except:
        return "El numero al cual buscarle pares y la posición a buscar deben ser enteros"

def esPar(pnum):
    """"
    Funcionamiento: Determina si un número es par 
    Entradas: pnum (int)
    Salidas: True si es par, False en caso contrario
    """
    if pnum%2==0:
        return True
    else:
        return False

def esAnnoBisiesto (panno):
    """"
    Funcionamiento: Determina si un año es bisiesto
    Entradas: panno (int)
    Salidas: True si es bisiesto, False en caso contrario 
    """
    if (panno%100)!=0 or (panno%400)==0:
        if panno%4==0:
            return True
        else:
            return False
    else:
        return False

def rangoEsAnnoBisiesto (pnum1,pnum2,cont):
    """"
    Funcionamiento: Determina la cantidad de años bisiestos en un lapso dado
    Entradas: pnum1 (int), pnum2 (int), cont (int)
    Salidas: cont (int,cantidad de años encontrados) 
    """
    if pnum1==pnum2:
        if esAnnoBisiesto(pnum1):
            cont+=1
        return cont
    else:
        if esAnnoBisiesto(pnum1):
            cont+=1
        return rangoEsAnnoBisiesto ((pnum1+1),pnum2,cont)

def auxrangoEsAnnoBisiesto(panno1,panno2):
    """"
    Funcionamiento: Valida las entradas de la función rangoEsAnnoBisiesto
    Entradas: panno1 (str/int), panno2 (str/int)
    Salidas: La salida de rangoEsAnnoBisiesto (anno1,anno2,0)
    """
    if str(panno1).isdigit() and str(panno2).isdigit():
        anno1=int(panno1)
        anno2=int(panno2)
        if anno1<anno2:
            return rangoEsAnnoBisiesto (anno1,anno2,0)
        else:
            return "El año de inicio debe ser menor al año de finalización"
    else:
        return "Los años ingresados deben ser enteros positivos"
    
def auxColonizarMarte (pnum):
    """"
    Funcionamiento: Valida las entradas de colonizarMarte 
    Entradas: pnum(int)
    Salidas: La salida de colonizarMarte (pnum)
    """
    if str(pnum).isdigit():
        num=int(pnum)
        if num<0:
            return "La generación ingresada debe ser un número natural"
        else:
            return colonizarMarte (num)
    else:
        return "La generación ingresada debe ser un número natural"

def colonizarMarte (pnum):
    """"
    Funcionamiento: Determina la cantidad de habitantes en la colonia marciana
    Entradas: pnum(int)
    Salidas: Un entero indicando la cantidad de habitantes
    """
    if pnum==0:
        return 27
    else:
        return (colonizarMarte(pnum-1)//2)*3


def insertarEnReferencia (pele,pref,lista,cont):
    """"
    Funcionamiento: Inserta el elemento pele cada vez que se encuentra a pref en lista
    Entradas: pele (elemento a insertar), pref (elemento a buscar), lista (list)
    cont(int)
    Salidas: Una lista con las modificaciones especificadas
    """
    if cont==len(lista):
        return lista
    if lista[cont]==pref:
        lista.insert(cont+1,pele)
        cont+=2
    else:
        cont+=1
    return insertarEnReferencia (pele,pref,lista,cont)

def esAscendente (lista,cont):
    """"
    Funcionamiento: Determina si los elementos numéricos de una lista son ascendentes o no
    Entradas: lista(list), cont (int)
    Salidas: True si es ascendente, False en caso contrario
    """
    if cont==len(lista)-1:
        return True
    if lista[cont]>lista[cont+1]:
        return False
    else:
        return esAscendente(lista,cont+1)


#P.P.
print("1:Determinar si dígito en posición es par")
num1=1234
pos1=3
print ("Las entradas fueron: "+str(num1)+" y "+str(pos1))
print ("Salida: "+str(auxEsParEnPosicion(num1,pos1)))
print ("***************************************")
print("4:Determinar cantidad de años bisiestos en un rango")
anno1=2000
anno2=2025
print ("Las entradas fueron: "+str(anno1)+" y "+str(anno2))
print ("Salida: "+str(auxrangoEsAnnoBisiesto(anno1,anno2)))
print ("***************************************")
print ("5: Cantidad de habitantes por generación")
gen=4
print ("La entrada fue: "+str(gen))
print ("Salida: "+str(auxColonizarMarte(gen)))
print ("***************************************")
print ("1: Insertar elemento despúes de referencia en lista")
ref=4
ele=2
lista=[1,4,1,1,1,4,1]
print ("Las entradas fueron: ele="+str(ele)+", ref="+str(ref)+", lista="+str(lista))
print ("Salida: "+str(insertarEnReferencia (ele,ref,lista,0)))
print ("***************************************")
#print("3:Separar elementos en posición par e impar")
#lista2=[1,2,3,4,5,6,7,8,9]
#print ("La entrada fue: "+str(lista2))
#print ("Salida: "+str(separarLista(lista2)))
#print ("***************************************")
print("5:Determinar si la lista es ascendente")
lista3=[1,10,100,100000,2,10000000]
print ("La entrada fue: "+str(lista3))
print ("Salida: "+str(esAscendente(lista3,0)))
print ("***************************************")







