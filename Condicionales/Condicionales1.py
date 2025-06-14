print("Programa de evaluacion de notas de alumnos")
nota_alumno = input("Introduce la nota del alumno: ")

def evaluacion(nota_alumno): #No importa si el nombre del parametro es diferente: Vease linea 11
    valoracion = "aprobado"
    if nota_alumno < 5:
        valoracion = "suspenso"
        nueva_variable = "" #Al crear una variable dentro del if solo se puede usar en este condicional
    return valoracion

print(evaluacion(int(nota_alumno))) # Aqui se llenan los valores del parametro


