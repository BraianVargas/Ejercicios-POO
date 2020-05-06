from ClaseFechaHora import FechaHora

from ClaseHora import Hora

if __name__ == '__main__':
    d = int(input("Ingrese Dia: "))
    mes = int(input("Ingrese Mes: "))
    a = int(input("Ingrese Año: "))
    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f = FechaHora(d,mes,a,h, m, s)
    f.Mostrar()
    input()
    h1 = int(input("Ingrese Hora: "))
    m1 = int(input("Ingrese Minutos: "))
    s1 = int(input("Ingrese Segundos: "))
    r = Hora(h1, m1, s1)
    r.Mostrar()
    input()
    print("Suma de F+R. \n")
    f2 = f + r
    f2.Mostrar()
    input()
    print("Suma de R+F. \n")
    f3 = r + f
    f3.Mostrar()
    input()
    print("Resta de F3-1. (Resta un numero a la fecha) \n")
    f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de
    # días indicada por el número entero
    f4.Mostrar()
    print("Suma de 1 + F2. (Suma un numero a la fecha) \n")
    f4 = 1 + f2 # suma un día a un objeto FechaHora
    f4.Mostrar()
    input()
    input()