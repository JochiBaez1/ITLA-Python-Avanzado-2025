import datetime
import csv
import os

dichistorial = {}
idIncrement = 1


NOMBRE_ARCHIVO = "historial_conversiones.csv"

def inicializar_csv():
    """Crea el archivo CSV si no existe, con encabezados."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["ID conversión", "Valor", "Fecha"])


def Listarhistorial():
    inicializar_csv()
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
        if filas:
            for fila in filas:
                print(f"ID conversión: {fila['ID conversión']}, Valor: {fila['Valor']}, Fecha: {fila['Fecha']}\n")
        else:
            print("No hay conversiones creadas\n")


def obtener_ultimo_id():
    """Devuelve el último ID usado en el CSV."""
    inicializar_csv()
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        ids = [int(fila["ID conversión"]) for fila in lector]
        return max(ids) if ids else 0


def agregar_conversion(valor):
    inicializar_csv()
    nuevo_id = obtener_ultimo_id() + 1
    fecha = datetime.datetime.now()
    with open(NOMBRE_ARCHIVO, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nuevo_id, valor, fecha])
    print(f"Conversión agregada con ID: {nuevo_id}, Valor: {valor}, Fecha: {fecha}\n")


def eliminar_conversion(id_conversion):
    inicializar_csv()
    encontrado = False
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

    with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID conversión", "Valor", "Fecha"])
        for fila in filas:
            if int(fila["ID conversión"]) != id_conversion:
                escritor.writerow([fila["ID conversión"], fila["Valor"], fila["Fecha"]])
            else:
                encontrado = True

    if encontrado:
        print(f"Conversión con ID {id_conversion} eliminada.\n")
    else:
        print(f"No se encontró la conversión con ID {id_conversion}.\n")


def editar_conversion(id_conversion, nuevo_valor):
    inicializar_csv()
    encontrado = False
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

    with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID conversión", "Valor", "Fecha"])
        for fila in filas:
            if int(fila["ID conversión"]) == id_conversion:
                fecha = datetime.datetime.now()
                escritor.writerow([id_conversion, nuevo_valor, fecha])
                encontrado = True
                print(f"Conversión con ID {id_conversion} actualizada a {nuevo_valor} en {fecha}.\n")
            else:
                escritor.writerow([fila["ID conversión"], fila["Valor"], fila["Fecha"]])

    if not encontrado:
        print(f"No se encontró la conversión con ID {id_conversion}.\n")

def validar_conversion(id_conversion):
    inicializar_csv()
    id_conversion = str(id_conversion).strip()
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["ID conversión"].strip() == id_conversion:
                return True
    return False
