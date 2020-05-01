class camion:
    __identificador=0
    __nombre=""
    __patente=""
    __marca=""
    __tara=0.0

#--------------------------------------------- Métodos get y set ------------------------------------------
    def getID(self):
        return self.__identificador
    def setID(self,ident):
        self.__identificador=ident
    def getNombre(self):
        return self.__nombre
    def setNombre(self, Nom):
        self.__nombre=Nom
    def getPatente(self):
        return self.__patente
    def setPatente(self, pat):
        self.__patente=pat
    def getMarca(self):
        return self.__marca
    def setMarga(self, marca):
        self.__marca=marca
    def getTara(self):
        return self.__tara
    def setTara(self, tara):
        self.__tara=tara
#--------------------------------------------------- Métodos propios --------------------------------------
    def __init__(self,id,nom,pat,marca,tara):
        self.__identificador=id 
        self.__nombre=nom 
        self.__patente= pat 
        self.__marca=marca 
        self.__tara=tara
        
    
