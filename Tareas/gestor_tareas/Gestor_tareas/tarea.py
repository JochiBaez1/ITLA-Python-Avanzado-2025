class Tarea:
    def __init__(self, titulo, descripcion, estado="Pendiente", prioridad="Media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.prioridad = prioridad

    #convierte a diccionario
    def guardar(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "prioridad": self.prioridad
        }

    #recibe un diccionario y devuelve un objeto
    @staticmethod
    def leer(data):
        return Tarea(
            data["titulo"], data["descripcion"],
            data.get("estado", "Pendiente"),
            data.get("prioridad", "Media")
        )
