from conversor_velocidad.ms import ms_a_kmh, ms_a_mph
from conversor_velocidad.mph import mph_a_kmh, mph_a_ms
from conversor_velocidad.kmh import kmh_a_ms, kmh_a_mph
from conversor_tiempo.hora import hora_a_segundos, hora_a_minutos
from conversor_tiempo.segundos import segundos_a_horas, segundos_a_minutos
from conversor_tiempo.minutos import minutos_a_horas, minutos_a_segundos
from historiales_conversion.historial import Listarhistorial, agregar_conversion, eliminar_conversion, editar_conversion, validar_conversion

def main():
    print("Bienvenido al conversor de velocidad")

    while True:
        print("""Seleccione el modo de la app de conversión:
        1. Conversor
        2. Lista de conversiones
        """)
        modo = input("Ingrese el número de la opción: ")
        if modo == "1":
            print("Has seleccionado el modo de conversión.")
            print("Seleccione la opción de conversión:")
            print("""        1. Metros por segundo (m/s)
            2. Kilómetros por hora (km/h)
            3. Millas por hora (mph)
            4. Horas (h)
            5. Segundos (s)
            6. Minutos (min)
            7. Salir""")

            opcion = input("Ingrese el número de la opción: ")
            if opcion == "1":
                velocidad = float(input("Ingrese la velocidad en m/s: "))
                print("1. m/s a km/h")
                print("2. m/s a mph")
                opcion = float(input("Ingrese el tipo de conversión (m/s): "))
                if opcion == 1:
                    agregar_conversion(ms_a_mph(velocidad))
                elif opcion == 2:
                    agregar_conversion(ms_a_kmh(velocidad))
            elif opcion == "2":
                velocidad = float(input("Ingrese la velocidad en km/h: "))
                print("1. km/h a m/s")
                print("2. km/h a mph")
                opcion = float(input("Ingrese el tipo de conversión (km/h): "))
                if opcion == 1:
                    agregar_conversion(kmh_a_ms(velocidad))
                elif opcion == 2:
                    agregar_conversion(kmh_a_mph(velocidad))
            elif opcion == "3":
                velocidad = float(input("Ingrese la velocidad en mph: "))
                print("1. mph a km/h")
                print("2. mph a m/s")
                opcion = float(input("Ingrese el tipo de conversión (mph): "))
                if opcion == 1:
                    agregar_conversion(mph_a_kmh(velocidad))
                elif opcion == 2:
                    agregar_conversion(mph_a_ms(velocidad))
            elif opcion == "4":
                hora = float(input("Ingrese la cantidad de horas: "))
                print("1. horas a segundos")
                print("2. horas a minutos")
                opcion = float(input("Ingrese el tipo de conversión (h): "))
                if opcion == 1:
                    agregar_conversion(hora_a_segundos(hora))
                elif opcion == 2:
                    agregar_conversion(hora_a_minutos(hora))
            elif opcion == "5":
                segundos = float(input("Ingrese la cantidad de segundos: "))
                print("1. segundos a horas")
                print("2. segundos a minutos")
                opcion = float(input("Ingrese el tipo de conversión (s): "))
                if opcion == 1:
                    agregar_conversion(segundos_a_horas(segundos))
                elif opcion == 2:
                    agregar_conversion(segundos_a_minutos(segundos))
            elif opcion == "6":
                minutos = float(input("Ingrese la cantidad de minutos: "))
                print("1. minutos a horas")
                print("2. minutos a segundos")
                opcion = float(input("Ingrese el tipo de conversión (min): "))  
                if opcion == 1:
                    agregar_conversion(minutos_a_horas(minutos))
                elif opcion == 2:
                    agregar_conversion(minutos_a_segundos(minutos))
            elif opcion == "7":
                print("Saliendo del conversor. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            print("Conversión realizada con éxito.")
            print("Seleccione otra opción o salga del programa.")
            print()
        elif modo == "2":
            print("Has seleccionado la lista de conversiones.")
            print("1. Mostrar lista de conversiones")
            print("2. Editar una conversión")
            print("3. Eliminar una conversión")
            opcion = input("Ingrese el número de la opción: ")
            if opcion == "1":
                Listarhistorial()
            elif opcion == "2":
                id_conversion = int(input("Ingrese el ID de la conversión a editar: "))
                if validar_conversion(id_conversion):
                    nuevo_valor = float(input("Ingrese el nuevo valor de la conversión: "))
                    editar_conversion(id_conversion, nuevo_valor)
                    print("Conversión editada correctamente.")
                else:
                    print(f"No se encontró la conversión con ID {id_conversion}.")
            elif opcion == "3":
                id_conversion = int(input("Ingrese el ID de la conversión a eliminar: "))
                if validar_conversion(id_conversion):
                    eliminar_conversion(id_conversion)
                else:
                    print(f"No se encontró la conversión con ID {id_conversion}.")
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()