class Lista:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def AgregaAlumno(self, alu):
        self.__lista.append(alu)

    def Mostrar_Lista(self):
        print("Lista: \n")
        i=0
        for i in range(len(self.__lista)):
            self.__lista[i].Mostrar()
    
    def CalculoPorcentaje(self,anio,div):
        i=0
        nombre=None
        print("Alumno       Porcentaje")
        for i in range(len(self.__lista)):
            porcent=self.__lista[i].Porcentaje(anio, div,1)
            nombre=self.__lista[i].Porcentaje(anio, div,2)
            if(nombre==None):
                pass
            else:
                print("{}       {:.2f}%" .format(nombre,porcent))
            i+=1