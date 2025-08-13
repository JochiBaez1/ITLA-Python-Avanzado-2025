#Gestor Incidencias

import Clases.GestorIncidentes as GI

print("Bienvenido al Gestor de Incidencias!!!\n")

while True:
    opcion = int(input("1-Listar | 2-Crear | 3-Modificar | 4-Eliminar "))

    if opcion == 1:
        GI.listarIncidentes()
    elif opcion == 2:
        subject = input("Subject: ")
        descripcion = input("Descripcion: ")
        user = input("User: ")
        GI.crearIncidentes(subject,descripcion,user)

    elif opcion == 3:
        clave = int(input("Digita el numero del incidente a modificar: "))
        if GI.validarIncidentes(clave):
            op = int(input("1- Subject | 2- Descripcion"))
            if op == 1:
                valorModificado = input("Inserte el Subject: ")
                GI.modificarIncidentes(clave,op,valorModificado)

    elif opcion == 4:
        pass