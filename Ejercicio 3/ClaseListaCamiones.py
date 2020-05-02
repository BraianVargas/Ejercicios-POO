class ListaCamiones:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def AgregaCamion(self,camion):
        self.__lista.append(camion)
    def getPatente(self, i):
        return self.__lista[i].getPatente()

    def getNombre(self, i):
        return self.__lista[i].getNombre()

    def getTara(self, i):
        return self.__lista[i].getTara()
    