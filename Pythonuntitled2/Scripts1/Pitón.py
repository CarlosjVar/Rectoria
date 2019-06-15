#Importación de librerías
from tkinter import *
from funciones import *
from tkinter import ttk
import pickle
import random
import re
from tkinter import messagebox


#Varibales Globales
nombList=["Mario","Alejandro","Carlos","Randall","Esteban","Laura","Maria","Gabriela","Kimberly","Sandra","Karla","Pablo","Luis","Sebastián"]
listaMiembros=[]
tipo=0
carreralist=["IC-Ingeniería en Computación","ATI-Administración en Tecnologías de la Información","E-Electrónica","AE-Administración de Empresas","CA-Ingeniería en Computadores"]
AdminList=["Secretaria","Asistente Administrativa","Director","Coordinador"]
contC=[0]
diccionarioVotos={}
añoVotacion=["0000"]
listaAños=["2019","2023","2027","2031","2035","2039","2043"]

##Funciones Botones
def cerrarVentana(principal):
    principal.lift()
def confirmacionCandidato(listaMiembros,contC,entryCedula,validacion2,generarV):
    MsgBox = messagebox.askquestion('Confirmación', '¿Esta seguro que desea postular a esta persona?')
    if MsgBox == 'yes':
        return postularCandidato(listaMiembros,contC,entryCedula,validacion2,generarV)
    else:
        return
def postularMiembro(principal):
    postularM=Tk()
    postularM.attributes("-toolwindow", 1)
    postularM.protocol("WM_DELETE_WINDOW", cerrarVentana(principal))
    postularM.geometry("340x160")
    postularM.focus()
    postularM.title("Postular candidato")
    entryCedula=Text(postularM,height=2, width=20)
    entryCedula.place(x=125,y=26)
    labelCedula=Label(postularM,text="Cédula ")
    labelCedula.place(x=45,y=26)
    validacion2=Label(postularM,text="")
    validacion2.place(x=180,y=126,anchor="center")
    postular=Button(postularM, text="Buscar",width=15,relief=GROOVE,command=lambda: confirmacionCandidato(listaMiembros,contC,entryCedula,validacion2,generarV))
    postular.place(x=45,y=80)
    limpiar = Button(postularM, relief=GROOVE, text="Limpiar", width=15,command=lambda: botonLimp([entryCedula]))
    limpiar.place(x=180,y=80)
    postularM.mainloop()



def generarMiembro(principal):
    generarM=Tk()
    generarM.attributes("-toolwindow", 1)
    generarM.protocol("WM_DELETE_WINDOW", cerrarVentana(principal))
    generarM.geometry("410x170")
    generarM.focus()
    generarM.title("Genenerar miembros")
    labtit=Label(generarM,text="Carga automática aleatoria")
    labtit.grid(row=0,column=0,padx=30,pady=10 ,sticky=W)
    entryCant=Entry(generarM,width=25)
    entryCant.grid(row=1,column=1,sticky=W)
    labelCant=Label(generarM,text="Cantidad de miembros a generar: ")
    labelCant.grid(row=1,column=0,padx=30,sticky=W)
    validacion=Label(generarM,text="")
    validacion.place(x=210,y=120,anchor="center")
    generar=Button(generarM,relief=GROOVE, text="Generar miembros",command=lambda: crearAlAzar(entryCant,carreralist,AdminList,nombList,listaMiembros,validacion,contC))
    generar.place(x=90,y=80)
    limpiar = Button(generarM, relief=GROOVE, text="Limpiar", width=15, command=lambda: botonLimp([entryCant]))
    limpiar.place(x=220,y=80)
    generarM.mainloop()

def registrarMiembro(principal):
    carreralist=["","IC-Ingeniería en Computación","ATI-Administración en Tecnologías de la Información","E-Electrónica","AE-Administración de Empresas","CA-Ingeniería en Computadores"]
    registM=Tk()
    registM.protocol("WM_DELETE_WINDOW", cerrarVentana(principal))
    registM.attributes("-toolwindow", 1)
    registM.geometry("460x450")
    registM.focus()
    registM.title("Registrar Miembro")
    cedlab=Label(registM,text="Cédula")
    cedlab.grid(row=0,column=0,sticky=W,padx = 20,pady = 5)
    entryCed=Entry(registM,width=20)
    entryCed.grid(row=0,column=1,sticky=W)
    NombrLab=Label(registM,text="Nombre Completo")
    NombrLab.grid(row=1,column=0,sticky=W,padx = 20,pady = 3)
    entryNomb = Entry(registM, width=40)
    entryNomb.grid(row=1,column=1,sticky=W)
    TelLab=Label(registM,text="Teléfono")
    TelLab.grid(row=2,column=0,sticky=W,padx = 20,pady = 3)
    entryTel=Entry(registM,width=20)
    entryTel.grid(row=2,column=1,sticky=W)
    ttk.Separator(registM).place(x=0, y=163,relwidth=1)
    carnLab=Label(registM,text="Carnet")
    carnLab.grid(row=6,column=0,sticky=W,padx = 20,pady=5)
    entrycarn = Entry(registM, width=40)
    entrycarn.grid(row=6, column=1, sticky=W)
    carreraLab=Label(registM,text="Carrera")
    carreraLab.grid(row=7,column=0,sticky=W,padx = 20)
    variable = StringVar()
    variable.set(carreralist[0])
    carrera=ttk.Combobox(registM,values=carreralist,width=30)
    carrera.grid(row=7,column=1,sticky=W,pady = 3)
    ttk.Separator(registM).place(x=0,y=220,relwidth=1)
    PublLab=Label(registM,text="Publicaciones")
    PublLab.grid(row=8,column=0,sticky=W,padx=20,pady=5)
    Publicaciones=Text(registM,width=30,heigh=4)
    Publicaciones.grid(row=8,column=1,sticky=W,pady=7)
    ttk.Separator(registM).place(x=0, y=300, relwidth=1)
    puestLab=Label(registM,text="Puesto")
    puestLab.grid(row=9,column=0,sticky=W,padx=20,pady=5)
    puestspin=Spinbox(registM,values=AdminList)
    puestspin.grid(row=9,column=1,sticky=W)
    ExtLab=Label(registM,text="Extensión")
    ExtLab.grid(row=10,column=0,sticky=W,padx=20)
    ExtEnt=Entry(registM,width=20)
    ExtEnt.grid(row=10,column=1,sticky=W)
    ttk.Separator(registM).place(x=0, y=360, relwidth=1)
    infoError=Label(registM,text="")
    infoError.place(x=145,y=365)
    registrar=Button(registM,relief=GROOVE,text="Registrar",width=20,command= lambda: confirmacionregistroNuevo(carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError,contC))
    registrar.place(x=70,y=400)
    limpiar=Button(registM,relief=GROOVE,text="Limpiar",width=20,command=lambda :botonLimp([entryCed,entryNomb,entrycarn,Publicaciones,entryTel,ExtEnt]))
    limpiar.place(x=240,y=400)
    v=IntVar()
    Est=Radiobutton(registM, text="Estudiante", variable=v, value=1,command=lambda:radioEST(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Est.grid(row=3,column=0,sticky=W,padx = 20)
    Prof=Radiobutton(registM, text="Profesor", variable=v, value=2,command=lambda:radioProf(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Prof.grid(row=4,column=0,sticky=W,padx = 20)
    Admi=Radiobutton(registM, text="Administrativo", variable=v, value=3,command=lambda:radioAdmi(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Admi.grid(row=5,column=0,sticky=W,padx = 20)
    Est.invoke()
    mostrar=Button(registM,relief=GROOVE, text="Muestra todo en consola",command=lambda: mostrarTodo(listaMiembros))
    mostrar.place(x=460,y=1)
    registM.mainloop()

def mostrarTodo (listaMiembros):
    for objeto in listaMiembros:
        objeto.mostrar()
    return 

##Auxiliares de botones
def radioEST(a,b,c,d,e):
    global tipo
    tipo=1
    botonLimp([c, d, e])
    a.config(state=NORMAL)
    b.config(state=NORMAL)
    c.config(state=DISABLED)
    d.config(state=DISABLED)
    e.config(state=DISABLED)

def radioProf(a,b,c,d,e):
    global tipo
    tipo=2
    botonLimp([a, b, d, e])
    a.config(state=DISABLED)
    b.config(state=DISABLED)
    c.config(state=NORMAL)
    d.config(state=DISABLED)
    e.config(state=DISABLED)

def radioAdmi(a,b,c,d,e):
    global tipo
    tipo=3
    botonLimp([a, b, c])
    a.config(state=DISABLED)
    b.config(state=DISABLED)
    c.config(state=DISABLED)
    d.config(state=NORMAL)
    e.config(state=NORMAL)
    
def botonLimp(lista):
    for widget in lista:
        try:
            widget.delete(0, END)
        except:
            widget.delete('1.0', END)
            
def genVota(principal,listaAños):
    genP=Tk()
    genP.focus()
    genP.attributes("-toolwindow", 1)
    genP.geometry("370x130")
    genP.protocol("WM_DELETE_WINDOW", cerrarVentana(principal))
    genP.title("Generar votación")
    genP.attributes("-toolwindow", 1)
    label=Label(genP,text="Indicar año")
    label.grid(row=0,column=0,padx=40,pady=20,sticky=W)
    años=ttk.Combobox(genP, values=listaAños, width=30)
    años.grid(row=0,column=1,sticky=W,pady=20)
    generar=Button(genP,width=20,relief=GROOVE,text="Elegir",command=lambda: confirmarVotacion(diccionarioVotos,contC,listaMiembros,añoVotacion,años))
    generar.place(x=50,y=80)
    regresar=Button(genP,relief=GROOVE,width=20,text="Regresar",command=lambda: destruir(genP))
    regresar.place(x=210,y=80)
    genP.mainloop()
    
def destruir(ventana):
    ventana.destroy()
    
def confirmarVotacion (diccionarioVotos,contC,listaMiembros,añoVotacion,años):
    MsgBox = messagebox.askquestion('Confirmación', '¿Esta seguro que desea generar una nueva votación?')
    if MsgBox == 'yes':
        añoVotacion[0]=años.get()
        return generarVotacionFinal(diccionarioVotos,listaMiembros,contC)
    else:
        return

def reportes(principal):
    principal = Tk()
    principal.focus()
    principal.protocol("WM_DELETE_WINDOW", cerrarVentana(principal))
    principal.geometry("230x190")
    principal.title("Elecciones TEC")
    principal.attributes("-toolwindow", 1)
    listaC = Button(principal,relief=GROOVE, text="Lista de Candidatos", command= lambda: infoCandidatos(listaMiembros,añoVotacion))
    cantidadV = Button(principal,relief=GROOVE, text="Cantidad de votantes por candidato", command=lambda:cantidadporcandidato(listaMiembros,añoVotacion,diccionarioVotos))
    seguidoresC = Button(principal,relief=GROOVE, text="Seguidores por candidato", command=None)
    votRol = Button(principal, relief=GROOVE,text="Votante por rol", command=None)
    novot = Button(principal, relief=GROOVE,text="Lista de no votantes", command=None)
    listaC.pack(padx=10, pady=5, side="top", fill="x")
    cantidadV.pack(padx=10, pady=5, side="top", fill="x")
    seguidoresC.pack(padx=10, pady=5, side="top", fill="x")
    votRol.pack(padx=10, pady=5, side="top", fill="x")
    novot.pack(padx=10, pady=5, side="top", fill="x")
    principal.mainloop()

##Tkinter
principal=Tk()
principal.geometry("230x190")
principal.attributes("-toolwindow", 1)
principal.title("Elecciones TEC")
try:
    with open("padrón.txt","rb") as f:
        listaMiembros=pickle.load(f)
    with open("contador.txt","rb")as g:
        contC=pickle.load(g)
    msg=messagebox.showinfo("Padrón","Se ha cargado un padrón guardado anteriormente")
    f.close()
except:
    relleno=0
registrarM=Button(principal,relief=GROOVE,text="Registrar Miembro",command=lambda:registrarMiembro(principal))
cargarDatos=Button(principal,relief=GROOVE,text="Cargar Datos",command=lambda:generarMiembro(principal))
registrarC=Button(principal,relief=GROOVE,text="Registrar Candidato",command=lambda:postularMiembro(principal))
generarV=Button(principal,relief=GROOVE,text="Generar Votación",command=lambda:genVota(principal))
reporte=Button(principal,relief=GROOVE,text="Reportes",command=lambda:reportes(principal))
registrarM.pack(padx=10, pady=5,side="top", fill="x")
cargarDatos.pack(padx=10, pady=5,side="top", fill="x")
registrarC.pack(padx=10, pady=5,side="top", fill="x")
generarV.pack(padx=10, pady=5,side="top", fill="x")
reporte.pack(padx=10, pady=5,side="top", fill="x")
if contC[0]==0:
    generarV.config(state=DISABLED)

principal.mainloop()
