import conversor_longitud as longitud
import conversor_temperatura.celcius as celcius


print("Bienvenido a la tarea 1 \n")


while True:
    opcion1 = int(input("1 - Temperatura | 2 - Longitud | 3 - Salir \n"))
    if opcion1 == 1:
        print("Seleccione temperatura a convertir!!! \n")
        temp = int(input("1 - Celcius | 2 - Fahrenheit | 3 - Kelvin \n"))
        if temp == 1:
            print("Seleccione a que temperatura desea convertir!!! \n")
            c = int(input("1 - Fahrenheit | 2 - Kelvin \n"))
            if c == 1:
                n = float(input("Ingrese temperatura: "))
                celcius.celcius_a_fahren(n)
            elif c == 2:
                n = float(input("Ingrese temperatura: "))

        elif temp == 2:
            n = float(input("Ingrese la temperatura: "))
        elif temp == 3:
            temp = float(input("Ingrese la temperatura: "))
        else:
            print("Opcion no existente")
    elif o == 2:
        a=0
    elif o == 3:
        break
    else:
        print("Opcion no existente")
