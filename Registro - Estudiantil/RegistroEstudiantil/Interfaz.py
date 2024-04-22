from ConexionPostgreSQL import ConexionPostgreSQL
import tkinter as tk
from tkinter import simpledialog, messagebox
import Notas as nota
from Estudiante import Estudiante
from Materia import Materia

class Interfaz:
    def __init__(self, master, conexion_bd):
        self.master = master
        self.conexion_bd = conexion_bd
        master.title("Sistema de Notas")
        master.geometry("600x400")  # Tamaño inicial de la ventana principal

        self.button_listar_estudiantes = tk.Button(master, text="Ver Lista de Estudiantes", command=self.mostrar_lista_estudiantes)
        self.button_listar_estudiantes.pack()

        self.button_registrar_estudiante = tk.Button(master, text="Registrar Nuevo Estudiante", command=self.registrar_estudiante)
        self.button_registrar_estudiante.pack()

        self.notas = nota.Notas()  # Instancia de Notas
        self.lista_estudiantes = []  # Lista para almacenar los estudiantes
        self.ventana_lista = None  # Inicializamos ventana_lista como None
        
    def mostrar_lista_estudiantes(self):
        # Mostrar la lista de estudiantes en la interfaz
        if self.lista_estudiantes:
            if self.ventana_lista:
                self.ventana_lista.destroy()

            self.ventana_lista = tk.Toplevel(self.master)
            self.ventana_lista.title("Lista de Estudiantes Registrados")
            self.ventana_lista.geometry("400x300")

            lista_estudiantes_frame = tk.Frame(self.ventana_lista)
            lista_estudiantes_frame.pack()

            lista_estudiantes_scrollbar = tk.Scrollbar(lista_estudiantes_frame)
            lista_estudiantes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.lista_estudiantes_widget = tk.Listbox(lista_estudiantes_frame, yscrollcommand=lista_estudiantes_scrollbar.set)
            self.lista_estudiantes_widget.pack(side=tk.LEFT, fill=tk.BOTH)

            lista_estudiantes_scrollbar.config(command=self.lista_estudiantes_widget.yview)

            for estudiante in self.lista_estudiantes:
                self.lista_estudiantes_widget.insert(tk.END, estudiante)

            # Botón para ver materias
            self.button_ver_materias = tk.Button(self.ventana_lista, text="Ver Materias", command=self.ver_materias_estudiante)
            self.button_ver_materias.pack()

            # Botón para ver notas
            self.button_ver_notas = tk.Button(self.ventana_lista, text="Ver Notas", command=self.ver_notas_estudiante)
            self.button_ver_notas.pack()

            # Botón para calcular promedio total
            self.button_calcular_promedio = tk.Button(self.ventana_lista, text="Calcular Promedio", command=self.calcular_promedio_total_estudiante)
            self.button_calcular_promedio.pack()
        else:
            messagebox.showinfo("Información", "No hay estudiantes registrados.")
# Función para ver materias de un estudiante
    def ver_materias_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            materias = self.notas.ver_materias_estudiante(nombre_estudiante)
            if materias:
                messagebox.showinfo("Materias", f"El estudiante {nombre_estudiante} está inscrito en las siguientes materias:\n{', '.join(materias)}")
            else:
                messagebox.showinfo("Materias", f"El estudiante {nombre_estudiante} no está inscrito en ninguna materia.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")


    # Función para ver notas de un estudiante
    def ver_notas_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            notas = self.notas.ver_notas_estudiante(nombre_estudiante)
            if notas:
                messagebox.showinfo("Notas", f"El estudiante {nombre_estudiante} tiene las siguientes notas:\n{notas}")
            else:
                messagebox.showinfo("Notas", f"El estudiante {nombre_estudiante} no tiene notas registradas.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")

    # Función para calcular promedio total de un estudiante
    def calcular_promedio_total_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            promedio = self.notas.calcular_promedio_estudiante(nombre_estudiante)
            if promedio is not None:
                messagebox.showinfo("Promedio Total", f"El promedio total de notas del estudiante {nombre_estudiante} es: {promedio}")
            else:
                messagebox.showinfo("Promedio Total", f"No hay notas registradas para el estudiante {nombre_estudiante}.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")


    def registrar_estudiante(self):
        # Creamos una ventana secundaria para el registro del estudiante
        ventana_registro = tk.Toplevel(self.master)
        ventana_registro.title("Registro de Nuevo Estudiante")
        ventana_registro.geometry("400x300")  # Tamaño de la ventana de registro

        # Campos para ingresar los datos del estudiante
        tk.Label(ventana_registro, text="ID del Estudiante:").pack()
        id_estudiante_entry = tk.Entry(ventana_registro)
        id_estudiante_entry.pack()

        tk.Label(ventana_registro, text="Nombre Completo:").pack()
        nombreCompleto_entry = tk.Entry(ventana_registro)
        nombreCompleto_entry.pack()

        tk.Label(ventana_registro, text="Fecha de Nacimiento (YYYY-MM-DD):").pack()
        fechaNacimiento_entry = tk.Entry(ventana_registro)
        fechaNacimiento_entry.pack()

        tk.Label(ventana_registro, text="Carrera:").pack()
        carrera_entry = tk.Entry(ventana_registro)
        carrera_entry.pack()

        # Botón para guardar los datos del estudiante
        tk.Button(ventana_registro, text="Guardar", command=lambda: self.guardar_estudiante(id_estudiante_entry.get(), nombreCompleto_entry.get(), fechaNacimiento_entry.get(), carrera_entry.get(), ventana_registro)).pack()

    def guardar_estudiante(self, id_estudiante, nombreCompleto, fechaNacimiento, carrera, ventana_registro):
        if id_estudiante and nombreCompleto and fechaNacimiento and carrera:
            # Llamamos al método registrar_estudiante con los datos proporcionados
            self.notas.registrar_estudiante(id_estudiante, nombreCompleto, fechaNacimiento, carrera, {})
            # Agregamos el nuevo estudiante a la lista de estudiantes
            nuevo_estudiante = f"{id_estudiante}: {nombreCompleto}"
            self.lista_estudiantes.append(nuevo_estudiante)
            # Actualizamos la lista de estudiantes en la interfaz
            self.mostrar_lista_estudiantes()  # Esta línea estaba faltando
            # Cerramos la ventana de registro después de guardar el estudiante
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Por favor ingrese todos los datos del estudiante.")

    # Función para ver materias de un estudiante
    def ver_materias_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            materias = self.notas.ver_materias_estudiante(nombre_estudiante)
            if materias:
                messagebox.showinfo("Materias", f"El estudiante {nombre_estudiante} está inscrito en las siguientes materias:\n{', '.join(materias)}")
            else:
                messagebox.showinfo("Materias", f"El estudiante {nombre_estudiante} no está inscrito en ninguna materia.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")

# Función para ver notas de un estudiante
    def ver_notas_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            notas = self.notas.ver_notas_estudiante(nombre_estudiante)
            if notas:
                messagebox.showinfo("Notas", f"El estudiante {nombre_estudiante} tiene las siguientes notas:\n{notas}")
            else:
                messagebox.showinfo("Notas", f"El estudiante {nombre_estudiante} no tiene notas registradas.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")

    # Función para calcular promedio total de un estudiante
    def calcular_promedio_total_estudiante(self):
        seleccion = self.lista_estudiantes_widget.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_estudiante = self.lista_estudiantes_widget.get(indice)
            promedio = self.notas.calcular_promedio_estudiante(nombre_estudiante)
            if promedio is not None:
                messagebox.showinfo("Promedio Total", f"El promedio total de notas del estudiante {nombre_estudiante} es: {promedio}")
            else:
                messagebox.showinfo("Promedio Total", f"No hay notas registradas para el estudiante {nombre_estudiante}.")
        else:
            messagebox.showerror("Error", "Seleccione un estudiante primero.")


if __name__ == "__main__":
    parametros_db = {
        "dbname": "escuelita",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": "5432"
    }

    conexion_bd = ConexionPostgreSQL(parametros_db)
    conexion_bd.conectar()

    root = tk.Tk()
    interfaz = Interfaz(root, conexion_bd)
    root.mainloop()
