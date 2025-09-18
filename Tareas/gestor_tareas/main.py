import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Gestor_tareas.gestor_tareas import GestorTareas
from Gestor_tareas.tarea import Tarea

class App:
    def __init__(self, root):
        self.gestor = GestorTareas()
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("900x600")

        # espacio superior para añadir tareas
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="x")

        ttk.Label(frame, text="Título:").pack(side="left")
        self.titulo_entry = ttk.Entry(frame, width=20)
        self.titulo_entry.pack(side="left", padx=5)
        
        ttk.Label(frame, text="Descripción:").pack(side="left")
        self.desc_entry = ttk.Entry(frame, width=30)
        self.desc_entry.pack(side="left", padx=5)

        self.prioridad = ttk.Combobox(frame, values=["Alta", "Media", "Baja"], width=7)
        self.prioridad.set("Media")
        self.prioridad.pack(side="left", padx=5)

        add_btn = ttk.Button(frame, text="Añadir", command=self.agregar_tarea)
        add_btn.pack(side="left", padx=5)

        # espacio de filtros
        filtro_frame = ttk.Frame(root, padding=5)
        filtro_frame.pack(fill="x")

        ttk.Label(filtro_frame, text="Estado:").pack(side="left")
        self.filtro_estado = ttk.Combobox(filtro_frame, values=["Todas", "Pendiente", "Completada"], width=12)
        self.filtro_estado.set("Todas")
        self.filtro_estado.pack(side="left", padx=5)

        ttk.Label(filtro_frame, text="Prioridad:").pack(side="left")
        self.filtro_prioridad = ttk.Combobox(filtro_frame, values=["Todas", "Alta", "Media", "Baja"], width=10)
        self.filtro_prioridad.set("Todas")
        self.filtro_prioridad.pack(side="left", padx=5)

        ttk.Label(filtro_frame, text="Buscar por título:").pack(side="left")
        self.buscar_entry = ttk.Entry(filtro_frame, width=20)
        self.buscar_entry.pack(side="left", padx=5)

        ttk.Button(filtro_frame, text="Aplicar", command=self.cargar_lista).pack(side="left", padx=5)

        # Lista de tareas
        self.tree = ttk.Treeview(root, columns=("titulo", "desc", "estado", "prioridad"), show="headings")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("desc", text="Descripción")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("prioridad", text="Prioridad")
        self.tree.pack(fill="both", expand=True, pady=10)

        # Botones inferiores
        btn_frame = ttk.Frame(root)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(btn_frame, text="Marcar Completada", command=self.marcar_completada).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Modificar", command=self.modificar_tarea).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Exportar JSON", command=self.exportar_json).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Importar JSON", command=self.importar_json).pack(side="left", padx=5)

        self.cargar_lista()

    
    # Funciones
    def agregar_tarea(self):
        titulo = self.titulo_entry.get()
        desc = self.desc_entry.get()
        prio = self.prioridad.get()
        if titulo:
            tarea = Tarea(titulo, desc, "Pendiente", prio)
            self.gestor.agregar(tarea)
            self.cargar_lista()
        else:
            messagebox.showwarning("Error", "El título es obligatorio")

    def cargar_lista(self):
        estado_filtro = self.filtro_estado.get()
        prioridad_filtro = self.filtro_prioridad.get()
        busqueda = self.buscar_entry.get().lower()

        for row in self.tree.get_children():
            self.tree.delete(row)

        if estado_filtro == "Todas":
            tareas = self.gestor.listar()
        else:
            tareas = self.gestor.listar(estado=estado_filtro)

        # Aplicar filtro por prioridad y búsqueda
        tareas_filtradas = []
        for t in tareas:
            if (prioridad_filtro == "Todas" or t.prioridad == prioridad_filtro) and \
               (busqueda in t.titulo.lower()):
                tareas_filtradas.append(t)

        for t in tareas_filtradas:
            self.tree.insert("", "end", values=(t.titulo, t.descripcion, t.estado, t.prioridad))

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Info", "Seleccione una tarea")
            return
        item = self.tree.item(seleccion[0])["values"]
        nueva = Tarea(item[0], item[1], "Completada", item[3])
        self.gestor.modificar(item[0], nueva)
        self.cargar_lista()

    def modificar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Info", "Seleccione una tarea")
            return
        item = self.tree.item(seleccion[0])["values"]

        # Ventana emergente
        win = tk.Toplevel(self.root)
        win.title("Modificar tarea")
        win.geometry("400x250")

        ttk.Label(win, text="Título:").pack(pady=5)
        titulo_entry = ttk.Entry(win, width=30)
        titulo_entry.insert(0, item[0])
        titulo_entry.pack()

        ttk.Label(win, text="Descripción:").pack(pady=5)
        desc_entry = ttk.Entry(win, width=40)
        desc_entry.insert(0, item[1])
        desc_entry.pack()

        ttk.Label(win, text="Prioridad:").pack(pady=5)
        prio_combo = ttk.Combobox(win, values=["Alta", "Media", "Baja"], width=10)
        prio_combo.set(item[3])
        prio_combo.pack()

        def guardar_cambios():
            nuevo_titulo = titulo_entry.get()
            nueva_desc = desc_entry.get()
            nueva_prio = prio_combo.get()
            nueva_tarea = Tarea(nuevo_titulo, nueva_desc, item[2], nueva_prio)
            self.gestor.modificar(item[0], nueva_tarea)
            self.cargar_lista()
            win.destroy()

        ttk.Button(win, text="Guardar", command=guardar_cambios).pack(pady=10)

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Info", "Seleccione una tarea")
            return
        item = self.tree.item(seleccion[0])["values"]
        self.gestor.eliminar(item[0])
        self.cargar_lista()

    def exportar_json(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if archivo:
            self.gestor.guardar(archivo)
            messagebox.showinfo("Éxito", "Tareas exportadas")

    def importar_json(self):
        archivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if archivo:
            self.gestor.cargar(archivo)
            self.cargar_lista()
            messagebox.showinfo("Éxito", "Tareas importadas")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
