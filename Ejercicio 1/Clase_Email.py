class Email:
    __idCuenta=0
    __dominio=""
    __TipoDominio=""
    __Contraseña=""
#--------------------------------Constructor--------------------------
    def __init__(self,id,dominio,TipoDominio,Contraseña):
        self.__idCuenta=id
        self.__dominio=dominio
        self.__TipoDominio=TipoDominio
        self.__Contraseña=Contraseña        
    
#--------------Métodos get y set------------------------
    def setID(self,i):
        self.__idCuenta=i
    def getID(self):
        return self.__idCuenta
    def setDominio(self, dom):
        self.__dominio=dom
    def getDominio(self):
        return self.__dominio
    def setTipo(self,tipo):
        self.__TipoDominio=tipo
    def getTipo(self):
        return self.__TipoDominio
    def setContraseña(self,cont):
        self.__Contraseña=cont
    def getContraseña(self):
        return self.__Contraseña
#--------------------------------Métodos-------------------------------
    def retornaEmail(self):
        return (self.__idCuenta + "@" + self.__dominio + '.' +self.__TipoDominio)

    def MostrarDatos(self):
        print("ID de cuenta: " + self.__idCuenta)
        print("Dominio: " + self.__dominio)
        print("Tipo de dominio: " + self.__TipoDominio)
        print("Contraseña: " + self.__Contraseña)
        
    def crearCuenta(self,direccion):
        idCuenta = direccion.split("@")
        self.__idCuenta=idCuenta[0]
        domi = idCuenta[1].split(".")
        self.__dominio=domi[0]
        self.__TipoDominio=domi[1]

