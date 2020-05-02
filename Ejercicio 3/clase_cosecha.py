import numpy as np

class cosecha:
    __id=None
    __dia=None
    __peso=None

    __tabla = np.empty((45,20))           #Arreglo Bidimensional

    def CereoTabla(self):
        i=j=0
        for i in range(45):
            for j in range(20):
                self.__tabla[i,j]=0
    
    def __init__(self,id,dia,peso):
        self.__id=id
        self.__dia=dia
        self.__peso=peso

    def setTabla(self,dia,id,valor):
        self.__tabla[dia,id]=self.__tabla[dia,id] + valor

    def getTabla(self,dia,id):
        return self.__tabla[dia,id]
    
    def getDia(self):
        return self.__dia
    def getID(self):
        return self.__id
    def getPeso(self):
        return self.__peso

    def MuestraDatos(self):
        print(str(self.__id))
        print(str(self.__dia))
        print(str(self.__peso))