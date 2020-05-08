from ClaseFechaHora import FechaHora

import gc

import os

if __name__=='__main__':
    bic=False

    print("**** Hora y Fecha1 ****")
    dia=int(input("Dia: "))
    mes=int(input("Mes: "))
    año=int(input("Año: "))
    hora=int(input("Hora: "))
    minuto=int(input("Minuto: "))
    segundo=int(input("Segundo: "))

    r=FechaHora(dia,mes,año,hora,minuto,segundo)
    r.Mostrar()
    
    try:
        dia=int(dia)
        mes=int(mes)
        año=int(año)

        if((año%400==0)or(año%100!=0 and año%4==0)):
            listames=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listames=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(dia<=listames[mes-1] and dia > 0):
            bic=False
        else:
            print("La fecha ingresada no es válida") 
            bic=True
    except ValueError:
        print("Debe ingresar Numeros enteros")

    def opcion1():
        print("*********** SUMAR HORAS ********")
        print("")
        try:            
            print("**** Hora 2 ****")
            hora1=int(input("Ingrese Hora: "))
            #minutos1=int(input("Ingrese Minutos: "))
            #segundos1=int(input("Ingrese Segundos: "))
            #b=FechaHora(dia, mes, año, hora1, minutos1, segundos1)
            
            c=r+hora1

            print("La suma de las horas es: ")
            r.Mostrar()

        except ValueError:
            print("Debe ingresar Numeros enteros")

        gc.collect()
        input("Enter para continuar...")
        os.system('cls')

    def opcion2():
        print("*********** RESTAR HORAS ********")
        print("")
        try:
            print("**** Hora 2 ****")
            hora1=int(input("Ingrese Hora: "))
            #minutos1=int(input("Ingrese Minutos: "))
            #segundos1=int(input("Ingrese Segundos: "))
            #b=FechaHora(dia, mes, año, hora1, minutos1, segundos1)
            
            c=r-hora1
            
            if(c!=-1):
                print("La Resta de las horas es: ")
                r.Mostrar()
            else:
                print("No se ha podido relizar la resta. Intente Nuevamente")

        except ValueError:
            print("Debe ingresar Numeros enteros")

        gc.collect()   
        input("Enter para continuar...")
        os.system('cls')

    def opcion3():
        print("*********** COMPARACION DE HORAS ********")
        print("")
        try:
            print("**** Hora 2 ****")
            print("")
            hora1=int(input("Ingrese Hora: "))
            #minutos1=int(input("Ingrese Minutos: "))
            #segundos1=int(input("Ingrese Segundos: "))
            #b=FechaHora(dia, mes, año, hora1, minutos1, segundos1)

            c=r>hora1
            if(c==1):
                print("(Hora 1) es mayor: ",hora)
            elif(c==0):
                print("(Hora 2) es mayor: ",hora1)
            else:
                print("Las horas ingresadas son iguales")    
        except ValueError:
            print("Debe ingresar Numeros enteros")

        gc.collect()   
        input("Enter para continuar...")
        os.system('cls')


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


    if bic== False:
        ban = False
        while not ban:
            print("1. Sumar Hora")
            print("2. Restar Hora")
            print("3. Distinguir entre dos horas cuál es mayor")
            print("4. Salir")

            opcion=input("Ingrese su opcion: ")
            opcion=int(opcion)
            switch(opcion)
            ban = int(opcion) == 4
    
    input("Presione ENTER para continuar")
