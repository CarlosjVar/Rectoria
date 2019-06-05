#Importación de librerías
from clases import *
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox
import pickle 

#Definición de funciones
#lista1=["Hola","me","llamo","idiota","yoda","es","gay"]
#lista2=["Pene","Inserte","texto","random","por","favor","matenme"]
#matriz=[lista1,lista2]

def nuevoMiembro(carreralist,listaMiembros,x,y,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,a,tipo,infoError):
    if tipo==1:
        z=entrycarn.get()
        if not re.match ("[0-9]{10}",z):
            infoError.config (text="Debe indicar un carnet válido para el alumno a registrar")
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
    with open("padrón.txt","wb") as f:
        pickle.dump(listaMiembros,f)
        f.close()
    infoError.config (text="Miembro registrado")
    return

def confirmacionregistroNuevo(carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError):
    print("Llego a la confirmación")
    MsgBox =messagebox.askquestion('Confirmación', '¿Esta seguro que desea registrar este miembro?') 
    if MsgBox == 'yes':
        auxnuevoMiembro (carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError) 
    return 

    
def auxnuevoMiembro (carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError):
    print("Llego a la validación")
    x=entryCed.get()
    y=entryNomb.get()
    a=entryTel.get()
    if y=="":
        infoError.config (text="Debe indicar un nombre para el miembro a registrar")
        return
    if not re.match ("[0-9]{9}",x):
        infoError.config (text="Como cédula debe introducir una serie de 9 dígitos")
        return
    if not re.match ("[0-9]{8}",a):
        infoError.config (text="El número telefónico debe estar compuesto por 8 dígitos")
        return
    x=int(x)
    a=int(a)
    print("Llego al registro")
    nuevoMiembro(carreralist,listaMiembros,x,y,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,a,tipo,infoError)
    print("salió del registro")
    return
    
    

def infoCandidatos(listaMiembros):
    with open("Reporte.html","w",encoding="UTF-8") as reporte:
        reporte.write("<!DOCTYPE html>")
        reporte.write("<meta charset=UTF-16>")
        reporte.write("<body>")
        reporte.write("<table border=1 align=center>")
        reporte.write("<caption>Candidatos para rector</caption")
        reporte.write("<tr><td>Cédula</td><td>Nombre Completo</td><td>Teléfono</td><td>Publicaciones</td></tr>")
        templateFila="""<tr>
        <td>"{p1}"</td>
        <td>"{p2}"</td>)<td>"{p3}"</td><td>"{p4}"</td></tr>"""
        for persona in listaMiembros:
            if persona.tipo=="profesor":
                fila=templateFila.format(p1=persona.cedula,p2=persona.nombreCompleto,p3=persona.telefono,p4=persona.publicaciones)
                reporte.write(fila)
        reporte.write("</table>")
        reporte.write("</body>")

