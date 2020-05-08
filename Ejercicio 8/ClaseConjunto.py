import gc
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
        print('Fecha: {}/{}/{}'.format(self.__dia, self.__mes, self.__año))
        print('Hora: {}:{}:{}'.format(self.__hora, self.__minutos, self.__segundos))

# ____________________________________________________ Suma y resta de fecha y hora _______________________________
    
    def __add__ (self,horas):
        if(horas<24 and horas > 0):
            self.__hora+=horas
            if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
                listames=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listames=[31,28,31,30,31,30,31,31,30,31,30,31]

            if(self.__hora>23):
                self.__hora -= 24
                self.__dia += 1
            if(self.__dia > listames[self.__mes-1]):
                self.__dia -= listames[self.__mes-1]
                self.__mes += 1
            if(self.__mes > 12):
                self.__mes -=12
                self.__año += 1
    
    def __sub__ (self,resta):
        if((self.__año%400==0)or(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(resta >= 0):
            self.__hora-=resta
            if(self.__hora<0):
                self.__hora+=24
                self.__dia-=1
            if(self.__dia==0):
                if(self.__mes==1):
                    self.__dia=listames[11]
                    self.__mes=12
                    self.__año-=1 
                else:
                    self.__mes-=1
                    self.__dia=listames[self.__mes-1]
        else:
            print("Usted ingreso un numero Real por favor vuelva a ingresar un numero entero positivo")

# _______________________________________________ Comparacion de horarios ___________________________________________
    def __gt__(self,obj):
        if(self.__hora>obj):
            return 1
        else:
            return 0

    gc.collect()
