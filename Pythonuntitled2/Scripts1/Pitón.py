#Importación de librerías
from tkinter import *
from funciones import *
from tkinter import ttk

#Varibales Globales
listaMiembros=[]
tipo=0
carreralist=["IC-Ingeniería en Computación","ATI-Administración en Tecnologías de la Información","E-Electrónica","AE-Administración de Empresas","CA-Ingeniería en Computadores"]
AdminList=["Secretaria","Asistente Administrativa","Director","Coordinador"]

##Funciones Botones
def registrarMiembro():
    carreralist=["","IC-Ingeniería en Computación","ATI-Administración en Tecnologías de la Información","E-Electrónica","AE-Administración de Empresas","CA-Ingeniería en Computadores"]
    registM=Tk()
    registM.geometry("460x450")
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
    infoError=Label(registM,text="Aquí van a ir las validaciones")
    infoError.place(x=145,y=365)
    registrar=Button(registM,text="Registrar",width=20,command= lambda: confirmacionregistroNuevo(carreralist,listaMiembros,entryCed,entryNomb,entrycarn,Publicaciones,ExtEnt,carrera,puestspin,entryTel,tipo,infoError))
    registrar.place(x=70,y=400)
    limpiar=Button(registM,text="Limpiar",width=20,command=lambda :botonLimp(entryCed,entryNomb,entrycarn,Publicaciones,entryTel,ExtEnt))
    limpiar.place(x=240,y=400)
    v=IntVar()
    Est=Radiobutton(registM, text="Estudiante", variable=v, value=1,command=lambda:radioEST(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Est.grid(row=3,column=0,sticky=W,padx = 20)
    Prof=Radiobutton(registM, text="Profesor", variable=v, value=2,command=lambda:radioProf(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Prof.grid(row=4,column=0,sticky=W,padx = 20)
    Admi=Radiobutton(registM, text="Administrativo", variable=v, value=3,command=lambda:radioAdmi(carrera,entrycarn,Publicaciones,puestspin,ExtEnt))
    Admi.grid(row=5,column=0,sticky=W,padx = 20)
    Est.invoke()
    mostrar=Button(registM, text="Muestra todo en consola",command=lambda: mostrarTodo(listaMiembros))
    mostrar.place(x=460,y=1)
    registM.mainloop()

def mostrarTodo (listaMiembros):
    for objeto in listaMiembros:
        objeto.mostrar()
    return 

def radioEST(a,b,c,d,e):
    global tipo
    tipo=1
    a.config(state=NORMAL)
    b.config(state=NORMAL)
    c.config(state=DISABLED)
    d.config(state=DISABLED)
    e.config(state=DISABLED)

def radioProf(a,b,c,d,e):
    global tipo
    tipo=2
    a.config(state=DISABLED)
    b.config(state=DISABLED)
    c.config(state=NORMAL)
    d.config(state=DISABLED)
    e.config(state=DISABLED)

def radioAdmi(a,b,c,d,e):
    global tipo
    tipo=3
    a.config(state=DISABLED)
    b.config(state=DISABLED)
    c.config(state=DISABLED)
    d.config(state=NORMAL)
    e.config(state=NORMAL)
    
def botonLimp(a,b,c,d,e,f):
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0,END)
    d.delete('1.0',END)
    e.delete(0,END)
    f.delete(0,END)

def reportes():
    principal = Tk()
    principal.geometry("230x190")
    principal.title("Elecciones TEC")
    principal.attributes("-toolwindow", 1)
    listaC = Button(principal, text="Lista de Candidatos", command= lambda: infoCandidatos(listaMiembros))
    cantidadV = Button(principal, text="Cantidad de votantes por candidato", command=None)
    seguidoresC = Button(principal, text="Seguidores por candidato", command=None)
    votRol = Button(principal, text="Votante por rol", command=None)
    novot = Button(principal, text="Lista de no votantes", command=None)
    listaC.pack(padx=10, pady=5, side="top", fill="x")
    cantidadV.pack(padx=10, pady=5, side="top", fill="x")
    seguidoresC.pack(padx=10, pady=5, side="top", fill="x")
    votRol.pack(padx=10, pady=5, side="top", fill="x")
    novot.pack(padx=10, pady=5, side="top", fill="x")
    principal.mainloop()

##Tkinter
principal=Tk()
principal.geometry("230x190")
principal.title("Elecciones TEC")
registrarM=Button(principal,text="Registrar Miembro",command=registrarMiembro)
cargarDatos=Button(principal,text="Cargar Datos",command=None)
registrarC=Button(principal,text="Registrar Candidato",command=None)
generarV=Button(principal,text="Generar Votación",command=None)
reporte=Button(principal,text="Reportes",command=reportes)
registrarM.pack(padx=10, pady=5,side="top", fill="x")
cargarDatos.pack(padx=10, pady=5,side="top", fill="x")
registrarC.pack(padx=10, pady=5,side="top", fill="x")
generarV.pack(padx=10, pady=5,side="top", fill="x")
reporte.pack(padx=10, pady=5,side="top", fill="x")
principal.mainloop()
