#Operadores logicos "and" y "or"

print("Programa de Becas 2025")
distancia_escuela = int(input("Introduzca la distancia en KM: "))
numero_hermanos = int(input("Introduce el numero de hermanos: "))
salario_familiar = int(input("Introduce salario anual bruto: "))

#Si no cumple las primera pero si la tercera aplicara a beca.
if distancia_escuela >= 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Aplica beca")
else:
    print("No aplica beca")


print("Asignaturas optativas 2025")
print("Informatica Grafica - Pruebas de software - Usabilidad y accesibilidad")
asignatura = input("Escribe la asignatura escogida: ").lower()

if asignatura.capitalize() in ("Informatica grafica","Pruebas de software", "Usabilidad y accesibilidad"):
    print(f'Asignatura elegida: {asignatura.title()}')
else:
    print("La asignatura escogida no esta contemplada")
