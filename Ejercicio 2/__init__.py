from Clase_Viajero import ViajeroFrecuente

import csv

import sys

import os

if __name__=='__main__':

    lista=[] 

    millasAcum=0.0
    archivo=open('Viajeros.csv')
    reader=csv.reader(archivo, delimiter=';')
    cargado=False


    for fila in reader:
        if(fila[0]=="NumeroDeViajero"):
            pass
        else:
            try:
                viajero = ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4].replace(",",".")))
                lista.append(viajero)                    #Creación de lista de viajeros
                cargado=True
            except:
                print("Error al Cargar el archivo. El programa se cerrará")
                input("Continuar...")
                cargado=False
                break

    if(cargado==True):
        num=int(input("Ingrese el numero de viajero frecuente: "))   #Ingreso de Número de viajero por teclado.
        if(num>0 and num<=20):
            ban=True
        else:
            print("Numero de viajero Incorrecto")
            input("Continuar...")
        
        i=0
        while ban==True:
            if (i>len(lista)):
                print("ERROR. Numero de viajero Inexistente.")
                num=input("Ingrese el numero de viajero frecuente: ")   #Ingreso de Número de viajero por teclado.
            else:
                try:
                    num=int(num)
                except ValueError:
                    print ("ATENCIÓN: Debe ingresar un número entero.")
                    break
                if(num == lista[i].getNum()):
                    print("Viajero Encontrado.")
                    ban=False
                    input("Continuar...")
                else:
                    i+=1
        print (lista[i].MuestraDatos())
        # ------------------------ Comienzo de menú ----------------------------------
        def opciona():
            print("La cantiad de millas que posee es: {}" .format(float(lista[i].cantidadTotaldeMillas())))
            input("Continuar...")
            os.system('cls')
        def opcionb():
            milla = input("Ingrese la cantidad de millas a acumular: ")
            try:
                milla = float(milla)
                lista[i].acumularMillas(milla)
                print('Se actualizó la cantidad de millas acumuladas, se sumaron {} nuevas millas'.format(milla))
                input("Continuar...")
                os.system('cls')
            except ValueError:
                print ("ATENCIÓN: Debe ingresar un número entero.")
        def opcionc():
            canje=int(input("Ingrese la cantidad de millas a canjear: "))
            ban=lista[i].canjearMillas(canje)
            if( ban == True):
                print('Se actualizó la cantidad de millas acumuladas, se canjeó  un total de {} millas'.format(canje))
                input("Continuar")
                os.system('cls')

        def opciond():
            pass

        switcher ={
            'a': opciona,
            'b': opcionb,
            'c': opcionc,
            'd': opciond
        }
        def switch(argument):
            func=switcher.get(argument,lambda:print('Opcion Incorrecta'))
            func()

        bandera=False
        while not bandera:
            print ("")
            print ("a. Consultar Cantidad de millas. ")
            print ("b. Acumular millas.")
            print ("c. Canjear millas. ")  
            print ("d. Salir")
            opcion=input("Elige una opcion: ")
            opcion=opcion.lower()
            switch(opcion)
            bandera= opcion =='d'
        
        archivo.close()

        input("Enter para continuar...")