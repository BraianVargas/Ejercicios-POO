import gc
class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0

    def __init__(self,dia=1,mes=1,año=2020,hora=0,minu=0,seg=0):
        self.__dia=dia
        self.__mes=mes
        self.__año=año
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
            self.__dia+=1
        if(self.__dia>=31 and self.__mes!=2):
            self.dia=dia-31
            self.__mes+=1
            if(self.__mes>12):
                self.__mes=1
                self.__año+=1
        elif(self.__dia==28 and self.__mes==2):             # *** Valida si el año es bisiesto
            if(self.__año%100==0):          
                if(self.__año%400==0):
                    self.dia+=1
                elif(self.__año%4==0):
                    self.dia+=1
                else:
                    self.dia=1
                    self.__mes+=1
                    if(self.__mes>12):
                        self.__mes=1
                        self.__año+=1

    def Mostrar(self):
        print('Fecha: {}/{}/{}'.format(self.__dia, self.__mes, self.__año))
        print('Hora: {}:{}:{}'.format(self.__hora, self.__minutos, self.__segundos))

    def PonerEnHora(self,hora=0, minutos=0, seg=0):
        if (hora >= 0 and hora <= 24):
            self.__hora=hora
            if (minutos >= 0 and minutos < 60):
                self.__minutos=minutos
                if (seg >= 0 and seg < 60):
                    if(seg==0):
                        seg=self.__segundos
                    else:
                        self.__segundos=seg
                else:
                    print("Cantidad de segundos invalidos")
            else:
                print("Cantidad de minutos invalidos")
        else:
            print("Cantidad de horas invalida")

    def AdelantarHora(self, h=0, m=0, s=0):

        if (h >= 0 and h <= 24):
            self.__hora+=h
        else:
            print("Cantidad de horas invalida")
        if (m >= 0 and m < 60):
            self.__minutos+=m
        else:
            print("Cantidad de minutos invalidos")
        if (s >= 0 and s < 60):
            self.__segundos+=s
        else:
            print("Cantidad de segundos invalidos")


        if(self.__segundos>=60):
            self.__segundos=0
            self.__minutos+=1
        if(self.__minutos>=60):
            self.__minutos=0
            self.__hora+=1
        if(self.__hora>=24):
            self.__hora=0
            self.__dia+=1
        if(self.__dia>=31 and self.__mes!=2):
            self.dia=0
            self.__mes+=1
            if(self.__mes>12):
                self.__mes=1
                self.__año+=1
        elif(self.__dia==28 and self.__mes==2):             # *** Valida si el año es bisiesto
            if(self.__año%100==0):          
                if(self.__año%400==0):
                    self.dia+=1
                elif(self.__año%4==0):
                    self.dia+=1
                else:
                    self.dia=1
                    self.__mes+=1
                    if(self.__mes>12):
                        self.__mes=1
                        self.__año+=1
# ____________________________________________________ Suma y resta de fecha y hora _______________________________
    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    def getSeg(self):
        return self.__segundos

    def __add__(self,obj):
        h=(self.__hora + obj.getHora())
        m=(self.__minutos+obj.getMinutos())
        s=(self.__segundos+obj.getSeg())
        obj.__init__(self.__dia,self.__mes,self.__año,h,m,s)
        return obj
    
    def __sub__(self,obj):
        ban=True
        if(self.__hora >= obj.getHora()):
            h=(self.__hora - obj.getHora())
            if(self.__minutos >= obj.getMinutos()):
                m=(self.__minutos - obj.getMinutos())
                if(self.__segundos >= obj.getSeg()):
                    s=(self.__segundos - obj.getSeg())
                else:
                    print("Los segundos deben ser menores")
                    ban=False
            else:
                print("Los minutos deben ser menores")
                ban=False
        else:
            print("Las horas deben ser menores")
            ban=False
        if(ban==True):
            obj.__init__(self.__dia,self.__mes,self.__año,h,m,s)
            return obj
        else:
            return -1
# _______________________________________________ Comparacion de horarios ___________________________________________
    def __gt__(self,obj):
        if(self.__hora == obj.getHora()):
            if(self.__minutos == obj.getMinutos()):
                if(self.__segundos == obj.getSeg()):
                    return 2
                elif(self.__segundos > obj.getSeg()):
                    return 1
                else: return 0
            elif(self.__minutos > obj.getMinutos()):
                return 1
            else:
                return 0
        elif(self.__hora > obj.getHora()):
            return 1
        else:
            return 2

    gc.collect()