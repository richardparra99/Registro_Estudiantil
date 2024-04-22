import Estudiante as estudiante
import Materia as materia
import Notas as nota

if __name__ == "__main__":
    
    notas = nota.Notas()

    # aqui creamos al estudiante y materia
    estudiante1 = estudiante.Estudiante(1, "Sergio Aguirre", "2000-01-01", "Ingeniería - Sistemas")
    materias_juan = {materia.Materia(1, "Matemáticas", 4): 90, materia.Materia(2, "Ciencias", 3): 85}

    #notas.registrar_estudiante(estudiante1, materias_juan)
    #print("Estudiante registrado con éxito.")
    
    #resultado = notas.eliminar_materia(2) # elimino mediante la id 
    #print("se elimino materia", resultado)
    
    print("Lista de estudiantes registrados:")
    print(notas.ver_lista_estudiantes())

    #print("\nMaterias inscritas por Juan:")
    #print(notas.ver_materias_estudiante(1))

    #print("\nNota de Juan en Matemáticas:")
    #print(notas.ver_nota_materia_estudiante(1, 1))
    
    #print("\nPromedio de notas de Juan en Matemáticas:")
    #print(notas.calcular_promedio_estudiante(1, 1))
    
    #print("\nActualizacion de informacion de registro:")
    #nueva_informacion = {"Matemáticas": 95, "Ciencias": 90}  # Nuevas notas o información a actualizar
    #print(notas.actualizar_informacion_estudiante(1, nueva_informacion))
    
    #print("\nEliminar estudiante:")
    #print(notas.eliminar_estudiante(1))  # Eliminar el estudiante con ID 1
    
    #print("\nEliminar materia:")
    #print(notas.eliminar_materia(1))  # Eliminar la materia con ID 1
    