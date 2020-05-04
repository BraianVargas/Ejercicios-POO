from ClaseAlumno import Alumno

from Manejador import Lista

import csv

import os

if __name__=='__main__':
# ------------------------------------------- Creacion de lista desde archivo -----------------------------------------
    archivo=open('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 2/2020/Practica 2/Ejercicio 5/Alumnos.csv')
    reader=csv.reader(archivo,delimiter=';')

    manejador=Lista()

    for fila in reader:
        if(fila[0] == 'Nombre'):
            pass
        else:
            Alu=Alumno(fila[0],fila[1],fila[2],fila[3])
            manejador.AgregaAlumno(Alu)
    archivo.close()
# -------------------------------------------- Menú ----------------------------------------------------
    def opcion1():
        anio=int(input("Ingrese el año: "))
        div= int(input("Ingrese la division: "))

        manejador.CalculoPorcentaje(anio,div)



    def opcion2():
        max=input("Ingrese la cantidad nueva de inasistencias permitidas: ")
        try:
            max=int(max)
            Alumno.ModificaMaximo(max)
        except ValueError:
            print("Debe ingresar un numero entero")
            input("Enter para continuar...")
    
    def opcion3():
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

    ban=False
    while ban==False:
        print("1. Ver por año porcentaje de inasistencias que supera la maxima permitida.")
        print("2. Modificar la cantidad máxima de inasistencias permitidas")
        print("3. Salir")

        opcion=int(input("Igrese su opcion: "))
        switch(opcion)
        ban = int(opcion) == 3
