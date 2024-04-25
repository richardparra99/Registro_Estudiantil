from ConexionPostgreSQL import ConexionPostgreSQL
from Estudiante import Estudiante



class Mi_consola:
    def __init__(self):
        self.db_connection = ConexionPostgreSQL()

    def registrar_estudiante(self, estudiante):
        query = "INSERT INTO estudiante (id_estudiante, nombre, apellido, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s, %s)"
        values = (estudiante.id_estudiante, estudiante.nombre, estudiante.apellido, estudiante.fecha_nacimiento, estudiante.carrera)
        self.db_connection.ejecutar_query(query, values)
        print("Estudiante registrado exitosamente.")

    def actualizar_estudiante(self, id_estudiante, nombre, apellido, fecha_nacimiento, carrera):
        query = "UPDATE estudiante SET nombre = %s, apellido = %s, fecha_nacimiento = %s, carrera = %s WHERE id_estudiante = %s"
        values = (nombre, apellido, fecha_nacimiento, carrera, id_estudiante)
        self.db_connection.ejecutar_query(query, values)
        print("Información del estudiante actualizada exitosamente.")

    def eliminar_estudiante(self, id_estudiante):
        query = "DELETE FROM estudiante WHERE id_estudiante = %s"
        values = (id_estudiante,)
        self.db_connection.ejecutar_query(query, values)
        print("Estudiante eliminado exitosamente.")

    def actualizar_materia(self, id_materia, nombre_materia, creditos):
        query = "UPDATE materia SET nombre_materia = %s, creditos = %s WHERE id_materia = %s"
        values = (nombre_materia, creditos, id_materia)
        self.db_connection.ejecutar_query(query, values)
        print("Información de la materia actualizada exitosamente.")

    def eliminar_materia(self, id_materia):
        query = "DELETE FROM materia WHERE id_materia = %s"
        values = (id_materia,)
        self.db_connection.ejecutar_query(query, values)
        print("Materia eliminada exitosamente.")

    def listar_estudiantes(self):
        query = "SELECT * FROM estudiante"
        estudiantes = self.db_connection.consultar_datos(query)
        if estudiantes:
            for estudiante in estudiantes:
                print(estudiante)

    def ver_materias_estudiante(self, id_estudiante):
        query = "SELECT m.id_materia, m.nombre_materia, m.creditos FROM materia m JOIN estudiante_materia em ON m.id_materia = em.cod_materia WHERE em.id_estudiante = %s"
        values = (id_estudiante,)
        materias = self.db_connection.consultar_datos(query, values)
        if materias:
            print("Materias inscritas por el estudiante:")
            for materia in materias:
                print(f"ID: {materia[0]}, Nombre: {materia[1]}, Créditos: {materia[2]}")
        else:
            print("El estudiante no está inscrito en ninguna materia.")

    def ver_notas_estudiante_materia(self, id_estudiante, id_materia):
        query = "SELECT * FROM notas WHERE id_estudiante = %s AND cod_materia = %s"
        values = (id_estudiante, id_materia)
        notas = self.db_connection.consultar_datos(query, values)
        if notas:
            for nota in notas:
                print(f"Notas del estudiante en la materia:")
                print(f"ID de la nota: {nota[0]}")
                print(f"Primer parcial: {nota[1]}")
                print(f"Segundo parcial: {nota[2]}")
                print(f"Examen final: {nota[3]}")
        else:
            print("No hay notas registradas para este estudiante en esta materia.")

    def calcular_promedio_estudiante_materia(self, id_estudiante, id_materia):
        query = "SELECT primer_parcial, segundo_parcial, examen_final FROM notas WHERE id_estudiante = %s AND cod_materia = %s"
        values = (id_estudiante, id_materia)
        notas = self.db_connection.consultar_datos(query, values)
        if notas:
            total_notas = sum(sum(nota) for nota in notas)
            cantidad_notas = len(notas) * 3
            promedio = total_notas / cantidad_notas
            print(f"El promedio de notas del estudiante en la materia es: {promedio:.2f}")
        else:
            print("No hay notas registradas para este estudiante en esta materia.")

if __name__ == "__main__":
    consola = Mi_consola()
    while True:
        print("1. Registrar nuevo estudiante")
        print("2. Actualizar información de un estudiante")
        print("3. Eliminar estudiante")
        print("4. Actualizar información de una materia")
        print("5. Eliminar materia")
        print("6. Ver lista de estudiantes")
        print("7. Ver materias de un estudiante")
        print("8. Ver notas de un estudiante en una materia")
        print("9. Calcular promedio de notas de un estudiante en una materia")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_estudiante = input("Ingrese ID del estudiante: ")
            nombre = input("Ingrese nombre del estudiante: ")
            apellido = input("Ingrese apellido del estudiante: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
            carrera = input("Ingrese carrera del estudiante: ")
            nuevo_estudiante = Estudiante(id_estudiante, nombre, apellido, fecha_nacimiento, carrera)
            consola.registrar_estudiante(nuevo_estudiante)
        elif opcion == "2":
            id_estudiante = input("Ingrese ID del estudiante a actualizar: ")
            nombre = input("Ingrese nuevo nombre del estudiante: ")
            apellido = input("Ingrese nuevo apellido del estudiante: ")
            fecha_nacimiento = input("Ingrese nueva fecha de nacimiento (YYYY-MM-DD): ")
            carrera = input("Ingrese nueva carrera del estudiante: ")
            consola.actualizar_estudiante(id_estudiante, nombre, apellido, fecha_nacimiento, carrera)
        elif opcion == "3":
            id_estudiante = input("Ingrese ID del estudiante a eliminar: ")
            consola.eliminar_estudiante(id_estudiante)
        elif opcion == "4":
            id_materia = input("Ingrese ID de la materia a actualizar: ")
            nombre_materia = input("Ingrese nuevo nombre de la materia: ")
            creditos = input("Ingrese nuevos créditos de la materia: ")
            consola.actualizar_materia(id_materia, nombre_materia, creditos)
        elif opcion == "5":
            id_materia = input("Ingrese ID de la materia a eliminar: ")
            consola.eliminar_materia(id_materia)
        elif opcion == "6":
            consola.listar_estudiantes()
        elif opcion == "7":
            id_estudiante = input("Ingrese el ID del estudiante: ")
            consola.ver_materias_estudiante(id_estudiante)
        elif opcion == "8":
            id_estudiante = input("Ingrese el ID del estudiante: ")
            id_materia = input("Ingrese el ID de la materia: ")
            consola.ver_notas_estudiante_materia(id_estudiante, id_materia)
        elif opcion == "9":
            id_estudiante = input("Ingrese el ID del estudiante: ")
            id_materia = input("Ingrese el ID de la materia: ")
            consola.calcular_promedio_estudiante_materia(id_estudiante, id_materia)
        elif opcion == "10":
            consola.db_connection.cerrar_conexion()
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")