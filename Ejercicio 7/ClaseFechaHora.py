class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0

    def __init__ (self, dia=1, mes=1,year=2020,hora=0,minutos=0,segundos=0):
        if((hora<=24 and hora>0)and (minutos<=60 and minutos>=0) and(segundos<=60 and segundos>=0) and (mes>0 and mes<=12)):
            if((year%400==0)or(year%100!=0 and year%4==0)):
                listames=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listames=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=listames[mes-1] and dia > 0):
                self.__dia = dia
                self.__mes = mes
                self.__año = year
                self.__hora = hora
                self.__minutos = minutos
                self.__segundos = segundos
            else:
                print("El dia esta fuera de rango")
        else:
            print("Hubo un error, verifique hora,minuto,segundos y mes")

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
    def __add__ (self,obj):
        dia=self.__dia
        mes=self.__mes
        year=self.__año
        hora=self.__hora
        minuto=self.__minutos
        segundo=self.__segundos
        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(obj)==int):
            if(obj>0):
                dia+=obj
                while(dia>listames[mes-1]):
                    if(mes==12):
                        mes=1
                        year+=1
                    else:
                        mes+=1
                return FechaHora(dia,mes,year,hora,minuto,segundo)
            else:
                print("Ingresar un valor positivo")
        else:
            hora+=obj.getHora()
            minuto+=obj.getMinutos()
            segundo+=obj.getSeg()
            if(minuto>=60):
                if(minuto==60):
                    minuto=1
                    hora+=1
                else:
                    minuto =minuto - 60
                    hora += 1
            if(hora>24):
                hora -= 24
                dia += 1
            if(dia > listames[mes-1]):
                dia -= listames[mes-1]
                mes += 1
            if(mes > 12):
                mes -=12
                year += 1
            return(FechaHora(dia,mes,year,hora,minuto,segundo))

    def __radd__ (self,obj):
        dia=self.__dia
        hora=self.__hora
        mes=self.__mes
        year=self.__año
        segundo=self.__segundos
        minuto=self.__minutos
        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(obj)==int):
            if(obj>-1):
                dia+=obj
                while(dia>listames[mes-1]):
                    if(mes==12):
                        mes=1
                        year+=1
                    else:
                        mes+=1
                return FechaHora(dia,mes,year,hora,minuto,segundo)
            else:
                print("Ingresar un valor positivo")
        else:
            hora+=obj.getHora()
            minuto+=obj.getMinutos()
            segundo+=obj.getSeg()
            if(minuto>=60):
                if(minuto == 60):
                    minuto=1
                    hora+=1
                else:
                    minuto -= 60
                    hora += 1
            if(hora>24):
                hora -= 24
                dia += 1
            if(dia > listames[mes-1]):
                dia -= listames[mes-1]
                mes += 1
            if(mes > 12):
                mes -=12
                year += 1
            return(FechaHora(dia,mes,year,hora,minuto,segundo))

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
                    mes-=1
            return FechaHora(dia,mes,year,self.__hora,self.__minutos,self.__segundos)
        else:
            print("Usted ingreso un numero Real por favor vuelva a ingresar un numero entero positivo")
