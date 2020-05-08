from ClaseConjunto import Conjunto

import gc

import os

if __name__=='__main__':
    def opcion1():
        c1=Conjunto()
        c2=Conjunto()
        print("")
        print("*** UNION DE CONJUNTOS ***")
        print("*** CONJUNTO 1 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        try:
            lon=int(lon)
            c1.AgregaCjto(lon)
            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")
        print("*** CONJUNTO 2 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        try:
            lon=int(lon)
            c2.AgregaCjto(lon)
            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")

        print("Conjunto 1:")
        c1.Mostrar()
        print("Conjunto 2:")
        c2.Mostrar()


        if(c1!=None and c2!=None):
            c3 = c1+c2
            print("La union de los conjuntos es: ",c3)
            gc.collect()
        else: print("No se ha podido realizar la operacion.")
        del c1,c2, c3

    def opcion2():        
        c1=Conjunto()
        c2=Conjunto()
        print("")
        print("*** DIFERENCIA DE CONJUNTOS ***")
        print("*** CONJUNTO 1 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        try:
            lon=int(lon)
            c1.AgregaCjto(lon)
            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")
        print("*** CONJUNTO 2 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        try:
            lon=int(lon)
            c2.AgregaCjto(lon)
            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")

        print("Conjunto 1:")
        c1.Mostrar()
        print("Conjunto 2:")
        c2.Mostrar()


        if(c1!=None and c2!=None):
            c3=c1-c2
            print("La suma de los conjuntos es: ",c3)
            gc.collect()
        else: print("No se ha podido realizar la operacion.")
        del c1,c2,c3

    def opcion3():        
        print("")
        print("*** IGUALDAD DE CONJUNTOS ***")
        print("*** CONJUNTO 1 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        c1=Conjunto()
        try:
            lon=int(lon)
            c1.AgregaCjto(lon)
            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")
        print("*** CONJUNTO 2 ***")
        lon=input("Igrese la cantidad de elementos del conjunto: ")
        c2=Conjunto()
        try:
            lon=int(lon)
            c2.AgregaCjto(lon)

            os.system('cls')
        except ValueError:
            print("Debe ingresar un numero entero.")

        print("Conjunto 1:")
        c1.Mostrar()
        print("Conjunto 2:")
        c2.Mostrar()

        
        if(c1!=None and c2!=None):
            if(c1==c2):
                print("Los conjuntos son iguales")
            else:
                print("Los conjuntos no son iguales")
            gc.collect()

            del c1,c2
        else: print("No se ha podido realizar la operacion.")
        input("")

    def opcion4():
        pass


    switcher ={
        1: opcion1,
        2: opcion2,
        3: opcion3,
        4: opcion4
    }

    def switch(argument):
        func=switcher.get(argument,lambda:print("Opcion Incorrecta"))
        func()

    ban=False
    while not ban:
        print("")
        print("1. Union de conjuntos.")
        print("2. Diferencia de conjuntos")
        print("3. Comparar igualdad de conjuntos.")
        print("4. Salir")

        opcion=input("Ingrese una opción.")
        opcion=int(opcion)
        switch(opcion)
        ban=opcion==4
