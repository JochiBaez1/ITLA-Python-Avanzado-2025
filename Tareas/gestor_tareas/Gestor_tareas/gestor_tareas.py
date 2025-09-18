import json
from Gestor_tareas.tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="data/tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar()

    def agregar(self, tarea: Tarea):
        self.tareas.append(tarea)
        self.guardar()

    def eliminar(self, titulo):
        self.tareas = [t for t in self.tareas if t.titulo != titulo]
        self.guardar()

    def modificar(self, titulo, nueva_tarea: Tarea):
        for i, t in enumerate(self.tareas):
            if t.titulo == titulo:
                self.tareas[i] = nueva_tarea
                break
        self.guardar()

    def listar(self, estado=None, prioridad=None):
        resultado = self.tareas
        if estado:
            resultado = [t for t in resultado if t.estado == estado]
        if prioridad:
            resultado = [t for t in resultado if t.prioridad == prioridad]
        return resultado

    def guardar(self, archivo=None):
        if archivo is None:
            archivo = self.archivo
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([t.guardar() for t in self.tareas], f, indent=4)

    def cargar(self, archivo=None):
        if archivo is None:
            archivo = self.archivo
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.tareas = [Tarea.leer(d) for d in datos]
        except FileNotFoundError:
            self.tareas = []
