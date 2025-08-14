import datetime
dichistorial = {}
idIncrement = 1


def Listarhistorial():
    if dichistorial:
        for clave,valor in dichistorial.items():
            print(f"ID conversión: {clave}, Valor: {valor[0]}, Fecha: {valor[1]}\n")  
    else:
        print('No hay conversiones creadas \n')

def agregar_conversion(valor):
    global idIncrement
    fecha = datetime.datetime.now()
    dichistorial[idIncrement] = (valor, fecha)
    print(f"Conversión agregada con ID: {idIncrement}, Valor: {valor}, Fecha: {fecha}\n")
    idIncrement += 1

def eliminar_conversion(id_conversion):
    if id_conversion in dichistorial:
        del dichistorial[id_conversion]
        print(f"Conversión con ID {id_conversion} eliminada.\n")
    else:
        print(f"No se encontró la conversión con ID {id_conversion}.\n")

def editar_conversion(id_conversion, nuevo_valor):
    if id_conversion in dichistorial:
        fecha = datetime.datetime.now()
        dichistorial[id_conversion] = (nuevo_valor, fecha)
        print(f"Conversión con ID {id_conversion} actualizada a {nuevo_valor} en {fecha}.\n")
    else:
        print(f"No se encontró la conversión con ID {id_conversion}.\n")

def validar_conversion(id_conversion):
    if id_conversion in dichistorial:
        return True
    else:
        return False