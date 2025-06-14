print("Programa de evaluacion de notas de alumnos")
nota_alumno = input("Introduce la nota del alumno: ")

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
        nuva_variable = "" #Al crear una variable dentro del if solo se puede usar en este condicional
    return valoracion

print(evaluacion(int(nota_alumno)))


