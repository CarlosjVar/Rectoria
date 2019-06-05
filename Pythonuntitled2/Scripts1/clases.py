class Persona():
    "Atributos"
    cedula=0
    nombreCompleto=""
    telefono=0
    voto=0
    
    "Médotos"
    def __init__(self,ced,nC,tel):
        self.cedula=ced
        self.nombreCompleto=nC
        self.telefono=tel
        return

    def setVoto (self,vot):
        self.voto=vot
        return

    def getVoto (self):
        return self.voto

    def getTelefono (self):
        return self.telefono

    def getCedula (self):
        return self.cedula
    
    def getnombreCompleto (self):
        return self.nombreCompleto

class Estudiante (Persona):
    "Atributos"
    carnet=""
    carrera=""
    tipo=""

    "Metodos"
    def __init__(self,ced,nC,tel,crnt):
        self.carnet=crnt
        self.tipo="estudiante"
        Persona.__init__(self,ced,nC,tel)

    def setCarrera(self,carre):
        self.carrera=carre
        return

    def getCarrera (self,carre):
        return self.carrera

    def getTipo (self):
        return self.tipo

    def getCarnet(self):
        return self.carnet

    def mostrar (self):
        print("Tipo: "+self.tipo)
        print("Cédula: "+str(self.cedula))
        print("Telefono: "+str(self.telefono))
        print("Nombre: "+self.nombreCompleto)
        print("Carnet: "+str(self.carnet))
        print("Carrera: "+str(self.carrera))
        print("*******************")
        return

class Profesor(Persona):
    "Atributos"
    publicaciones=""
    candidato=""
    tipo=""
    
    "Métodos"
    def __init__(self,ced,nC,tel,pub):
        self.publicaciones=pub
        self.tipo="profesor"
        Persona.__init__(self,ced,nC,tel)

    def setCandidato(self,cand):
        self.candidato=cand
        return
    
    def getCandidato (self):
        return self.candidato

    def getPublicaciones(self):
        return self.publicaciones

    def getTipo (self):
        return self.tipo

    def mostrar (self):
        print("Tipo: "+self.tipo)
        print("Cédula: "+str(self.cedula))
        print("Telefono: "+str(self.telefono))
        print("Nombre: "+self.nombreCompleto)
        print("Publicaciones: "+self.publicaciones)
        print("Candidatura: "+self.candidato)
        print("*******************")
        return

class Administrativo(Persona):
    "Atributos"
    puesto=""
    extension=""
    tipo=""

    "Métodos"
    def __init__(self,ced,nC,tel,pst,ext):
        self.puesto=pst
        self.extension=ext
        self.tipo="administrativo"
        Persona.__init__(self,ced,nC,tel)

    def getExtension(self):
        return self.extension

    def getPuesto(self):
        return self.puesto

    def getTipo (self):
        return self.tipo

    def mostrar(self):
        print("Tipo: "+self.tipo)
        print("Cédula: "+str(self.cedula))
        print("Telefono: "+str(self.telefono))
        print("Nombre: "+self.nombreCompleto)
        print("Puesto: "+self.puesto)
        print("Extensión: "+str(self.extension))
        print("*******************")
        return

    

    

    
    
    
        

    
    






    
    
    
