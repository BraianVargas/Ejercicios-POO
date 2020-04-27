import csv

from Clase_Email import Email 

import re



if __name__=='__main__':
#---------------------------------------------------Ingreso de datos--------------------------    
    nombre=input("Ingrese su nombre: \n")
    nomCuenta=input("ingrese su id de cuenta: \n")
    dominio=input("Ingrese el dominio: \n")
    tipo=input("Ingrese el tipo de dominio: \n")
    contr=input("Ingrese su contraseña: \n")
    reing=input("Reingrese su contraseña: \n")
#-----------------------------Validacion de contraseña-----------------------------
    a=True
    while a:
        if(contr==reing):
            mail = Email(nomCuenta,dominio,tipo,contr)
            print ("Estimado "+ nombre +", te enviaremos tus mensajes a la direccion " + mail.retornaEmail())       #--- Muestra mensaje solicitado ---
            a=False
        else:
            print ("Contraseña Incorrecta, reingrese su contraseña.")
            contr=input("Ingrese su contraseña: \n")
            reing=input("Reingrese su contraseña: \n")
#-----------------------------Fin Validacion de contraseña------------------------------------------------------


#-------------------------------Menú para opciones de incisos 2 al 4 -------------------------------------------    
    def opcion4():
        pass

    def opcion3():
        archivo=open('Correos.csv')
        reader = csv.reader(archivo,delimiter=';')
        domi=input("Ingrese el dominio a saber la cantidad: ")
        cont=0
        for fila in reader:
            if(str(fila[1]) == domi):
                cont+=1
        print("La cantidad de correos con dominio " + domi + " es: " + str(cont))
        archivo.close()


    def opcion2():
        email=Email("","","","")
        correo=input("Ingrese su correo elecronico: \n")

        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):     # ----- Verifica correctitud de correo, si es correcto crea instancia y muestra datos 
            print("Correo correcto")
            email.crearCuenta(correo)

            """
            #------------------------------ En caso de requerir ingresar una contraseña ------------------------------
            contr=input("Ingrese su contraseña: \n")
            reing=input("Reingrese su contraseña: \n")
            a=True
            while a:
                if(contr==reing):
                    #print ("Estimado "+ nombre +", te enviaremos tus mensajes a la direccion " + mail.retornaEmail()) #--- Muestra mensaje solicitado ---
                    email.MostrarDatos()
                    a=False
                else:
                    print ("Contraseña Incorrecta, reingrese su contraseña")
                    contr=input("Ingrese su contraseña: \n")
                    reing=input("Reingrese su contraseña: \n")
            """
            email.MostrarDatos()
        else:
            print ("Correo incorrecto")

    
    def opcion1():
        a=True
        actual=input("Ingrese su contraseña actual: ")
        while a:
            if(actual==mail.getContraseña()):
                nueva=input("Ingrese la contraseña nueva: ")
                nueva2=input("Reingrese la contraseña: ")
                if nueva==nueva2:
                    mail.setContraseña(nueva2)
                    a=False
                    print("La contraseña se estableció Correctamente.")
                else:
                    print("Las contraseñas no coinciden.")
            else:
                print ("Contraseña Incorrecta, reingrese su contraseña.")
                actual=input("Ingrese su contraseña actual: ")

    switcher ={
        1: opcion1,
        2: opcion2,
        3: opcion3,
        4: opcion4
    }
    def switch(argument):
        func=switcher.get(argument,lambda:print('Opcion Incorrecta'))
        func()

    bandera=False
     
    while not bandera:
        print ("")
        print ("1. Modificar Contraseña.")
        print ("2. Mostrar datos por separado de un correo.")
        print ("3. Leer Datos desde archivo.")
        print ("4. Salir")
        opcion=int(input("Elige una opcion: "))
        switch(opcion)
        bandera= int(opcion)==4
 

    input("Presione Enter para continuar...")

