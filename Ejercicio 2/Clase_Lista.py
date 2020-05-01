class Lista:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def AgregaViajero(self,viajer):
        self.__lista.append(viajer)

    def ConsultarMillas(self,numViaj):
        cant=-1
        for nodo in self.__lista:
            if(numViaj == nodo.getNum()):       # *** Compara el numero ingresado con los de los objetos de la lista ***
                cant=nodo.getMillas()           # *** Asigna a "cant" la cantidad de millas que posee el viajero. ***
        if(cant==-1):
            return cant
        else:
            return cant
    def AcumularMillas(self,nviaj,acum):
        ban=False
        anterior=0
        nuevo=0
        for nodo in self.__lista:
            if(nviaj == nodo.getNum()):       # *** Compara el numero ingresado con los de los objetos de la lista ***
                anterior=nodo.getMillas()
                nuevo=anterior+acum
                nodo.acumularMillas(acum)
                ban=True
        if(ban==True):
            print("*** Millas Asignadas correctamente. *** ")
            print("")
            print("    Cantidad anterior de millas: {:.2f}".format(anterior))
            print("    Cantidad Nueva de millas: {:.2f}".format(nuevo))
            print("\n")
        else:
            print("No se ha podido asignar millas. Posible numero de viajero inexistente")
            
        
    def CanjearMillas(self,num,cant):
        ban=False
        anterior=0
        nuevo=0
        for nodo in self.__lista:
            if(num == nodo.getNum()):       # *** Compara el numero ingresado con los de los objetos de la lista ***
                anterior=nodo.getMillas()
                if(anterior>=cant):
                    nuevo=anterior-cant
                    nodo.canjearMillas(cant)
                    ban=True
                else:
                    ban=-1
        if(ban==True):
            print("*** Millas Canjeadas correctamente. ***")
            print("")
            print("    Cantidad anterior de millas: {:.2f}".format(anterior))
            print("    Cantidad Nueva de millas: {:.2f}".format(nuevo))
            print("\n")
        elif(ban==-1):
            print("No se ha podido canjear millas. La cantidad ingresada es mayor a la acumulada por el viajero.")
        else:
            print("No se ha podido canjear millas. Posible numero de viajero inexistente")