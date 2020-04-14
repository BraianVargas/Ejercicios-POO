import csv

from Clase_Email import Email 

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
            mail=Email(nomCuenta,dominio,tipo,contr)
            print ("Estimado "+ nombre +", te enviaremos tus mensajes a la direccion " + mail.retornaEmail()) #--- Muestra mensaje solicitado ---
            a=False
        else:
            print ("Contraseña Incorrecta, reingrese su contraseña.")
            contr=input("Ingrese su contraseña: \n")
            reing=input("Reingrese su contraseña: \n")
#-----------------------------Fin Validacion de contraseña------------------------------------------------------


#-------------------------------Menú para opciones de incisos 2 al 4 -------------------------------------------    
    print ("1. Modificar Contraseña.")
    print ("2. Mostrar datos de correo por separado.")
    print ("3. Leer Datos desde archivo.")
    print ("4. Salir")
    opcion=int(input("Elige una opcion: "))
     
    while(opcion != 4):
        #-----------------------Opcion 1 -------------------------------
        if opcion == 1:
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
        #------------------------Opcion 2 -------------------------------
        elif opcion == 2:
            email=Email("","","","")
            correo=input("Ingrese su correo elecronico: \n")
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

        #------------------------Opcion 3 -------------------------------
        elif opcion == 3:
            archivo=open('Correos.csv')
            reader = csv.reader(archivo,delimiter=';')
            domi=input("Ingrese el dominio a saber la cantidad: ")
            cont=0
            for fila in reader:
                if(str(fila[1]) == domi):
                    cont+=1
            print("La cantidad de correos con dominio " + domi + " es: " + str(cont))
            archivo.close()

        print ("1. Modificar Contraseña.")
        print ("2. Mostrar datos de correo por separado.")
        print ("3. Leer Datos desde archivo.")
        print ("4. Salir")
        opcion=int(input("Elige una opcion: "))

    input("Presione Enter para continuar...")


