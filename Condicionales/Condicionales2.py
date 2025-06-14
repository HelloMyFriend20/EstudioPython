print("Verificacion de acceso: ")
edad_usuario = int(input("Introduce tu edad por favor: "))

if edad_usuario < 18 and 2 == 2:
    print("No puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("puedes pasar")

print("El programa ha finalizado ")

nota_alumno = int(input("Ingrese su nota: "))
if nota_alumno < 5:
    print("Reprobado")
elif nota_alumno < 6:
    print("Aprobado")
elif nota_alumno < 7:
    print("Bien aprobado")
elif nota_alumno < 9:
    print("Superior")
else:
    print("Sobresaliente")