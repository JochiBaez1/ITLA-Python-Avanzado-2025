import datetime

dicIncidentes = {}
idIncrement = 0

def listarIncidentes():
    if dicIncidentes:
        for clave,valor in dicIncidentes.items():
            print(f"{clave} - subject: {valor['subject']} - descripcion: {valor['descripcion']} - user: {valor['user']} - fechaCreacion: {valor['fechaCreacion']}")
    else:
        print("No hay incidencias!!!")


def crearIncidentes(subject, descripcion, user, fechaCreacion=datetime.datetime.now()):
    global idIncrement
    dicIncidentes[idIncrement] = {
        'subject':subject,
        'descripcion':descripcion,
        'user':user,
        'fechaCreacion':fechaCreacion,
    }
    print(f"Se ha creado correctamente la incidencia {idIncrement}")
    idIncrement = idIncrement + 1

def modificarIncidentes(id, tipoModificacion, valorModificado, fechaModificacion=datetime.datetime.now()):
    if tipoModificacion == 1:
        dicIncidentes[idIncrement] = {
        'subject':valorModificado,
        'descripcion':dicIncidentes[id]['descripcion'],
        'user':dicIncidentes[id]['user'],
        'fechaCreacion':dicIncidentes[id]['fechaCreacion'],
        'fechaModificacion':fechaModificacion,
        }
        print(f"El incidente numero {id} fue modificado")
    
    elif tipoModificacion == 2:
        dicIncidentes[idIncrement] = {
        'subject':dicIncidentes[id]['subject'],
        'descripcion':valorModificado,
        'user':dicIncidentes[id]['user'],
        'fechaCreacion':dicIncidentes[id]['fechaCreacion'],
        'fechaModificacion':fechaModificacion,
        }
        print(f"El incidente numero {id} fue modificado")

def eliminarIncidentes(id):
    del dicIncidentes[id]
    print(f"El incidente numero {id} fue eliminado")

def validarIncidentes(id):
    if id in dicIncidentes:
        return True
    else:
        return False