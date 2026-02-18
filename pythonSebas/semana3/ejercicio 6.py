# Nombre del estudiante
# Edad
# Promedio final
# Si aprobó (el promedio es mayor o igual a 3.0)
# Lista de materias inscritas
# Código del estudiante (dato no modificable)
# Número de materias aprobadas (sin repetir)
# Requerimientos:
# Crear las variables usando el tipo de dato correcto.
# Determinar automáticamente si el estudiante aprobó usando operadores relacionales.
# Verificar el tipo de cada variable con type().
# Crear un diccionario que agrupe toda la información.
# Actualizar el promedio final aplicando una operación aritmética (corrección de nota).
# Eliminar una materia del listado usando operaciones sobre listas.

nombreEstudiante=input("¿Cuál es el nombre del estudiante?")
edad=int(input("¿Cuál es la edad del estudiante?"))
promedioFinal=float(input("¿Cuál es su promedio final?"))

def cualcularPromedio(promedioFinal):
    aprueba=promedioFinal>=3.0
    return aprueba

aprobado=cualcularPromedio(promedioFinal)
print(f"es estudiante {nombreEstudiante}")

asigIncritas=["Sociales",  "Quimica", "Fisica", "Español"]
codEstudiante=(583577,)

print(type(nombreEstudiante))
print(type(edad))
print(type(promedioFinal))
print(type(asigIncritas))
print(type(codEstudiante))


asigIncritas.remove("Quimica")
asigAprobadas=len(set(asigIncritas))

infoEstudiante={
    "Nombre":nombreEstudiante,
    "Edad":edad,
    "Promedio":promedioFinal,
    "Asignaturas":asigIncritas,
    "Asignaturas aprobadas":asigAprobadas,
    "ID Estudiante":codEstudiante,
}

corrPromedio=promedioFinal+0.2

print("\nLa información del estudiante es:")
print(infoEstudiante)