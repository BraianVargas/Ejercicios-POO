class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0

    def __init__(self,dia=1,mes=1,año=2020,hora=0,minu=0,seg=0):
        if(dia> 0 and dia <= 31):
            self.__dia=dia
        else:
            print("Cantidad de dias invalidos")
        if (mes > 0 and mes <= 12):
            self.__mes=mes
        else:
            print("Cantidad de meses invalidos")
        if (año > 0):
            self.__año=año
        else:
            print("Cantidad de años invalidos")
        if (hora >= 0 and hora <= 24):
            self.__hora=hora
        else:
            print("Cantidad de horas invalida")
        if (minu >= 0 and minu <= 60):
            self.__minutos=minu
        else:
            print("Cantidad de minutos invalidos")
        if (seg >= 0 and seg <= 60):
            self.__segundos=seg
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
