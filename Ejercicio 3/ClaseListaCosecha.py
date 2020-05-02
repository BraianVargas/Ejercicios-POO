from ClaseListaCamiones import ListaCamiones

import os

class ListaCosecha:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def AgregaCosecha(self,cosecha):
        self.__lista.append(cosecha)

    def CargaTabla(self,listaCamion):
        self.__lista[0].CereoTabla()
        
        for i in range(len(self.__lista)):
            ban=True
            idcamion = dia = j = 0 
            peso = taracamion = neto = 0.0

            idcamion=int(self.__lista[i].getID())
            dia=int(self.__lista[i].getDia())
            peso=float(self.__lista[i].getPeso())
            
            if(idcamion > 0 and dia > 0) and (idcamion<=20 and dia<=45):
                while (ban==True) and (j>=0)and(j<20):
                    if(int(self.__lista[j].getID()) == idcamion):
                        taracamion=float(listaCamion.getTara(j))          # *** Obtiene la tara del camion ***
                        j=j+1
                        ban=False
                    else:
                        j=j+1
                        ban=True
                neto = peso - taracamion                                    # *** Calculo del peso neto descargado ***
                
                self.__lista[i].setTabla(dia-1,idcamion-1,float(neto))          # *** Almacenamiento en lista bidimencional ***
                idcamion = taracamion = neto = 0
                i=i+1
        print("Datos de cosecha cargados correctamente.")
        input("Presione ENTER para continuar...")
        os.system('cls')