from Clase_Viajero import ViajeroFrecuente

from Clase_Lista import Lista as Li


import csv

import os


if __name__=='__main__':
#   -------------------------------------------- Creacion de Lista desde datos de archivo ----------------------------------------------
    lista=Li()
    archivo=open('Viajeros.csv')
    reader=csv.reader(archivo,delimiter=';')
    cargado=True
    for fila in reader:
        if(fila[0]=="NumeroDeViajero"):
            pass
        else:
            try:
                viajero = ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4].replace(',','.')))    # *** Crea una instancia de viajero frecuente que luego agrega a la lista ***
                lista.AgregaViajero(viajero)                # **** Crea la lista de viajeros en la clase Lista **** 
                cargado=True
            except ValueError:
                print("ERROR. No se ha podido cargar el archivo. El programa se cerrará")
                input("Continuar...")
                cargado=False
                break
    archivo.close()
#   -------------------------------------------- Menú de opciones ----------------------------------------------
    if(cargado==True):
        def switch(argument):
            func=switcher.get(argument,lambda:print('Opcion Incorrecta'))
            func()
        def opciona():
            res = lista.ConsultarMillas(numviaj)
            if(res == -1):
                print("El viajero no ha sido encontrado.")
            else:
                print("El viajero tiene un total de {:.2f} millas ".format(res))

            input("Enter para continuar...")
            os.system('cls')

        def opcionb():
            cant=input("Ingrese la cantidad de millas que desea acumular: ")
            try:
                cant=float(cant.replace(',','.'))
                lista.AcumularMillas(numviaj,cant)
            except ValueError:
                print ("ERROR en el ingreso de las millas")

            input("Enter para continuar...")
            os.system('cls')

        def opcionc():
            cant=input("Ingrese la cantidad de millas que desea canjear: ")
            try:
                cant=float(cant.replace(',','.'))
                lista.CanjearMillas(numviaj,cant)
            except ValueError:
                print ("ERROR en el ingreso de las millas")
        def opciond():
            pass
        switcher ={
            'a': opciona,
            'b': opcionb,
            'c': opcionc,
            'd': opciond
        }
        
        bandera=False
        while not bandera:
            nume=True
            while nume==True:
                numviaj=input("Ingrese el numero de un viajero: ")
                try:
                    numviaj=int(numviaj)
                    nume=False
                except ValueError:
                    print("Debe ingresar un numero entero.")
                    input("Presion ENTER para continuar...")
                    os.system('cls')
            print("")
            print("a. Consultar cantidad de millas")
            print("b. Acumular millas")
            print("c. Canjear milas")
            print("d. Salir")
            opcion=input("Ingrese su opcion: ")
            opcion=opcion.lower()
            switch(opcion)
            bandera= opcion =='d'