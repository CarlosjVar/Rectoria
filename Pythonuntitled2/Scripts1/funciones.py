#Importación de librerías
from clases import *
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox
import pickle
import random

#Definición de funciones
def postularCandidato (listaMiembros,contC,entryCedula,validacion):
    x=entryCedula.get()
    if not re.match ("^[0-9]{9}$",x):
        validacion.config (text="Como cédula debe introducir una serie de 9 dígitos")
        return
    if contC[0]>=4:
        validacion.config (text="Ya se ha alcanzo el máximo de candidatos")
        return
    for objeto in listaMiembros:
        if objeto.getTipo()=="profesor":
            if objeto.getCedula()==int(x):
                objeto.setCandidato("2019-"+str(contC[0]+1))
                contC[0]=contC[0]+1
                validacion.config (text="Se ha postulado a "+objeto.getnombreCompleto()+" como "+str(contC[0])+"° candidato")
                guardarPadron (listaMiembros,contC)
                return
    validacion.config (text="No se ha encontrado ningún profesor con el número de cédula indicado")
    return


def crearAlAzar(entryCant,carreralist,AdminList,nombList,listaMiembros,validacion,contC):
    cant=entryCant.get()
    try:
        cant=int(cant)
        if cant<=0 or cant>100:
            validacion.config(text="La cantidad de miembros a generar debe ser un número entre 1 y 100")
            return
    except:
        validacion.config(text="La cantidad de miembros a generar debe ser un número entre 1 y 100")
        return
    MsgBox =messagebox.askquestion("Confirmación", "¿Esta seguro que desea generar "+str(cant)+" miembros?") 
    if MsgBox == 'yes':
        for i in range(cant):
            cedula=generarCedula()
            cont1=0
            while cont1<=(len(listaMiembros)-1):
                objeto=listaMiembros[cont1]
                if objeto.getCedula()==cedula:
                    cedula=generarCedula()
                    cont1=0
                else:
                    cont1+=1
            telefono=str(random.randint(1,9))
            for cont2 in range (7):
                telefono=telefono+str(random.randint(0,9))
            nombre=nombList[random.randint(0,13)]
            tipo=random.randint(1,3)
            if tipo==1:
                carne=str(random.randint(1,9))
                for cont3 in range  (9):
                    carne=carne+str(random.randint(0,9))
                carrera=carreralist[random.randint(0,4)]
                nuevo=Estudiante(int(cedula),nombre,int(telefono),int(carne))
                nuevo.setCarrera(carrera)
                listaMiembros.append(nuevo)
            elif tipo==2:
                publicaciones="Sin publicaciones registradas"
                nuevo=Profesor(int(cedula),nombre,int(telefono),publicaciones)
                listaMiembros.append(nuevo)
            else:
                puesto=AdminList[random.randint(0,3)]
                extension=str(random.randint(1,9))
                for cont4 in range(3):
                    extension=extension+str(random.randint(0,4))
                nuevo=Administrativo(cedula,nombre,int(telefono),puesto,int(extension))
                listaMiembros.append(nuevo)
        guardarPadron (listaMiembros,contC)
        validacion.config(text="Se han generado "+str(cant)+" miembros")
    return

def generarCedula ():
    cedula=str(random.randint(1,7))
    for cont1 in range(8):
        cedula=cedula+str(random.randint(0,9))
    return int(cedula)

def nuevoMiembro(carreralist,listaMiembros,x,y,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,a,tipo,infoError,contC):
    if tipo==1:
        z=entrycarn.get()
        if not re.match ("^[0-9]{10}$",z):
            infoError.config (text="Debe indicar un carnet válido para el alumno a registrar")
            return
        nuevo=Estudiante(x,y,a,z)
        b=carrera.get()
        if b not in carreralist:
            infoError.config (text="La carrera indicada debe escogerse de entre las opciones dadas")
            return
        if b=="":
            infoError.config (text="Debe indicar una carrera para el miembro a registrar")
            return
        nuevo.setCarrera(b)
        listaMiembros.append(nuevo)
    elif tipo==2:
        z=Publicaciones.get("1.0", "end-1c")
        if z=="":
            z="Sin publicaciones reistradas"
        nuevo=Profesor(x,y,a,z)
        listaMiembros.append(nuevo)
    else:
        z=puestspin.get()
        b=ExtEnt.get()
        if b=="" or z=="":
            infoError.config (text="Debe indicar un puesto y una extensión para el miembro a registrar")
            return
        nuevo=Administrativo(x,y,a,z,b)
        listaMiembros.append(nuevo)
    guardarPadron (listaMiembros,contC)
    infoError.config (text="Miembro registrado")
    return


def guardarPadron (listaMiembros,contC):
    with open("padrón.txt","wb") as f:
        pickle.dump(listaMiembros,f)
        f.close()
    with open("contador.txt","wb")as g:
        pickle.dump(contC,g)
        f.close()
    return

def confirmacionregistroNuevo(carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError,contC):
    MsgBox =messagebox.askquestion('Confirmación', '¿Esta seguro que desea registrar este miembro?') 
    if MsgBox == 'yes':
        auxnuevoMiembro (carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError,contC)
    return


    
def auxnuevoMiembro (carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError,contC):
    x=entryCed.get()
    y=entryNomb.get()
    a=entryTel.get()
    if y=="":
        infoError.config (text="Debe indicar un nombre para el miembro a registrar")
        return
    if not re.match ("^[0-9]{9}$",x):
        infoError.config (text="Como cédula debe introducir una serie de 9 dígitos")
        return
    x=int(x)
    for objeto in listaMiembros:
        if objeto.getCedula()==x:
           infoError.config (text="Ya existe un miembro registrado con la cédula indicada")
           return
    if not re.match ("^[0-9]{8}$",a):
        infoError.config (text="El número telefónico debe estar compuesto por 8 dígitos")
        return
    a=int(a)
    nuevoMiembro(carreralist,listaMiembros,x,y,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,a,tipo,infoError,contC)
    return
def generarVotacion(contC,listaMiembros,diccionarioVotos):
    for persona in listaMiembros:
        voto=random.randint(0,contC[0])
        persona.setVoto(voto)
    for i in range(contC[0]+1):
        diccionarioVotos[str(i)]=0
    keys=diccionarioVotos.keys()
    print(keys)
    for persona in listaMiembros:
        print("b")
        try:
            if persona.voto==0:
                diccionarioVotos["0"]+=1
            elif persona.voto==1:
                diccionarioVotos["1"] += 1
            elif persona.voto==2:
                diccionarioVotos["2"] += 1
            elif persona.voto==3:
                diccionarioVotos["3"] += 1
            elif persona.voto==4:
                diccionarioVotos["4"] += 1
        except:
            pass
    keys=diccionarioVotos.keys()
    for llave in keys:
        print(diccionarioVotos[llave])

    return diccionarioVotos
def analisisVotacion(diccionarioVotos,listaMiembros,contC):
    mayor=0
    ganador=0
    poblacion=contarPoblación(listaMiembros)
    for i in range(contC[0]):
        if diccionarioVotos[i]>mayor:
            mayor=diccionarioVotos[i]
            ganador=i







def contarPoblacion(listaMiembros):
    contP=0
    for persona in listaMiembros:
        contP+=1
    return contP

    

def infoCandidatos(listaMiembros):
    with open("Reporte.html","w",encoding="UTF-8") as reporte:
        reporte.write("<!DOCTYPE html>")
        reporte.write("<meta charset=UTF-16>")
        reporte.write("<head>")
        reporte.write("<style>")
        reporte.write("table, th, td {border: 1px solid black; border-collapse: collapse;}")
        reporte.write("</style>")
        reporte.write("</head>")
        reporte.write("<body>")
        reporte.write("<table border=1 align=center>")
        reporte.write("<caption>Candidatos para rector</caption")
        reporte.write("<tr><td>Cédula</td><td>Nombre Completo</td><td>Teléfono</td><td>Publicaciones</td></tr>")
        templateFila="""<tr>
        <td>"{p1}"</td>
        <td>"{p2}"</td>)<td>"{p3}"</td><td>"{p4}"</td></tr>"""
        for persona in listaMiembros:
            if persona.tipo=="profesor":
                if persona.candidato!="":
                    fila=templateFila.format(p1=persona.cedula,p2=persona.nombreCompleto,p3=persona.telefono,p4=persona.publicaciones)
                    reporte.write(fila)
        reporte.write("</table>")
        reporte.write("</body>")

