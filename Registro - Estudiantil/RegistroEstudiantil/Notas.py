import psycopg2
class Notas:
    def __init__(self):
        self.estudiantes = {}
        self.conn = psycopg2.connect(
            dbname="Escuelita",
            user="postgres",
            password="root",
            host="localhost",
            port ="5432"
        )
        self.cur = self.conn.cursor()

    def registrar_estudiante(self, estudiante, materias):
        self.cur.execute("INSERT INTO estudiantes (nombre_completo, fecha_nacimiento, carrera) VALUES (%s, %s, %s) RETURNING id_estudiante", 
        (estudiante.nombreCompleto, estudiante.fechaNacimiento, estudiante.carrera))
        id_estudiante = self.cur.fetchone()[0]
        for materia, nota in materias.items():
        # Registrar la materia si no existe
            self.cur.execute("INSERT INTO materias (nombre, creditos) VALUES (%s, %s) RETURNING id_materia",
                (materia.nombre, materia.creditos))
            id_materia = self.cur.fetchone()[0]
        # Insertar la nota
            self.cur.execute("INSERT INTO notas (id_estudiante, id_materia, nota) VALUES (%s, %s, %s)", 
                (id_estudiante, id_materia, nota))
        self.conn.commit()


    def ver_lista_estudiantes(self):
        return list(self.estudiantes.values())

    def ver_materias_estudiante(self, id_estudiante):
        estudiante = self.estudiantes.get(id_estudiante)
        if estudiante:
            return estudiante.ver_materias_inscritas()
        else:
            return "Estudiante no encontrado"

    def ver_notas_estudiante(self, id_estudiante):
        estudiante = self.estudiantes.get(id_estudiante)
        if estudiante:
            return estudiante.materias
        else:
            return "Estudiante no encontrado"

    def ver_nota_materia_estudiante(self, id_estudiante, id_materia):
        estudiante = self.estudiantes.get(id_estudiante)
        if estudiante:
            return estudiante.ver_nota(id_materia)
        else:
            return "Estudiante no encontrado"

    def calcular_promedio_estudiante(self, id_estudiante, id_materia):
        estudiante = self.estudiantes.get(id_estudiante)
        if estudiante:
            return estudiante.calcular_promedio(id_materia)
        else:
            return "Estudiante no encontrado"
        
    def ver_lista_estudiantes(self):
        try:
            self.cur.execute("SELECT * FROM estudiantes")
            estudiantes = self.cur.fetchall()
            return estudiantes
        except psycopg2.Error as e:
            print(f"Error al obtener la lista de estudiantes: {e}")
            return []

    def actualizar_informacion_estudiante(self, id_estudiante, nueva_informacion):
        estudiante = self.estudiantes.get(id_estudiante)
        if estudiante:
            for materia, nota in nueva_informacion.items():
                estudiante.materias[materia] = nota
        else:
            return "Estudiante no encontrado"
        
    def eliminar_estudiante(self, id_estudiante):
        try:
            # Eliminar las notas del estudiante
            self.cur.execute("DELETE FROM notas WHERE id_estudiante = %s", (id_estudiante,))
            # Eliminar al estudiante
            self.cur.execute("DELETE FROM estudiantes WHERE id_estudiante = %s", (id_estudiante,))
            self.conn.commit()
            return f"Estudiante con ID {id_estudiante} eliminado correctamente."
        except psycopg2.Error as e:
            self.conn.rollback()
            return f"Error al eliminar al estudiante: {e}"

    def eliminar_materia(self, id_materia):
        self.cur.execute("DELETE FROM materias WHERE id_materia = %s", (id_materia,))
        self.conn.commit()
