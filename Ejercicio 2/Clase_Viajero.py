class ViajeroFrecuente:
    __NumViajero=0
    __DNI=0
    __Nombre=""
    __Apellido=""
    __MillasAcum=0.0

# -------------------------------------- Métodos get y set   -----------------------------
    def getNum(self):
        return self.__numViaejero
    def setNum(self, num):
        try:
            self.__numViaejero=int(num)
        except ValueError:
            print ("ATENCIÓN: No se pudo asignar correctamente el valor Numero de Viajero")
    def getDni(self):
        return self.__dni
    def setDni(self, dni):
        self.__dni=dni
    def getNom(self):
        return self.__nombre
    def setNom(self, nom):
        self.__nombre=nom
    def getApell(self):
        return self.__apellido
    def setApell(self, ape):
        self.__apellido=ape
    def getMillas(self):
        return float(self.__millasAcum)
    def setMillas(self, millas):
        self.__millasAcum=float(millas)
# -------------------------------------- Métodos solicitados -----------------------------
    def __init__(self, num, dni, nom, apell,millas):
        self.setNum(num),self.setDni(dni), self.setNom(nom)
        self.setApell(apell), self.setMillas(millas)
        
    def cantidadTotaldeMillas(self):
        return str(self.__millasAcum)

    def acumularMillas(self,recorridas):
        self.__millasAcum = self.__millasAcum + recorridas
        
    def canjearMillas(self,cantidad):
        self.__millasAcum = self.__millasAcum - cantidad    