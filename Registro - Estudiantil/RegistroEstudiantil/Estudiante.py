class Estudiante:
    def __init__(self, id_estudiante, nombre, apellido, fecha_nacimiento, carrera):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera
        self.materias = {}
        self.notas = {}
        
    def inscribir_materia(self, materia, notas):
        self.materias[materia.id_materia] = materia
        self.notas[materia.id_materia] = notas
        
