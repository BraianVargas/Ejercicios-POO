class Conjunto:
    __lista=[]

    def __init__(self,ban=0):
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
        i=j=0
        cont=0
        self.__lista.sort()
        cjto.__lista.sort()
        N=len(self.__lista) + len(cjto.__lista)

        li=Conjunto(1)
        for i in range(len(self.__lista)):
            for j in range(len(cjto.__lista)):
                if(self.__lista[i]==cjto.__lista[j]):
                    cont+=1
        cota=N-cont
        x=k=l=0
        while((x<cota) and (k < len(self.__lista)) and (l<len(cjto.__lista)) ):
            if(self.__lista[k]==cjto.__lista[l]):
                li.Agrega(self.__lista[k])
                k+=1
                l+=1
            else:
                if(self.__lista[k] < cjto.__lista[l]):
                    li.Agrega(self.__lista[k])
                    k+=1
                else:
                    li.Agrega(cjto.__lista[l])
                    l+=1
            x+=1
        if(k==len(self.__lista)):
            z=x
            for z in range(cota):
                if(l<len(cjto.__lista)):
                    li.Agrega(cjto.__lista[l])
                    l+=1
                z+=1
        if(l==len(cjto.__lista)):
            z=x
            for z in range(cota-1):
                if(l<len(self.__lista)):
                    li.Agrega(self.__lista[k])
                    k+=1
                z+=1
        return li

    def __sub__(self,cjto):
        i=j=0
        cont=0
        li=[]
        self.__lista.sort()
        cjto.__lista.sort()

        li=Conjunto(1)
        for i in range(len(self.__lista)):
            for j in range(len(cjto.__lista)):
                if(self.__lista[i]==cjto.__lista[j]):
                    cont+=1
        cota=cont
        x=0
        i=j=0
        for i in range(len(self.__lista)):
            for j in range(len(cjto.__lista)):
                if ((x<cota)and(self.__lista[i]==cjto.__lista[j])):
                    li.Agrega(self.__lista[i])
                    x+=1
                j+=1
            i+=1
        return li

    def __eq__(self, cjto):
        if not isinstance(cjto, self.__class__):
            return False
        return sorted(self.__lista) == sorted(cjto.__lista)

    def Mostrar(self):
        self.__lista.sort()
        print(self.__lista)
        