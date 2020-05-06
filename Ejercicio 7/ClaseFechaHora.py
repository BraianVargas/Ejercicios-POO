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
        print("{}/{}/{} {}:{}:{}".format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos))

# ____________________________________________________ Metodos get _______________________________
    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    def getSeg(self):
        return self.__segundos

# ----------------------------------------------------------- Suma -----------------------------------------
    def __add__(self,obj):
        dia=self.__dia
        mes=self.__mes
        año=self.__año

        h=(self.__hora)
        m=(self.__minutos)
        s=(self.__segundos)
        
        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        
        if(type(obj)==int):
            if(obj>0):
                dia = dia + obj
                while(dia>listames[mes-1]):
                    if(mes==12):
                        mes=1
                        año = año + 1
                    else:
                        mes = mes + 1
                return FechaHora(dia,mes,año,h,m,s)
            else:
                print("Ingresar un valor positivo")
        else:
            h+=obj.getHora()
            m+=obj.getMinutos()
            s+=obj.getSeg()
            
            if(m>=60):
                if(m == 60):
                    m=1
                    h+=1
                else:
                    m -= 60
                    h += 1
            if(h>24):
                h -= 24
                dia += 1
            if(dia > listames[mes-1]):
                dia -= listames[mes-1]
                mes += 1
            if(mes > 12):
                mes -=12
                año += 1

            return FechaHora(dia,mes,año,h,m,s)

    def __radd__ (self,obj):
        dia=self.__dia
        mes=self.__mes
        año=self.__año
        
        h=self.__hora
        s=self.__segundos
        m=self.__minutos

        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(obj)==int):
            if(obj > -1):
                dia+=obj
                while(dia>listames[mes-1]):
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        mes+=1
                return FechaHora(dia,mes,año,h,m,s)
            else:
                print("Ingresar un valor positivo")
        else:
            h+=obj.getHora()
            m+=obj.getMinutos()
            s+=obj.getSeg()
            
            if(m>=60):
                if(m == 60):
                    m=1
                    h+=1
                else:
                    m -= 60
                    h += 1
            if(h>24):
                h -= 24
                dia += 1
            if(dia > listames[mes-1]):
                dia -= listames[mes-1]
                mes += 1
            if(mes > 12):
                mes -=12
                año += 1

            return(FechaHora(dia,mes,año,h,m,s))
# -------------------------------------------------------------------- Resta ------------------------------------------------
    def __sub__ (self,obj):
        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(obj > 0):
            dia=self.__dia
            mes=self.__mes
            year=self.__año
            dia = dia - obj
            while(dia<1):
                if(mes==0):
                    dia+=31
                    mes=12
                    year+=1
                else:
                    dia=listames[mes-2]
                    dia-=1 #BORRAAR
                    mes-=1
            return FechaHora(dia,mes,year,self.__hora,self.__minutos,self.__segundos)
        else:
            print("Usted ingreso un numero Real por favor vuelva a ingresar un numero entero positivo")
