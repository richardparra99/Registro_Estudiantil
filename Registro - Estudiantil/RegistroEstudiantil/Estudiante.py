class Estudiante:
    def __init__(self, id_estudiante, nombreCompleto, fechaNacimiento, carrera):
        self.id_estudiante = id_estudiante
        self.nombreCompleto = nombreCompleto
        self.fechaNacimiento = fechaNacimiento
        self.carrera = carrera
        self.materias = {}

    def inscribir_materia(self, materia, notas):
        self.materias[materia.id_materia] = notas

    def ver_materias_inscritas(self):
        return list(self.materias.keys())

    def ver_nota(self, materia):
        return self.materias.get(materia, "Materia no encontrada")

    def calcular_promedio(self, materia):
        nota = self.materias.get(materia)
        if nota:
            return nota
        else:
            return "No hay nota registrada para esta materia"
