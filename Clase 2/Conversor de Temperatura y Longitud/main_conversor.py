import conversor_longitud.kilometros as kilometros
import conversor_longitud.millas as millas
import conversor_longitud.metros as metros
import conversor_longitud.pies as pies
import conversor_temperatura.celcius as celcius
import conversor_temperatura.fahrenheit as fahrenheit
import conversor_temperatura.kelvin as kelvin


print("Bienvenido a la tarea 1 \n")


while True:
    print("Seleccione el modo de conversion!!! \n")
    opcionModo = int(input("1 - Temperatura | 2 - Longitud | 3 - Salir \n"))

    if opcionModo == 1:

        print("Seleccione Temperatura a convertir!!! \n")
        opcionTemp = int(input("1 - Celcius | 2 - Fahrenheit | 3 - Kelvin \n"))

        if opcionTemp == 1: # Celcius
            print("Seleccione a que temperatura desea convertir!!! \n")
            a = int(input("1 - Fahrenheit | 2 - Kelvin \n"))
            if a == 1:
                n = float(input("Ingrese temperatura: "))
                celcius.celcius_a_fahren(n)
            elif a == 2:
                n = float(input("Ingrese temperatura: "))
                celcius.celcius_a_kelvin(n)

        elif opcionTemp == 2: # Fahrenheit
            print("Seleccione a que temperatura desea convertir!!! \n")
            a = int(input("1 - Celcius | 2 - Kelvin \n"))
            if a == 1:
                n = float(input("Ingrese temperatura: "))
                fahrenheit.fahr_a_celcius(n)
            elif a == 2:
                n = float(input("Ingrese temperatura: "))
                fahrenheit.fahr_a_kelvin(n)

        elif opcionTemp == 3: # Kelvin
            print("Seleccione a que temperatura desea convertir!!! \n")
            a = int(input("1 - Celcius | 2 - Fahrenheit \n"))
            if a == 1:
                n = float(input("Ingrese temperatura: "))
                kelvin.kelvin_a_celcius(n)
            elif a == 2:
                n = float(input("Ingrese temperatura: "))
                kelvin.kelvin_a_fahrenheit(n)

        else:
            print("Opcion no existente\n")

    elif opcionModo == 2:
        print("Seleccione Longitud a convertir!!! \n")
        opcionLong = int(input("1 - Kilometros | 2 - Millas | 3 - Metros | 4 - Pies \n"))

        if opcionLong == 1:
            print("Seleccione a que longitud desea convertir!!! \n")
            a = int(input("1 - Millas | 2 - Metros | 3 - Pies \n"))
            if a == 1:
                n = float(input("Ingrese distancia: "))
                kilometros.kilom_a_millas(n)
            elif a == 2:
                n = float(input("Ingrese distancia: "))
                kilometros.kilom_a_metros(n)
            elif a == 3:
                n = float(input("Ingrese distancia: "))
                kilometros.kilom_a_pies(n)

        elif opcionLong == 2:
            print("Seleccione a que longitud desea convertir!!! \n")
            a = int(input("1 - Kilometros | 2 - Metros | 3 - Pies \n"))
            if a == 1:
                n = float(input("Ingrese distancia: "))
                millas.millas_a_kilometros(n)
            elif a == 2:
                n = float(input("Ingrese distancia: "))
                millas.millas_a_metros(n)
            elif a == 3:
                n = float(input("Ingrese distancia: "))
                millas.millas_a_pies(n)

        elif opcionLong == 3:
            print("Seleccione a que longitud desea convertir!!! \n")
            a = int(input("1 - Kilometros | 2 - Millas | 3 - Pies \n"))
            if a == 1:
                n = float(input("Ingrese distancia: "))
                metros.metros_a_kilom(n)
            elif a == 2:
                n = float(input("Ingrese distancia: "))
                metros.metros_a_millas(n)
            elif a == 3:
                n = float(input("Ingrese distancia: "))
                metros.metros_a_pies(n)

        elif opcionLong == 4:
            print("Seleccione a que longitud desea convertir!!! \n")
            a = int(input("1 - Kilometros | 2 - Millas | 3 - Metros \n"))
            if a == 1:
                n = float(input("Ingrese distancia: "))
                pies.pies_a_kilometros(n)
            elif a == 2:
                n = float(input("Ingrese distancia: "))
                pies.pies_a_millas(n)
            elif a == 3:
                n = float(input("Ingrese distancia: "))
                pies.pies_a_metros(n)

        else:
            print("Opcion no existente")

    elif opcionModo == 3:
        print("Gracias por usar el conversor de unidades, hasta luego!!!")
        break

    else:
        print("Opcion no existente")
