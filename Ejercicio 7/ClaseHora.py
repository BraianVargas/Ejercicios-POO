class Hora:
    __hora=0
    __minutos=0
    __segundos=0

    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    def getSeg(self):
        return self.__segundos

    def __init__(self,hora=0,minu=0,seg=0):
        self.__hora=hora
        self.__minutos=minu
        self.__segundos=seg
        
        if(self.__segundos>=60):
            self.__segundos=seg-60
            if(self.__segundos<0):
                self.__segundos=self.__segundos*(-1)
            self.__minutos+=1
        if(self.__minutos>=60):
            self.__minutos=minu-60
            if(self.__minutos<0):
                self.__minutos=self.__minutos*(-1)
            self.__hora+=1
        if(self.__hora>=24):
            self.__hora=(hora-24)
            if(self.__hora<0):
                self.__hora=self.__hora*(-1)

    def __radd__(self,obj):
        h=(self.__hora + obj.getHora())
        m=(self.__minutos+obj.getMinutos())
        s=(self.__segundos+obj.getSeg())
        obj.__init__(h,m,s)
        return obj

    def Mostrar(self):
        print('Hora: {}:{}:{}'.format(self.__hora, self.__minutos, self.__segundos))
