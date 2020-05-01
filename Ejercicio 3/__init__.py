from clase_camion import camion

from clase_cosecha import cosecha

import csv

import os

if __name__=='__main__':
    
    listaCamion=[]
    listaCosecha=[]

    banCamion=False
    banCosecha=False
#-------------------------------------- Carga archivo "camiones.csv" -------------------------------------
    ArchCamion=open('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 2/2020/Practica 2/Ejercicio 3 (Listas Bidimencionales)/Camiones.csv')
    readerCamion=csv.reader(ArchCamion, delimiter=';')

    for fila in readerCamion:
        if(fila[0] !="Identificador"):
            if( (int(fila[0])>=1) and (int(fila[0])<=20) ):
                cam= camion(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4].replace(',','.')))
                listaCamion.append(cam)                                                          #Creación de lista de Camiones
                banCamion=True
            else:pass
        else:
            pass    

    ArchCamion.close()              
#-------------------------------------- Carga archivo "cosecha.csv" --------------------------------------
    ArchCosecha=open('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 2/2020/Practica 2/Ejercicio 3 (Listas Bidimencionales)/cosecha.csv')
    readerCosecha=csv.reader(ArchCosecha, delimiter=';')
    for fila1 in readerCosecha:
        if(fila1[0]!="Id"):
            if( (int(fila1[0])>0) and (int(fila1[0])<=20) ) and ( (int(fila1[1])>0) and (int(fila1[1])<=45) ):
                cos= cosecha(int(fila1[0]),int(fila1[1]),float(fila1[2].replace(',','.')))
                listaCosecha.append(cos)                                                 #Creación de lista de cosecha
                banCosecha=True
            else: pass
        else:
            pass

    ArchCosecha.close()
#-------------------------------------- Carga de arreglo bidimencional -------------------------------------------------
    i = 0
    ban=True
    listaCosecha[i].inicial()

    for i in range(len(listaCosecha)):
        ban=True
        idcamion = dia = j = 0 
        peso = taracamion = neto = 0.0

        idcamion=int(listaCosecha[i].getID())
        dia=int(listaCosecha[i].getDia())
        peso=float(listaCosecha[i].getPeso())
        
        if(idcamion > 0 and dia > 0) and (idcamion<=20 and dia<=45):
            while ban and (j<20):
                if(int(listaCamion[j].getID()) == idcamion):
                    taracamion=float(listaCamion[j].getTara())          # *** Obtiene la tara del camion ***
                    j=j+1
                    ban=False
                else:
                    j=j+1
                    ban=True
            neto = peso - taracamion                                    # *** Calculo del peso neto descargado ***
            
            listaCosecha[i].setTabla(dia-1,idcamion-1,float(neto))          # *** Almacenamiento en lista bidimencional ***
            idcamion = taracamion = neto = 0
            i=i+1
#-------------------------------------- Menú de opciones -------------------------------------------------
    if(banCamion==True and banCosecha== True):
        def opcion1():              # ********* Dado el número de identificador de un camión mostrar, la cantidad total de kilos descargados *********
            i = j = 0
            totalDescar = 0.0
            k=True
            
            idcam=input("Ingrese el identificador del camión (Numero Entero): ")
            try:
                idcam=int(idcam)
                if (idcam>0) and (idcam<=20):
                    obj=cosecha("","","")
                    for i in range(45):                             # *** Range(45) por la cantidad total de dias ***
                        k=True
                        while k:
                            if(j==idcam):
                                totalDescar = float(totalDescar) + float(obj.getTabla(i,idcam-1))     # *** Acumulador de cantidad de kilos descargados por un camion a lo largo de los 45 dias ***
                                k=False
                            else: j=j+1
                        i=i+1
                    print("El total de kilos descargados por el camion es de {:.2f} .".format(totalDescar))
                    input("Enter para continuar...")
                    os.system('cls')
                else: 
                    print ("Identificador Incorrecto.")
                    input("Enter para continuar...")
                    os.system('cls')
            except (ValueError):                                         # *** Capta el error del valor del identificador. Verifica que se ingrese un numero entero como se solicita ***
                print ("Identificador Incorrecto.")
        def opcion2():              # ********* Dado un número correspondiente a un día mostrar un listado con formato ********* 
            patente=""
            conductor=""
            kilos=0.0
            i=0

            dia=input("Ingrese el dia a ver: ")
            try:
                dia=int(dia)
                if(dia>0 and dia<=45):
                    obje=cosecha("","","")
                    print('Patente     Conductor     Cantidad de kilos')
                    for i in range(20):                 # *** Range(20) por la cantidad de camiones existentes en el archivo ***
                        patente = listaCamion[i].getPatente()
                        conductor = listaCamion[i].getNombre()
                        kilos = float(obje.getTabla(dia-1,i))            # *** i es el identificador del camion ***
                        i = i+1
                        print("{}     {}            {:.2f}" .format(patente,conductor,kilos))

                else:
                    print("El dia ingresado es incorrecto. ")
                    input("Enter para continuar...")
                    os.system('cls')
            except (ValueError):
                print("El dia ingresado es incorrecto. ")
                input("Enter para continuar...")
                os.system('cls')

        def opcion3():      # *** SALIR ***
            pass

        switcher ={
            1: opcion1,
            2: opcion2,
            3: opcion3
        }
        def switch(argument):
            func=switcher.get(argument,lambda:print('Opcion Incorrecta'))
            func()
            input("Enter para continuar...")
            os.system('cls')
            
        
        bandera=False
        while not bandera:
            print ("")
            print ("1. Mostrar cantidad total de kilos descargados por camion")
            print ("2. Ver listado por dia")
            print ("3. Salir")

            opcion=int(input("Igrese su opcion: "))
            switch(opcion)
            bandera = int(opcion) == 3
    else: 
        print ("Ha ocurrido un error. El programa se cerrará.")
        
    input("Enter para continuar...")
