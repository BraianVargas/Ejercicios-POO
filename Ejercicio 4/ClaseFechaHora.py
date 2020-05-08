class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0

    def __init__ (self, dia=1, mes=1,year=2020,hora=0,minutos=0,segundos=0):
        if((hora<=24 and hora>=0)and (minutos<=60 and minutos>=0) and(segundos<=60 and segundos>=0) and (mes>0 and mes<=12)):
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


        if((self.__año%400==0)and(self.__año%100!=0 and self.__año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
            
            if(self.__segundos>=60):
                self.__segundos=0
                self.__minutos+=1
            if(self.__minutos>=60):
                self.__minutos=0
                self.__hora+=1
            if(self.__hora>23):
                self.__hora -= 24
                self.__dia += 1
            if(self.__dia > listames[self.__mes-1]):
                self.__dia -= listames[self.__mes-1]
                self.__mes += 1
            if(self.__mes > 12):
                self.__mes -=12
                self.__año += 1
