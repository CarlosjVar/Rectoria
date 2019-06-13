##################################################
#Creado por: Carlos Varela y Joseph Tenorio
#Fecha de creación: 09/06/2019
#Fecha de última modificación: 23:52 12/06/2019
#Versión: 3.7.3
###################################################
#Importación de librerías
import re
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

def separarListaImpares (plista):
    """"
    Funcionamiento: Dada una lista, devuelve otra lista conformada por los elementos
    en las posiciones impares de la lista original (contando desde cero)
    Entradas: plista (list)
    Salidas: Una lista con los elementos en posición impar
    """
    if plista==[]:
        return []
    if esPar(len(plista)):
        return [plista[0]]+separarListaImpares (plista[1:])
    else:
        return []+separarListaImpares (plista[1:])

def separarListaPares (plista):
    """"
    Funcionamiento: Dada una lista, devuelve otra lista conformada por los elementos
    en las posiciones pares de la lista original (contando desde cero)
    Entradas: plista (list)
    Salidas: Una lista con los elementos en posición par
    """
    if plista==[]:
        return []
    if not esPar(len(plista)):
        return [plista[0]]+separarListaPares (plista[1:])
    else:
        return []+separarListaPares (plista[1:])
    
def auxSepararLista (plista):
    """"
    Funcionamiento: Dada una lista, devuelve otra lista con dos sublistas,
    la primera con los elementos en la posición impar, y la segunda con los
    elementos en la posición par
    Entradas: plista (list)
    Salidas: Una lista que contiene dos sublistas de posiciones impares y pares
    """
    if plista==[]:
        return "La lista no debe estar vacía"
    else:
        return [separarListaImpares (plista),separarListaPares (plista)]
    
def auxsumaRecursiva(num):
    """"
    Funcionamiento: Valida entradas para la función suma recursiva
    Entradas: num (int)
    Salidas: sumaRecursiva(num)
    """
    try:
        int(num)
        if num>=0:
            return sumarecursiva(num)
        else:
            return "Debe ser un numero mayor o igual que 0"
    except:
        return "Debe ingresar un número entero"
def sumarecursiva(num):
    """"
    Funcionamiento: Dado un número, realiza la sumatoria desde el 0 hasta ese número y devuelve el resultado
    Entradas: num (int)
    Salidas: Un int que indica el resultado de la sumatoria
    """
    if num==0:
        return 0
    if num!=0:
        return num+sumarecursiva(num-1)

def auxPrimosEnRango(num1,num2):
    """"
    Funcionamiento: Valida entradas para la función PrimosEnRango
    Entradas: num1,num2 (int)
    Salidas: primosEnRango
    """
    try:
        int(num1)
        int(num2)
        if num2>num1:
            return primosEnRango(num1,num2)
        else:
            return "El segundo número no puede ser mayor al primero"
    except:
        return "Debe ingresar números enteros"
def primosEnRango(num1,num2):
    """"
    Funcionamiento: Dado 2 enteros, se calcula cuantos números primos existen en el intervalo de esos 2 números
    Entradas: num1,num2 (int)
    Salidas: Un int que indica la cantidad de números primos existentes
    """
    if num1==num2:
        if esPrimo(num1):
            return 1
        else:
            return 0
    elif num1<=num2:
        if esPrimo(num1):
            return 1+primosEnRango(num1+1,num2)
        else:
            return primosEnRango(num1+1,num2)
        
def esPrimo(num):
    """"
    Funcionamiento: Verifica si un número es primo o no
    Entradas: num1 (int)
    Salidas: True or False
    """
    if num < 1:
        return False
    elif num==1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
def auxDetectarAlternado(lista):
    """"
    Funcionamiento: Valida entradas para la funcion DetectarAlternado
    Entradas: lista(list)
    Salidas: DetectarAlternado
    """
    try:
        list(lista)
        if len(lista)==0:
            return "La lista no debe estar vacía"
        else:
            for elemento in lista:
                try:
                    int(elemento)
                except:
                    return "Los elementos de la lista deben ser enteros"
                return DetectarAlternado(lista)
    except:
        return "El elemento debe ser una lista"
def DetectarAlternado(lista):
    """"
    Funcionamiento: Detecta si los números en una lista alternan o no alternan
    Entradas: num1 (int)
    Salidas: True or False
    """
    if len(lista)==1:
        return True
    elif not esPar(abs(lista[0]-lista[1])):
        return DetectarAlternado(lista[1:])
    else:
        return False
def auxDuplicarElementos(lista,contador,listadummy):
    """"
    Funcionamiento: Valida entradas para la funcion duplicarElementosLista
    Entradas: lista(list) contador(int) y listadummy(list)
    Salidas: duplicarElementosLista
    """
    try:
        list(lista)
        if len(lista) == 0:
            return "La lista no debe estar vacía"
        else:
            for elemento in lista:
                try:
                    int(elemento)
                except:
                    return "Los elementos de la lista deben ser enteros"
            try:
                int(contador)
            except:
                return "El contador debe ser entero"
            return DetectarAlternado(lista)
    except:
        return "El elemento debe ser una lista"

def duplicarElementosLista(lista,contador,listadummy):
    """"
    Funcionamiento: Duplica los elementos de una lista
    Entradas: lista(list) contador(int) y listadummy(list)
    Salidas: Una lista con elementos duplicados
    """
    if contador==0:
        return sorted(listadummy)
    else:
        return duplicarElementosLista(lista,contador-1,lista+listadummy)

def auxSepararListas(lis, elemento, mainlist, lista):
    """"
    Funcionamiento: Valida entradas para la funcion separarListasElem
    Entradas: lis(list)elemento(str/int) mainlist y lista son listas vacías
    Salidas: separarListasElem
    """
    try:
        list(lis)
        if len(lis) == 0:
            return "La lista no debe estar vacía"
        else:
            return separarListasElem(lis, elemento, mainlist, lista)
    except:
        return "El elemento debe ser una lista"
def separarListasElem(lis, elemento, mainlist, lista):
    """"
    Funcionamiento: Separa elementos dado un separados
    Entradas: lis(list)elemento(str/int) mainlist y lista son listas vacías
    Salidas: lista con listas resultado de "splits"
    """
    if lis == []:
        if lista != []:
            mainlist.append(lista)
    else:
        if lis[0] != elemento:
            lista.append(lis[0])
        else:
            mainlist.append(lista)
            lista = []
        separarListasElem(lis[1:], elemento, mainlist, lista)
    return mainlist

    #P.P.
print("1:Determinar si dígito en posición es par")
num1=1234
pos1=3
print ("Las entradas fueron: "+str(num1)+" y "+str(pos1))
print ("Salida: "+str(auxEsParEnPosicion(num1,pos1)))
print ("***************************************")
print("2:Calcular sumatoria número de 0 a n")
print("-------ATENCION-------")
print("Las salidas van a diferir de las que se solicitaron en el enunciado y esto es debido a que el número 1 no es primo y en el enunciado este se contó como primo")
num=7
print("La entrada fue: "+str(num))
print("La salida fue: "+str((auxsumaRecursiva(num))))
print ("***************************************")
print("3:Determinar la cantidad de números primos en un rango")
numero1=1
numero2=15
print("Las entradas son:"+str(numero1)+" y "+str(numero2))
print("La salida fue:  "+str((auxPrimosEnRango(numero1,numero2))))
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
print("2:Detectar paridad o imparidad")
lista4=[2, "a", 4, 7]
print("La entrada fue: "+str(lista4))
print("La salida es: "+str(auxDetectarAlternado(lista4)))
print ("***************************************")
print("3:Separar elementos en posición par e impar")
lista2=[0,1,2,3,4,5,6,7,8]
print ("La entrada fue: "+str(lista2))
print ("Salida: "+str(auxSepararLista(lista2)))
print ("***************************************")
print("4:Dupicar elementos en una lista")
contador=3
print("Las entradas son: "+str(lista4)+"y "+str(contador)+"y una lista vacía")
print("La salida es: "+str(auxDuplicarElementos(lista4,contador,list())))
print ("***************************************")
print("5:Determinar si la lista es ascendente")
lista3=[1,10,100,100000,2,10000000]
print ("La entrada fue: "+str(lista3))
print ("Salida: "+str(esAscendente(lista3,0)))
print ("***************************************")
elemento="x"
lista6=[1,5,3,2,"x","x",5,6,4,"x",67,7,6]
listavacia=[]
listavacia2=[]
print("Las entradas son: "+str(elemento)+str(lista6)+"y 2 listas vacías para el correcto funcionamiento de la función")
print("La salida es: "+str(auxSepararListas(lista6, elemento, listavacia, listavacia2)))








