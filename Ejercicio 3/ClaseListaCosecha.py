import numpy as np
class ListaCosecha:
    __lista=np.emty()

    def __init__(self):
        self.__lista=np.emty((45,20))
        
    def inicial(self):
        i=j=0
        for i in range(45):
            for j in range(20):
                self.__lista[i,j]=0

    def AgregaCosecha(self,cosecha):
        self.__lista.append(cosecha)
    