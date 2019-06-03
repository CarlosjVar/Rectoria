#Importación de librerías
from clases import *
from tkinter import *
from tkinter import ttk
import re

#Definición de funciones
def nuevoMiembro(carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError):
    x=entryCed.get()
    y=entryNomb.get()
    a=entryTel.get()
    if y=="":
        infoError.config (text="Debe indicar un nombre para el miembro a registrar")
        return
    if not re.match ("[0-9]{9}",x):
        infoError.config (text="Como cédula debe introducir una serie de 9 dígitos")
        return
    for objeto in listaMiembros:
        if objeto.cedula==x:
            infoError.config (text="Ya existe un miembro con el número de cédula indicado")
        return
    if not re.match ("[0-9]{8}",a):
        infoError.config (text="El número telefónico debe estar compuesto por 8 dígitos")
        return
    x=int(x)
    a=int(a)
    if tipo==1:
        z=entrycarn.get()
        if z=="":
            infoError.config (text="Debe indicar un carnet para el alumno a registrar")
            return
        nuevo=Estudiante(x,y,a,z)
        b=carrera.get()
        if b not in carreralist:
            infoError.config (text="La carrera indicada debe escogerse de entre las opciones dadas")
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
    for objeto in listaMiembros:
        objeto.mostrar()
    return

