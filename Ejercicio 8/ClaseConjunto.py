class Conjunto:
    __lista=[]

    def __init__(self):
        self.__lista=[]
       
            
    def Agrega(self,elem):
        self.__lista.append(elem)

    def retornaValor (self):
        return self.__lista
    
    def AgregaCjto(self, long):
        i=0
        for i in range(long):
            print("")
            elem=input("Elemento {}: ".format(i+1))
            try:
                elem=int(elem)
                self.__lista.append(elem)
                i+=1
            except ValueError:
                print("Debe ingresar un numero entero")
                i=i                


    def __add__(self,cjto):
        nueva=[]
        nueva.extend(self.__lista)
        nueva.extend(cjto.retornaValor())
        nueva=set(nueva)
        return nueva

    def __sub__(self,cjto):
        lista=[]
        lista.extend(self.__lista)
        conjunto = cjto.retornaValor()
        for valor in conjunto:
            if valor in lista:
                lista.remove(valor)
        return (lista)


    def __eq__(self, cjto):
        if not isinstance(cjto, self.__class__):
            return False
        return sorted(self.__lista) == sorted(cjto.__lista)

    def Mostrar(self):
        self.__lista.sort()
        print(self.__lista)
        
