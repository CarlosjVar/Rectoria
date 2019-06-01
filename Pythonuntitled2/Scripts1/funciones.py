#Importación de librerías
from clases import *
from tkinter import *
from tkinter import ttk

#Definición de funciones
def nuevoMiembro(listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo):
    if tipo==1:
        x=entryCed.get()
        y=entryNomb.get()
        z=entrycarn.get()
        a=entryTel.get()
        nuevo=Estudiante(x,y,a,z)
        b=carrera.get()
        nuevo.setCarrera(b)
        listaMiembros.append(nuevo)
    elif tipo==2:
        x=entryCed.get()
        y=entryNomb.get()
        z=Publicaciones.get("1.0", "end-1c")
        a=entryTel.get()
        nuevo=Profesor(x,y,a,z)
        listaMiembros.append(nuevo)
    else:
        x=entryCed.get()
        y=entryNomb.get()
        a=entryTel.get()
        z=puestspin.get()
        b=ExtEnt.get()
        nuevo=Administrativo(x,y,a,z,b)
        listaMiembros.append(nuevo)
    print (len(listaMiembros))
    return

